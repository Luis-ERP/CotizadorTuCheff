from Layouts.AuthenticationActivity.logInActivity import LogInActivity
from Source.queryManager import QueryManager
from Database.user import User

from PyQt5 import QtGui

class LogIn(LogInActivity):
    def __init__(self, parent):
        super(LogIn, self).__init__()
        self.parent = parent
        self.db = QueryManager()

        ## ----------------------------------------------------------------- QUITAR DESPUES DE DEBUGGEAR
        self.email.setText('a01702056@itesm.mx')
        self.password.setText('1234567')

        ##event handlers
        self.btnEnter.clicked.connect(self.logInUser)
        self.btnNewUser.clicked.connect(self.parent.changeToRegisterWindow)

    def logInUser(self):
        user = User()
        user.email = self.email.text()
        user.password = self.password.text()
        logIn = self.db.signIn(user)

        if logIn == True:
            self.parent.changeToMainWindow()
        else:
            self.message.setText('Correo y/o contraseña inválidos')