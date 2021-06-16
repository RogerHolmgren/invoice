import textwrap

from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot

from reportlab.pdfgen.canvas import Canvas
from datetime import datetime
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

# https://www.learnpyqt.com/examples/python-pdf-report-generator/

class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.
    """
    error = pyqtSignal(str)
    file_saved_as = pyqtSignal(str)


class Generator(QRunnable):
    """
    Worker thread

    Inherits from QRunnable to handle worker thread setup, signals
    and wrap-up.

    :param data: The data to add to the PDF for generating.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            template = PdfReader("resources/FakturaTemplate.pdf",
                                 decompress=False).pages[0]
            template_obj = pagexobj(template)

            outfile = "target/result.pdf"
            canvas = Canvas(outfile)
            canvas.setFont('Helvetica', 10)

            xobj_name = makerl(canvas, template_obj)
            canvas.doForm(xobj_name)

            col1 = 73
            col3 = 224
            col4 = 300

            # Invoice number
            canvas.drawString(col1, 710, self.data['invoice_nr'])

            # Name
            canvas.drawString(col1, 670, self.data['name'])

            # Invoice date:
            today = datetime.today()
            canvas.drawString(col4, 710, today.strftime('%F'))

            # End date
            canvas.drawString(col3, 605, today.strftime('%F'))

            comments = self.data['comments'].replace('\n', ' ')
            if comments:
                lines = textwrap.wrap(comments, width=65) # 45
                first_line = lines[0]
                remainder = ' '.join(lines[1:])

                lines = textwrap.wrap(remainder, 75) # 55
                lines = lines[:4]  # max lines, not including the first.

                canvas.drawString(155, 223, first_line)
                for n, l in enumerate(lines, 1):
                    canvas.drawString(80, 223 - (n*28), l)

            canvas.save()

        except Exception as e:
            self.signals.error.emit(str(e))
            return

        self.signals.file_saved_as.emit(outfile)

