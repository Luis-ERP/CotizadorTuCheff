from Layouts.DatabasesActivity.databasesActivity import *
from Source.Databases.elementsDB import NewElementToDB
from Source.Databases.servicesDB import ServiceToDB
from Source.queryManager import QueryManager


class Databases(DatabasesActivity):
    def __init__(self):
        super().__init__()
        ##event handlers
        self.elements.btnAddNewElement.clicked.connect(self.createNewElementQDialog)
        self.services.btnAddNewService.clicked.connect(self.createNewServiceQDialog)
        self.elements.updateElementTable()
        self.services.updateServiceTable()

    def createNewElementQDialog(self):
        self.ElemWindow = NewElementToDB()
        self.ElemWindow.show()

    def createNewServiceQDialog(self):
        self.ServWindow = ServiceToDB()
        self.ServWindow.show()