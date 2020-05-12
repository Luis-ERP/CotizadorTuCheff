from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class ElementsDBActivity(QWidget):
    def __init__(self):
        super(ElementsDBActivity, self).__init__()
        self.setMaximumWidth(750)

        ##declare layouts
        vLayout1 = QVBoxLayout()
        self.tLayout1 = QTableWidget(0, 5)

        ##declare components
        label1 = QLabel('Elementos')
        self.btnAddNewElement = QPushButton('Agregar elemento')

        ##components configuration
        self.btnAddNewElement.setMaximumWidth(100)
        self.tLayout1.setHorizontalHeaderLabels(['Nombre', 'Categorias', 'Precio', 'Modificar', 'Borrar'])
        header = self.tLayout1.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)

        ##layout structure
        vLayout1.addWidget(label1)
        vLayout1.addWidget(self.btnAddNewElement)
        vLayout1.addWidget(self.tLayout1)
        self.setLayout(vLayout1)


class ElementToDB(QDialog):
    def __init__(self):
        super(ElementToDB, self).__init__()
        self.setFixedWidth(400)

        ##declare layouts
        vLayout1 = QVBoxLayout()
        hLayout1 = QHBoxLayout()
        hLayout2 = QHBoxLayout()
        hLayout3 = QHBoxLayout()
        self.vLayout2 = QVBoxLayout()

        ##declare widgets
        label1 = QLabel('Nuevo elemento')
        label2 = QLabel('Nombre')
        label3 = QLabel('Precio')
        label4 = QLabel('Quitar')
        self.btnAddNewElement = QPushButton('Aceptar')
        self.btnAddCategory = QPushButton('Agregar categoría')
        self.elementName = QLineEdit()
        self.elementDescription = QLineEdit()

        ##components configuration
        self.elementName.setPlaceholderText('Nombre')
        self.elementDescription.setPlaceholderText('Descripción')

        ##layout structure
        hLayout1.addWidget(label1)
        hLayout1.addWidget(self.btnAddNewElement)

        hLayout2.addWidget(self.elementName)
        hLayout2.addWidget(self.elementDescription)

        hLayout3.addWidget(label2)
        hLayout3.addWidget(label3)
        hLayout3.addWidget(label4)

        vLayout1.addLayout(hLayout1)
        vLayout1.addLayout(hLayout2)
        vLayout1.addWidget(self.btnAddCategory)
        vLayout1.addLayout(hLayout3)
        vLayout1.addLayout(self.vLayout2)

        self.setLayout(vLayout1)


class Category(QWidget):
    def __init__(self):
        super(Category, self).__init__()
        ##declare layouts
        hLayout1 = QHBoxLayout()

        ##declare components
        self.name = QLineEdit()
        self.price = QDoubleSpinBox()
        self.btnDelete = QPushButton()

        ##components configuration
        self.name.setPlaceholderText('Nombre del atributo')
        self.price.setFixedWidth(70)
        self.btnDelete.setIcon(QtGui.QIcon('Res/Icons/remove1.png'))

        ##set layout structure
        hLayout1.addWidget(self.name)
        hLayout1.addWidget(self.price)
        hLayout1.addWidget(self.btnDelete)

        self.setLayout(hLayout1)
