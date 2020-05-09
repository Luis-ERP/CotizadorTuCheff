from Layouts.AuthenticationActivity.logInActivity import LogInActivity
from Source.queryManager import QueryManager
from Database.user import User

from PyQt5 import QtGui

class LogIn(LogInActivity):
    def __init__(self, parent):
        super(LogIn, self).__init__()
        self.parent = parent
        self.db = QueryManager()
        self.user = User()

        ## ----------------------------------------------------------------- QUITAR DESPUES DE DEBUGGEAR
        self.email.setText('leramirezp@hotmail.com')
        self.password.setText('Saurio9810')

        ##event handlers
        self.btnEnter.clicked.connect(self.logInUser)
        self.btnNewUser.clicked.connect(self.parent.changeToRegisterWindow)

    def logInUser(self):
        email = self.email.text()
        password = self.password.text()
        logIn = self.db.signIn(email, password)

        if logIn == True:
            self.parent.changeToMainWindow()
        else:
            self.message.setText('Correo y/o contraseña inválidos')