from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class ServicesDB(QWidget):
    def __init__(self):
        super(ServicesDB, self).__init__()
        self.setMaximumWidth(700)

        ##declare layouts
        vLayout1 = QVBoxLayout()
        self.tLayout1 = QTableWidget(1, 5)

        ##declare components
        label1 = QLabel('Servicios')
        self.btnAddNewService = QPushButton()

        ##components configuration
        self.tLayout1.setHorizontalHeaderLabels(['Nombre', 'Descripción', 'Lista de elementos', 'Modificar', 'Borrar'])
        self.tLayout1.setColumnWidth(0, 115)
        self.tLayout1.setColumnWidth(1, 200)
        self.tLayout1.setColumnWidth(2, 250)
        self.tLayout1.setColumnWidth(3, 50)
        self.tLayout1.setColumnWidth(4, 50)

        ##layout structure
        vLayout1.addWidget(label1)
        vLayout1.addWidget(self.btnAddNewService)
        vLayout1.addWidget(self.tLayout1)
        self.setLayout(vLayout1)


class NewServiceToDB(QDialog):
    def __init__(self):
        super(NewServiceToDB, self).__init__()

        ##declare layouts
        vLayout1 = QVBoxLayout()
        hLayout1 = QHBoxLayout()
        hLayout2 = QHBoxLayout()
        hLayout3 = QHBoxLayout()
        self.vLayout2 = QVBoxLayout()
        wLayout1 = QWidget()
        scrollArea = QScrollArea()

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

        ##layout structure
        hLayout1.addWidget(label1)
        hLayout1.addWidget(self.btnAddNewService)

        hLayout2.addWidget(self.serviceName)
        hLayout2.addWidget(self.serviceDescription)

        hLayout3.addWidget(label1)
        hLayout3.addWidget(label2)
        hLayout3.addWidget(label3)
        hLayout3.addWidget(label4)
        hLayout3.addWidget(label5)
        hLayout3.addWidget(label6)
        hLayout3.addWidget(label7)

        wLayout1.setLayout(self.vLayout2)
        scrollArea.setWidget(wLayout1)

        vLayout1.addLayout(hLayout1)
        vLayout1.addLayout(hLayout2)
        vLayout1.addWidget(self.btnAddElement)
        vLayout1.addLayout(hLayout3)
        vLayout1.addWidget(scrollArea)

        self.setLayout(vLayout1)