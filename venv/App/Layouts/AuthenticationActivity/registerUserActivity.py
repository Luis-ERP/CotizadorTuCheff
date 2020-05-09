from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class RegisterUserActivity(QWidget):
    def __init__(self):
        super(RegisterUserActivity, self).__init__()

        ##declare layouts
        vLayout1 = QVBoxLayout()

        ##declare components
        title = QLabel('Resistro de usuario')
        label1 = QLabel('Nombre completo')
        label2 = QLabel('Correo electrónico')
        label3 = QLabel('Confirmación de correo')
        label4 = QLabel('Contraseña')
        label5 = QLabel('Confirmación de contraseña')
        label6 = QLabel('Número de celular (10 dígitos)')
        self.name = QLineEdit()
        self.email = QLineEdit()
        self.emailConfirmation = QLineEdit()
        self.password = QLineEdit()
        self.passConfirmation = QLineEdit()
        self.phone = QLineEdit()
        self.btnLogIn = QPushButton('Ya tengo cuenta')
        self.btnEnter = QPushButton('Registrarme')
        self.message = QLabel()

        ##components configuration
        self.password.setEchoMode(QLineEdit.Password)
        self.passConfirmation.setEchoMode(QLineEdit.Password)
        self.email.setPlaceholderText('e-mail')
        self.password.setPlaceholderText('password')
        title.setStyleSheet('QLabel { font-size: 25px; Color: #800000 }')
        self.message.setStyleSheet('QLabel { color: red; }')
        self.btnLogIn.setMaximumWidth(85)
        self.btnLogIn.setStyleSheet(
            'QPushButton {color: #2318ff; background-color: Transparent;}  QPushButton:Hover { color: #5bc7ff }')

        ## ---------------------------------------------------------------- delete after debugging
        self.password.setText('1234567')
        self.passConfirmation.setText('1234567')
        self.emailConfirmation.setText('a01702056@itesm.mx')
        self.email.setText('a01702056@itesm.mx')

        ##set layout structure
        vLayout1.addWidget(title)
        vLayout1.addWidget(self.message)
        vLayout1.addWidget(label1)
        vLayout1.addWidget(self.name)
        vLayout1.addWidget(label2)
        vLayout1.addWidget(self.email)
        vLayout1.addWidget(label3)
        vLayout1.addWidget(self.emailConfirmation)
        vLayout1.addWidget(label4)
        vLayout1.addWidget(self.password)
        vLayout1.addWidget(label5)
        vLayout1.addWidget(self.passConfirmation)
        vLayout1.addWidget(label6)
        vLayout1.addWidget(self.phone)
        vLayout1.addWidget(self.btnLogIn)
        vLayout1.addWidget(self.btnEnter)

        self.setLayout(vLayout1)

class SuccesfulRegisterActivity(QWidget):
    def __init__(self):
        super(SuccesfulRegisterActivity, self).__init__()

        ##declare layout
        vLayout1 = QVBoxLayout()

        ##declate components
        label1 = QLabel('Registro hecho correctamente')
        label2 = QLabel('Espera a que uno de los administradores verifique tus datos')
        label3 = QLabel('Por lo mientras, tendrás accesso como invitado')
        self.btnEnter = QPushButton('Aceptar')

        ##components configuration
        label1.setStyleSheet('QLabel { font-size: 25px; color: #800000; margin-bottom: 20px; }')
        label2.setStyleSheet('QLabel { font-size: 12px; }')
        label3.setStyleSheet('QLabel { font-size: 12px; margin-bottom: 20px; }')
        vLayout1.setAlignment(QtCore.Qt.AlignTop)

        ##set layout structure
        vLayout1.addWidget(label1)
        vLayout1.addWidget(label2)
        vLayout1.addWidget(label3)
        vLayout1.addWidget(self.btnEnter)

        self.setLayout(vLayout1)
