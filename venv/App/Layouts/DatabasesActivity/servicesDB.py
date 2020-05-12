from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class ServicesDBActivity(QWidget):
    def __init__(self):
        super(ServicesDBActivity, self).__init__()
        self.setMaximumWidth(700)

        ##declare layouts
        vLayout1 = QVBoxLayout()
        self.tLayout1 = QTableWidget(0, 5)

        ##declare components
        label1 = QLabel('Servicios')
        self.btnAddNewService = QPushButton('Agregar servicio')

        ##components configuration
        self.btnAddNewService.setMaximumWidth(100)
        self.tLayout1.setHorizontalHeaderLabels(['Nombre', 'Descripción', 'Lista de elementos', 'Modificar', 'Borrar'])
        header = self.tLayout1.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)

        ##layout structure
        vLayout1.addWidget(label1)
        vLayout1.addWidget(self.btnAddNewService)
        vLayout1.addWidget(self.tLayout1)
        self.setLayout(vLayout1)


class NewServiceToDB(QDialog):
    def __init__(self):
        super(NewServiceToDB, self).__init__()
        self.setFixedWidth(500)

        ##declare layouts
        vLayout1 = QVBoxLayout()
        hLayout1 = QHBoxLayout()
        hLayout2 = QHBoxLayout()
        hLayout3 = QHBoxLayout()
        self.vLayout2 = QVBoxLayout()

        ##declare widgets
        label1 = QLabel('Nuevo servicio')
        label2 = QLabel('Nombre')
        label3 = QLabel('Visible')
        label4 = QLabel('Categoría')
        label5 = QLabel('Precio')
        label6 = QLabel('Descripción')
        label7 = QLabel('Quitar')
        self.btnAddNewService = QPushButton('Aceptar')
        self.btnAddElement = QPushButton('Agregar elemento')
        self.serviceName = QLineEdit()
        self.serviceDescription = QLineEdit()

        ##components comfiguration
        self.serviceName.setPlaceholderText('Nombre')
        self.serviceDescription.setPlaceholderText('Descripción')

        ##layout structure
        hLayout1.addWidget(label1)
        hLayout1.addWidget(self.btnAddNewService)

        hLayout2.addWidget(self.serviceName)
        hLayout2.addWidget(self.serviceDescription)

        hLayout3.addWidget(label2)
        hLayout3.addWidget(label3)
        hLayout3.addWidget(label4)
        hLayout3.addWidget(label5)
        hLayout3.addWidget(label6)
        hLayout3.addWidget(label7)

        vLayout1.addLayout(hLayout1)
        vLayout1.addLayout(hLayout2)
        vLayout1.addWidget(self.btnAddElement)
        vLayout1.addLayout(hLayout3)
        vLayout1.addLayout(self.vLayout2)

        self.setLayout(vLayout1)


class ElementLayout(QWidget):
    def __init__(self):
        super(ElementLayout, self).__init__()

        ##declare layouts
        hLayout1 = QHBoxLayout()

        ##declare components
        self.name = QComboBox()
        self.btnVisible = QPushButton()
        self.category = QComboBox()
        self.priceLabel = QLabel()
        self.descriptionLabel = QLabel()
        self.btnDelete = QPushButton()

        ##components configuration
        self.btnVisible.setIcon(QtGui.QIcon('Res/Icons/visibleOn.png'))
        self.btnVisible.setMaximumWidth(30)
        self.btnDelete.setIcon(QtGui.QIcon('Res/Icons/remove1.png'))
        self.btnDelete.setMaximumWidth(30)

        ##set layout structure
        hLayout1.addWidget(self.name)
        hLayout1.addWidget(self.btnVisible)
        hLayout1.addWidget(self.category)
        hLayout1.addWidget(self.priceLabel)
        hLayout1.addWidget(self.descriptionLabel)
        hLayout1.addWidget(self.btnDelete)

        self.setLayout(hLayout1)