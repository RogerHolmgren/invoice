import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton

from functools import partial

class Window(QMainWindow):
    """Main Window."""
    def __init__(self):
        """Initializer."""
        super().__init__()
        self.setWindowTitle('QMainWindow')

        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createMenu()
        self._createStatusBar()

        # Add content
        self._createForm()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Meny")
        self.menu.addAction('&Avsluta', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Statusbar")
        self.setStatusBar(status)

    def _createForm(self):
        myForm = QFormLayout()
        myForm.addRow('Name:', QLineEdit())
        myForm.addRow('Age:', QLineEdit())
        myForm.addRow('Job:', QLineEdit())
        self.generalLayout.addLayout(myForm)

class Controller:
    def __init__(self, view):
        self._view = view
        self._connectSignals()

    def _connectSignals(self):
        status = QStatusBar()
        status.showMessage("Other message")
        self._view.setStatusBar(status)
        # self._view.showMessage("Other message")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Window()
    view.show()
    Controller(view=view)
    sys.exit(app.exec_())
