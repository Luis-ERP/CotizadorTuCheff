from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from Source.Configuration.quote import Quote
from Source.Configuration.factura import Factura
from Source.Configuration.users import Users
from Source.Configuration.myAccount import MyAccount
from Source.Configuration.info import Info
from Source.Configuration.firebase import Firebase

class ConfigurationActivity(QWidget):
    def __init__(self):
        super().__init__()

        ##declare layout
        hLayout1 = QHBoxLayout()
        vLayout1 = QVBoxLayout()
        vLayout2 = QVBoxLayout()

        ##declare components
        label1 = QLabel('Configuración')
        self.quote = Quote()
        self.factura = Factura()
        self.users = Users()
        self.myAccount = MyAccount()
        self.info = Info()
        self.firebase = Firebase()

        ##configuration components
        vLayout1.setAlignment(QtCore.Qt.AlignTop)
        vLayout2.setAlignment(QtCore.Qt.AlignTop)

        ##layout structure
        vLayout2.addWidget(self.info)
        vLayout2.addWidget(self.firebase)

        vLayout1.addWidget(self.myAccount)
        vLayout1.addWidget(self.quote)

        hLayout1.addLayout(vLayout1)
        hLayout1.addLayout(vLayout2)
        hLayout1.addWidget(self.users)

        self.setLayout(hLayout1)