from Layouts.AuthenticationActivity.registerUserActivity import RegisterUserActivity, SuccesfulRegisterActivity
from Database.user import User
from Source.queryManager import QueryManager

class RegisterUser(RegisterUserActivity):
    def __init__(self, parent):
        super(RegisterUser, self).__init__()
        self.parent = parent
        self.db = QueryManager()

        ##event handlers
        self.btnEnter.clicked.connect(self.addNewUser)
        self.btnLogIn.clicked.connect(self.parent.changeToLogInWindow)

    def addNewUser(self):
        email = self.email.text()
        emailConfir = self.emailConfirmation.text()
        password = self.password.text()
        passConfir = self.passConfirmation.text()
        name = self.name.text()
        phone = self.phone.text()

        newUser = User()
        newUser.name = name
        newUser.email = email
        newUser.password = password
        newUser.phone = phone
        response = self.db.createNewUser(newUser, emailConfir, passConfir)
        if not (response == True):
            self.message.setText(response)
        else:
            self.parent.changeToSuccesWindow()
            self.clearAllFields()

    def clearAllFields(self):
        self.email.setText('')
        self.emailConfirmation.setText('')
        self.password.setText('')
        self.passConfirmation.setText('')
        self.name.setText('')
        self.phone.setText('')



class SuccesfulRegister(SuccesfulRegisterActivity):
    def __init__(self, parent):
        super(SuccesfulRegister, self).__init__()

        ##events handler
        self.btnEnter.clicked.connect(parent.changeToMainWindow)

