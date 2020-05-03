from Layouts.QuoteActivity.getNewService import GetNewService
from Source.Quote.newElement import NewElement
from Source.queryManager import QueryManager

from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class NewService(GetNewService):
    def __init__(self, parent):
        super(NewService, self).__init__(parent)
        self.dbManager = QueryManager()
        self.services = [] #list of service objects

        self.fillServicesComboBox()
        self.getServiceTemplate()
        ##events handler
        self.btnAddElement.clicked.connect(self.addNewElement)
        self.checkXPerson.stateChanged.connect(self.enabledNuGuests)
        self.checkXHour.stateChanged.connect(self.enabledNuHours)
        self.serviceTemplates.currentIndexChanged.connect(self.getServiceTemplate)


    def enabledNuGuests(self, state):
        if state == QtCore.Qt.Checked:
            self.nuGuests.setEnabled(True)
        else:
            self.nuGuests.setEnabled(False)

    def enabledNuHours(self, state):
        if state == QtCore.Qt.Checked:
            self.nuHours.setEnabled(True)
        else:
            self.nuHours.setEnabled(False)

    def fillServicesComboBox(self):
        self.services = self.dbManager.getAllServices()
        for service in self.services:
            self.serviceTemplates.addItem(service.name)

    def getServiceTemplate(self):
        while not self.vLayout3.isEmpty():
            self.vLayout3.removeWidget(self.vLayout3.itemAt(0).widget())
        currentService = self.services[self.serviceTemplates.currentIndex()]
        self.serviceName.setText(currentService.name)
        elementsInService = []
        for i in currentService.elements:
            elem = self.dbManager.getElementById(i['Id'])
            elementsInService.append(elem)
        for i, element in enumerate(elementsInService) :
            elemName = element.name
            comments = element.comments
            elemVisible = currentService.elements[i]['Visible']
            categories = element.categories
            defaultCat = currentService.elements[i]['DefaultCategoryId']
            self.addNewElement(personalized=True,
                               name=elemName,
                               visibility=elemVisible,
                               categoriesDict=categories,
                               defaultCatId=defaultCat,
                               comments=comments)


    def addNewElement(self, personalized=False, name='', visibility=True, categoriesDict=[], defaultCatId='', comments=''):
        widget = NewElement(self)
        if personalized:
            widget.nameStr = name
            widget.commentsStr = comments
            widget.setVisibility(visibility)
            widget.categories = categoriesDict
            widget.currentCategoryId = defaultCatId
            widget.setCategoriesToComboBox()
            widget.fillWithCategoryInfo()
        self.vLayout3.addWidget(widget)