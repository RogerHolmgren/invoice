import os
import sys

from PyQt5.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton

from functools import partial

from generate import Generator

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()

        # Main window stuff
        self.setWindowTitle('Faktura Program')
        self.invoiceLayout = QVBoxLayout()
        self.customerLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.invoiceLayout)
        self._createMenu()

        # Create form elements
        self.name = QLineEdit()
        self.invoice_nr = QSpinBox()
        self.invoice_nr.setRange(0, 3000)
        self.comments = QTextEdit()
        self.generate_btn = QPushButton("Skapa Faktura")
        self.generate_btn.pressed.connect(self.generate)

        self.save_btn = QPushButton("Spara")
        self.save_btn.pressed.connect(self.generate) #TODO

        # Add elements to invoiceForm
        invoiceForm = QFormLayout()
        invoiceForm.addRow("Kund", self.name)
        invoiceForm.addRow("Faktura nr", self.invoice_nr)
        invoiceForm.addRow("Comments", self.comments)
        invoiceForm.addRow(self.generate_btn)
        self.invoiceLayout.addLayout(invoiceForm)

        # Add elements to addCustomerForm
        addCustomerForm = QFormLayout()
        addCustomerForm.addRow("Kund", self.name)
        addCustomerForm.addRow(self.save_btn)
        self.customerLayout.addLayout(addCustomerForm)

    def goToCreateCustomer(self):
        self._centralWidget.setLayout(self.customerLayout)


    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Meny")
        self.menu.addAction('&Lägg till kund', self.goToCreateCustomer)
        self.menu.addAction('&Avsluta', self.close)

    def generate(self):
        self.generate_btn.setDisabled(True)
        data = {
            'name': self.name.text(),
            'invoice_nr': str(self.invoice_nr.value()),
            'comments': self.comments.toPlainText()
        }
        g = Generator(data)
        g.signals.file_saved_as.connect(self.generated)
        g.signals.error.connect(print)  # Print errors to console.
        self.threadpool.start(g)

    def generated(self, outfile):
        self.generate_btn.setDisabled(False)
        try:
            os.startfile(outfile)
        except Exception:
            # If startfile not available, show dialog.
            QMessageBox.information(self, "Klar", "Faktura är skapad")


app = QApplication([])
w = MainWindow()
w.show()
app.exec()
