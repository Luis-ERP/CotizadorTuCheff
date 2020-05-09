from PyQt5.QtWidgets import *
from PyQt5 import QtGui

from Source.Quote.quote import Quote
from Source.Databases import databases
from Source.Configuration import configuration
from Source.Help import help as helpModule
from Source.Authentication import logIn, registerUser
from Source import main


class MainActivity(QTabWidget):
    def __init__(self):
        super().__init__()

        ## declare tabs
        tab1 = Quote()
        tab2 = databases.Databases()
        tab3 = configuration.Configuration()
        tab4 = helpModule.Help()

        ## define structure
        self.addTab(tab1, "Nueva Cotización")
        self.addTab(tab2, "Bases de datos")
        self.addTab(tab3, "Configuración")
        self.addTab(tab4, "Ayuda")


class AuthenticationDialogActivity(QDialog):
    def __init__(self, parent):
        super(AuthenticationDialogActivity, self).__init__()
        self.setWindowIcon(QtGui.QIcon('Res/Icons/Imagen1.png'))
        self.mainWindow = parent

        ##declase layouts
        vLayout1 = QVBoxLayout()
        self.stacker = QStackedWidget()

        ##declare components
        self.logInWidget = logIn.LogIn(self)
        self.registerWidget = registerUser.RegisterUser(self)
        self.successResponseWindow = registerUser.SuccesfulRegister(self)

        ##set layout strucutre
        self.stacker.addWidget(self.logInWidget)
        self.stacker.addWidget(self.registerWidget)
        self.stacker.addWidget(self.successResponseWindow)
        vLayout1.addWidget(self.stacker)

        self.setLayout(vLayout1)

    def changeToMainWindow(self):
        self.mainApplication = main.Main()
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
