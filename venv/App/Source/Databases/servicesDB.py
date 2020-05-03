from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel, QComboBox, QPushButton, QMessageBox

from Layouts.DatabasesActivity.servicesDB import NewServiceToDB, ElementLayout, ServicesDBActivity
from Source.queryManager import QueryManager
from Database import element, service


class ServicesDB(ServicesDBActivity):
    def __init__(self):
        super(ServicesDB, self).__init__()
        self.dbManager = QueryManager()
        ##storage variables
        self.allRows = []
        
    def updateServiceTable(self):
        self.allElements = []
        self.tLayout1.clear()
        self.tLayout1.setRowCount(0)
        serviceObj = self.dbManager.getAllServices()
        for serv in serviceObj:
            self.addServiceRowToTable(serv)
            self.allElements.append(serv.elements)
            
    def addServiceRowToTable(self, serv):
        self.row = ServTableRow(self, serv)
        ##add to service table
        rowPosition = self.tLayout1.rowCount()
        self.tLayout1.insertRow(rowPosition)
        self.tLayout1.setCellWidget(rowPosition, 0, self.row.nameLabel)
        self.tLayout1.setCellWidget(rowPosition, 1, self.row.descriptionLabel)
        self.tLayout1.setCellWidget(rowPosition, 2, self.row.elementsList)
        self.tLayout1.setCellWidget(rowPosition, 3, self.row.btnEdit)
        self.tLayout1.setCellWidget(rowPosition, 4, self.row.btnDelete)
        self.allRows.append(self.row)


class ServTableRow:
    def __init__(self, parent, service):
        self.dbManager = QueryManager()
        self.service = service
        self.allElements = service.elements
        self.id = service.id
        self.parent = parent

        ##declare components
        self.nameLabel = QLabel(service.name)
        self.descriptionLabel = QLabel(service.description)
        self.elementsList = QComboBox()
        self.btnEdit = QPushButton('Editar')
        self.btnDelete = QPushButton('Borrar')

        ##event handler
        self.btnDelete.clicked.connect(self.warningMessageDisplay)

        ##add elements to combobox
        for itemDict in self.allElements:
            try:
                element = self.dbManager.getElementById(itemDict['Id'])
                self.elementsList.addItem(element.name)
            except:
                pass

        ##event handlers
        self.btnEdit.clicked.connect(self.editServiceDialog)

    def warningMessageDisplay(self):
        msg = QMessageBox()
        msg.setText('Eliminar Servicio')
        msg.setInformativeText('¿Estás seguro de eliminar el servicio? Esta acción NO es reversible')
        msg.setWindowTitle('Aviso')
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.delete)
        retval = msg.exec_()

    def delete(self, i):
        if i.text() != 'OK':
            return
        self.dbManager.deleteService(self.id)
        self.parent.updateServiceTable()

    def editServiceDialog(self):
        self.window = ServiceToDB()
        self.window.serviceName.setText(self.service.name)
        self.window.serviceDescription.setText(self.service.description)
        for i, elemDict in enumerate(self.allElements):
            element = self.dbManager.getElementById(elemDict['Id'])
            self.window.addElement()
            elemIndex = self.window.vLayout2.itemAt(i).widget().name.findText(element.name)
            self.window.vLayout2.itemAt(i).widget().name.setCurrentIndex(elemIndex)
            if not elemDict['Visible']:
                self.window.vLayout2.itemAt(i).widget().setVisibility()
            category = None
            for cat in element.categories:
                if cat['id'] == elemDict['DefaultCategoryId']:
                    category = cat
            catIndex = self.window.vLayout2.itemAt(i).widget().category.findText(category['name'])
            self.window.vLayout2.itemAt(i).widget().category.setCurrentIndex(catIndex)
        self.window.show()


class ServiceToDB(NewServiceToDB):
    def __init__(self):
        super(ServiceToDB, self).__init__()
        self.dbManager = QueryManager()

        ##event handlers
        self.btnAddElement.clicked.connect(self.addElement)
        self.btnAddNewService.clicked.connect(self.saveServiceToDB)

    def addElement(self):
        newElement = Element(self)
        self.vLayout2.addWidget(newElement)

    def removeElement(self):
        for i in range(self.vLayout2.count()):
            widget = self.vLayout2.itemAt(i)
            if not widget.widget().isEnabled():
                self.vLayout2.removeWidget(widget.widget())
                break

    def saveServiceToDB(self):
        elementsList = []
        for i in range(self.vLayout2.count()):
            elem = self.vLayout2.itemAt(i).widget()
            elementsList.append(elem.getInfo())
        newService = service.Service(name=self.serviceName.text(), description=self.serviceDescription.text(), elements=elementsList)
        self.dbManager.addNewService(newService)
        self.close()


class Element(ElementLayout):
    def __init__(self, parent):
        super(Element, self).__init__()

        ##storage variables
        self.isVisible = True
        self.dbManager = QueryManager()
        self.parent = parent

        ##fill comboBoxes
        self.usedElemIds = []
        self.usedCategories = []

        allElements = self.dbManager.getAllElements()
        for elem in range(len(allElements)):
            self.name.addItem(allElements[elem].name)
            self.usedElemIds.append(allElements[elem])

        ##event handlers
        self.elemNameIndexChaged()
        self.displayCategories()
        self.name.currentIndexChanged.connect(self.elemNameIndexChaged)
        self.category.currentIndexChanged.connect(self.displayCategories)
        self.btnVisible.clicked.connect(self.setVisibility)
        self.btnDelete.clicked.connect(self.destroy)

    def destroy(self):
        self.setEnabled(False)
        self.setVisible(False)
        self.parent.removeElement()

    def elemNameIndexChaged(self):
        self.currentSelectedCat = None
        currentSelectedElem = self.usedElemIds[self.name.currentIndex()]
        #fill labels
        self.descriptionLabel.setText(currentSelectedElem.description)
        #fill categories
        categoriesList = currentSelectedElem.categories
        self.category.clear()
        self.usedCategories = []
        for i, catDict in enumerate(categoriesList):
            if i == 0:
                self.currentSelectedCat = catDict
            self.category.addItem(catDict['name'])
            self.usedCategories.append([catDict])

    def displayCategories(self):
        categoriesList = self.usedElemIds[self.name.currentIndex()].categories
        self.currentSelectedCat = categoriesList[self.category.currentIndex()]
        for item in categoriesList:
            if item['name'] == self.category.currentText():
                self.priceLabel.setText('$ %.2f' %(item['price']))

    def setVisibility(self):
        self.isVisible = not self.isVisible
        if self.isVisible:
            self.btnVisible.setIcon(QtGui.QIcon('Res/Icons/visibleOn.png'))
        else:
            self.btnVisible.setIcon(QtGui.QIcon('Res/Icons/visibleOff.png'))

    def getInfo(self):
        obj = element.Element(id=self.usedElemIds[self.name.currentIndex()].id, visibility=self.isVisible, defaultCatId=self.currentSelectedCat['id'])
        info = obj.getElementReference()
        return info