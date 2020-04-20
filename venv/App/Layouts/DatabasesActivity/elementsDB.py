from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class ElementsDB(QWidget):
    def __init__(self):
        super(ElementsDB, self).__init__()
        self.setMaximumWidth(750)

        ##declare layouts
        vLayout1 = QVBoxLayout()
        self.tLayout1 = QTableWidget(1, 6)

        ##declare components
        label1 = QLabel('Elementos')
        self.btnAddNewElement = QPushButton()

        ##components configuration
        self.tLayout1.setHorizontalHeaderLabels(['Nombre', 'Visible', 'Categorias', 'Precio', 'Modificar', 'Borrar'])
        self.tLayout1.setMinimumWidth(500)
        self.tLayout1.setColumnWidth(0, 125)
        self.tLayout1.setColumnWidth(1, 175)
        self.tLayout1.setColumnWidth(2, 250)
        self.tLayout1.setColumnWidth(3, 50)
        self.tLayout1.setColumnWidth(4, 50)
        self.tLayout1.setColumnWidth(4, 50)

        ##layout structure
        vLayout1.addWidget(label1)
        vLayout1.addWidget(self.btnAddNewElement)
        vLayout1.addWidget(self.tLayout1)
        self.setLayout(vLayout1)

class NewElementToDB(QWidget):
    def __init__(self):
        super(NewElementToDB, self).__init__()

        ##declare layouts
        vLayout1 = QVBoxLayout()
        hLayout1 = QHBoxLayout()
        hLayout2 = QHBoxLayout()
        hLayout3 = QHBoxLayout()
        self.vLayout2 = QVBoxLayout()
        wLayout1 = QWidget()
        scrollArea = QScrollArea()

        ##declare widgets
        label1 = QLabel('Nuevo elemento')
        label2 = QLabel('Nombre')
        label3 = QLabel('Precio')
        label4 = QLabel('Quitar')
        self.btnAddNewElement = QPushButton('Aceptar')
        self.btnAddCategory = QPushButton('Agregar categoría')
        self.elementName = QLineEdit()
        self.elementDescription = QLineEdit()

        ##layout structure
        hLayout1.addWidget(label1)
        hLayout1.addWidget(self.btnAddNewService)

        hLayout2.addWidget(self.elementName)
        hLayout2.addWidget(self.elementDescription)

        hLayout3.addWidget(label1)
        hLayout3.addWidget(label2)
        hLayout3.addWidget(label3)
        hLayout3.addWidget(label4)

        wLayout1.setLayout(self.vLayout2)
        scrollArea.setWidget(wLayout1)

        vLayout1.addLayout(hLayout1)
        vLayout1.addLayout(hLayout2)
        vLayout1.addWidget(self.btnAddElement)
        vLayout1.addLayout(hLayout3)
        vLayout1.addWidget(scrollArea)

        self.setLayout(vLayout1)