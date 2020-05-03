from PyQt5.QtWidgets import *
from Source.Databases.servicesDB import ServicesDB
from Source.Databases.elementsDB import ElementsDB


class DatabasesActivity(QWidget):
    def __init__(self):
        super().__init__()

        ##declare layouts
        hLayout1 = QHBoxLayout()

        ##declare components
        self.services = ServicesDB()
        self.elements = ElementsDB()

        ##layout structure
        hLayout1.addWidget(self.services)
        hLayout1.addWidget(self.elements)

        self.setLayout(hLayout1)