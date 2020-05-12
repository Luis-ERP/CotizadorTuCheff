from Layouts.mainActivity import MainActivity, AuthenticationDialogActivity
from Source.queryManager import QueryManager
from PyQt5 import QtGui

class Main(MainActivity):
    def __init__(self):
        super().__init__()


class AuthenticationDialog(AuthenticationDialogActivity):
    def __init__(self, parent):
        super(AuthenticationDialog, self).__init__(parent)

        ##initial window
        self.changeToLogInWindow()

    def changeToMainWindow(self):
        self.mainApplication = Main()
        self.mainWindow.setCentralWidget(self.mainApplication)
        self.mainWindow.setGeometry(10, 35, 1580, 820)
        self.mainWindow.setWindowIcon(QtGui.QIcon('Res/Icons/Imagen1.png'))
        self.mainWindow.setWindowTitle("Cotizador TuCheff Eventos")

    def changeToRegisterWindow(self):
        self.mainWindow.resize(550, 250)
        self.stacker.setCurrentIndex(1)

    def changeToLogInWindow(self):
        self.mainWindow.resize(300, 250)
        self.stacker.setCurrentIndex(0)

    def changeToSuccesWindow(self):
        self.stacker.setCurrentIndex(2)

