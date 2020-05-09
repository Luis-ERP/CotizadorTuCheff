from PyQt5.QtWidgets import *

class LogInActivity(QWidget):
    def __init__(self):
        super(LogInActivity, self).__init__()
        self.setMaximumSize(300, 250)

        ##declare layouts
        vLayout1 = QVBoxLayout()

        # declare components
        title = QLabel('Verificación de usuario')
        label1 = QLabel('Correo electrónico')
        label2 = QLabel('Contraseña')
        self.email = QLineEdit()
        self.password = QLineEdit()
        self.btnNewUser = QPushButton('Registarme')
        self.btnEnter = QPushButton('Entrar')
        self.message = QLabel()

        ##components configurations
        self.password.setEchoMode(QLineEdit.Password)
        self.email.setPlaceholderText('e-mail')
        self.password.setPlaceholderText('password')
        title.setStyleSheet('QLabel { font-size: 25px; color: #800000; }')
        self.message.setStyleSheet('QLabel { color: red; }')
        self.btnNewUser.setMaximumWidth(60)
        self.btnNewUser.setStyleSheet(
            'QPushButton {color: #2318ff; background-color: Transparent;}  QPushButton:Hover { color: #5bc7ff }')

        ##set layout structure
        vLayout1.addWidget(title)
        vLayout1.addWidget(self.message)
        vLayout1.addWidget(label1)
        vLayout1.addWidget(self.email)
        vLayout1.addWidget(label2)
        vLayout1.addWidget(self.password)
        vLayout1.addWidget(self.btnNewUser)
        vLayout1.addWidget(self.btnEnter)

        self.setLayout(vLayout1)