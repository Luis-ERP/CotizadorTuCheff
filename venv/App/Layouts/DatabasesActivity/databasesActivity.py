from PyQt5.QtWidgets import *
from Layouts.DatabasesActivity.servicesDB import ServicesDB
from Layouts.DatabasesActivity.elementsDB import ElementsDB


class DatabasesActivity(QWidget):
    def __init__(self):
        super().__init__()

        ##declare layouts
        hLayout1 = QHBoxLayout()

        ##declare components
        services = ServicesDB()
        elements = ElementsDB()

        ##layout structure
        hLayout1.addWidget(services)
        hLayout1.addWidget(elements)

        self.setLayout(hLayout1)
