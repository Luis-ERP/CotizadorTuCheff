from PyQt5.QtWidgets import *


class InfoConfig(QGroupBox):
    def __init__(self):
        super(InfoConfig, self).__init__('Información Personal')
        self.setMaximumHeight(400)
        self.setMaximumWidth(500)

        ##declare layouts
        vLayout1 = QVBoxLayout()

        ##declare components
        label1 = QLabel('Dirección')
        label2 = QLabel('Teléfono móbil')
        label3 = QLabel('Teléfono fijo')
        label4 = QLabel('E-mail 1')
        label5 = QLabel('E-mail 2')
        label6 = QLabel('RFC')
        label7 = QLabel('Nombre moral/físico')

        self.address = QLineEdit()
        self.phone = QLineEdit()
        self.telephone = QLineEdit()
        self.email1 = QLineEdit()
        self.email2 = QLineEdit()
        self.rfc = QLineEdit()
        self.name = QLineEdit()
        self.btnSaveChanges = QPushButton('Guardar cambios')

        ##layout structure
        vLayout1.addWidget(label1)
        vLayout1.addWidget(self.address)
        vLayout1.addWidget(label2)
        vLayout1.addWidget(self.phone)
        vLayout1.addWidget(label3)
        vLayout1.addWidget(self.telephone)
        vLayout1.addWidget(label4)
        vLayout1.addWidget(self.email1)
        vLayout1.addWidget(label5)
        vLayout1.addWidget(self.email2)
        vLayout1.addWidget(label6)
        vLayout1.addWidget(self.rfc)
        vLayout1.addWidget(label7)
        vLayout1.addWidget(self.name)
        vLayout1.addWidget(self.btnSaveChanges)

        self.setLayout(vLayout1)