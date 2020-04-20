from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from Layouts.ConfigurationActivity.quoteConfig import QuoteConfig
from Layouts.ConfigurationActivity.facturaConfig import FacturaConfig
from Layouts.ConfigurationActivity.usersConfig import UsersConfig
from Layouts.ConfigurationActivity.myAccountConfig import MyAccountConfig
from Layouts.ConfigurationActivity.infoConfig import InfoConfig

class ConfigurationActivity(QWidget):
    def __init__(self):
        super().__init__()

        ##declare layout
        hLayout1 = QHBoxLayout()
        vLayout1 = QVBoxLayout()

        ##declare components
        label1 = QLabel('Configuración')

        self.quote = QuoteConfig()
        self.factura = FacturaConfig()
        self.users = UsersConfig()
        self.myAccount = MyAccountConfig()
        self.info = InfoConfig()

        ##layout structure
        vLayout1.addWidget(self.myAccount)
        vLayout1.addWidget(self.quote)

        hLayout1.addLayout(vLayout1)
        hLayout1.addWidget(self.info)
        hLayout1.addWidget(self.users)

        self.setLayout(hLayout1)