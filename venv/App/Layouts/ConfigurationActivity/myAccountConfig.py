from PyQt5.QtWidgets import *


class MyAccountConfig(QGroupBox):
    def __init__(self):
        super(MyAccountConfig, self).__init__('Mi cuenta')
        self.setMaximumWidth(400)
        self.setMaximumHeight(120)

        ##declare layout
        fLayout1 = QFormLayout()

        ##declare components
        label1 = QLabel('Nombre')
        label2 = QLabel('E-mail')
        label3 = QLabel('Teléfono')
        self.nameLabel = QLabel()
        self.emailLabel = QLabel()
        self.phoneLabel = QLabel()
        self.btnEditInfo = QPushButton('Editar')

        ##layout structure
        fLayout1.addRow(label1, self.nameLabel)
        fLayout1.addRow(label2, self.emailLabel)
        fLayout1.addRow(label3, self.phoneLabel)
        fLayout1.addRow(self.btnEditInfo)

        self.setLayout(fLayout1)


class EditInfo(QDialog):
    def __init__(self):
        super(EditInfo, self).__init__()

        ##declare layout
        fLayout1 = QFormLayout()

        ##declare components
        label1 = QLabel('Nombre completo:')
        label2 = QLabel('Teléfono')
        label3 = QLabel('Contraseña anterior:')
        label4 = QLabel('Contraseña nueva:')
        self.name = QLineEdit()
        self.phone = QLineEdit()
        self.oldPassword = QLineEdit()
        self.newPassword = QLineEdit()
        self.btnSaveChanges = QPushButton()

        ##layout structure
        fLayout1.addRow(label1, self.name)
        fLayout1.addRow(label2, self.phone)
        fLayout1.addRow(label3, self.oldPassword)
        fLayout1.addRow(label4, self.newPassword)
        fLayout1.addRow(self.btnSaveChanges)

        self.setLayout(fLayout1)