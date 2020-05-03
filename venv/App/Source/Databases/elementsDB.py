from Layouts.DatabasesActivity.elementsDB import ElementsDBActivity, ElementToDB, Category
from Database import element
from Source.queryManager import QueryManager

from uuid import uuid4
from PyQt5.QtWidgets import QLabel, QPushButton, QComboBox, QMessageBox


class ElementsDB(ElementsDBActivity):
    def __init__(self):
        super(ElementsDB, self).__init__()
        self.dbManager = QueryManager()
        ##storage variables
        self.allRows = []

    def updateElementTable(self):
        self.allCategories = []
        self.tLayout1.clear()
        self.tLayout1.setRowCount(0)
        elementsObj = self.dbManager.getAllElements()
        for elem in elementsObj:
            self.addElementRowToTable(elem)
            self.allCategories.append(elem.categories)

    def addElementRowToTable(self, elem):
        self.row = ElemTableRow(self, elem)
        ##add to element table
        rowPosition = self.tLayout1.rowCount()
        self.tLayout1.insertRow(rowPosition)
        self.tLayout1.setCellWidget(rowPosition, 0, self.row.nameLabel)
        self.tLayout1.setCellWidget(rowPosition, 1, self.row.categoriesCombo)
        self.tLayout1.setCellWidget(rowPosition, 2, self.row.priceLabel)
        self.tLayout1.setCellWidget(rowPosition, 3, self.row.btnEdit)
        self.tLayout1.setCellWidget(rowPosition, 4, self.row.btnDelete)
        self.allRows.append(self.row)


class ElemTableRow:
    def __init__(self, parent, element):
        self.dbManager = QueryManager()
        self.element = element
        self.allCategories = element.categories
        self.id = element.id
        self.parent = parent

        ##declare components
        self.nameLabel = QLabel(element.name)
        self.categoriesCombo = QComboBox()
        self.priceLabel = QLabel('precio')
        self.btnEdit = QPushButton('Editar')
        self.btnDelete = QPushButton('Borrar')

        ##event handler
        self.btnDelete.clicked.connect(self.warningMessageDisplay)

        ##add categories to combobox
        for itemDict in self.allCategories:
            self.categoriesCombo.addItem(itemDict['name'])

        ##event handlers
        self.updateComponentsElementTable()
        self.categoriesCombo.currentIndexChanged.connect(self.updateComponentsElementTable)
        self.btnEdit.clicked.connect(self.editElementDialog)

    def updateComponentsElementTable(self):
        price = self.allCategories[self.categoriesCombo.currentIndex()]['price']
        self.priceLabel.setText('$ %.2f' %(price))

    def warningMessageDisplay(self):
        msg = QMessageBox()
        msg.setText('Eliminar Elemento')
        msg.setInformativeText('¿Estás seguro de eliminar el elemento? Esta acción NO es reversible')
        msg.setWindowTitle('Aviso')
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.delete)
        retval = msg.exec_()

    def delete(self, i):
        if i.text() != 'OK':
            return
        elemIndex = None
        allElements = self.dbManager.getAllElements()
        for i in range(len(allElements)):
            if self.id == allElements[i].id:
                elemIndex = i
                break
        self.dbManager.deleteElementInServices(self.id, elemIndex)
        self.dbManager.deleteElement(self.id)
        self.parent.updateElementTable()

    def editElementDialog(self):
        self.window = NewElementToDB()
        self.window.elementName.setText(self.element.name)
        self.window.elementDescription.setText(self.element.description)
        for i, category in enumerate(self.allCategories):
            self.window.addCategory()
            self.window.vLayout2.itemAt(i).widget().name.setText(category['name'])
            self.window.vLayout2.itemAt(i).widget().price.setValue(category['price'])
        self.window.show()


class NewElementToDB(ElementToDB):
    def __init__(self):
        super(NewElementToDB, self).__init__()
        self.dbManager = QueryManager()

        ##event handlers
        self.btnAddCategory.clicked.connect(self.addCategory)
        self.btnAddNewElement.clicked.connect(self.saveElementToDB)

    def addCategory(self):
        self.newCategory = NewCategory(self)
        self.vLayout2.addWidget(self.newCategory)

    def removeCategory(self):
        for i in range(self.vLayout2.count()):
            widget = self.vLayout2.itemAt(i)
            if not widget.widget().isEnabled():
                self.vLayout2.removeWidget(widget.widget())
                break

    def saveElementToDB(self):
        categories = []
        for i in range(self.vLayout2.count()):
            cat = self.vLayout2.itemAt(i).widget()
            categories.append(cat.getInfo())

        newElement = element.Element(name=self.elementName.text(), description=self.elementDescription.text(), categories=categories)
        self.dbManager.addNewElement(newElement)
        self.close()


class NewCategory(Category):
    def __init__(self, parent):
        super(NewCategory, self).__init__()
        self.id = str(uuid4())
        self.parent = parent

        ##event handlers
        self.btnDelete.clicked.connect(self.destroy)

    def destroy(self):
        self.setEnabled(False)
        self.setVisible(False)
        self.parent.removeCategory()

    def getInfo(self):
        return {'name': self.name.text(), 'price': self.price.value(), 'id': self.id}