from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore

class GetNewService(QGroupBox):
    def __init__(self, parent):
        super(GetNewService, self).__init__('Servicio')
        self.parent = parent

        ##declare layouts
        vLayout1 = QVBoxLayout()
        hLayout1 = QHBoxLayout()
        hLayout2 = QHBoxLayout()
        hLayout3 = QHBoxLayout()
        vLayout2 = QVBoxLayout()
        tLayout1 = QGridLayout()
        self.vLayout3 = QVBoxLayout()

        ##declare components
        label1 = QLabel('persona(s)')
        label2 = QLabel('hora(s)')
        label3 = QLabel('Cantidad')
        label4 = QLabel('Visible')
        label5 = QLabel('Nombre')
        label6 = QLabel('Categoría')
        label7 = QLabel('Precio X cant.')
        label8 = QLabel('Descripción')
        label9 = QLabel('Quitar')
        self.serviceName = QLineEdit()
        self.checkXPerson = QCheckBox('Servicio por')
        self.checkXHour = QCheckBox('Servicio por')
        self.nuGuests = QSpinBox()
        self.nuHours = QSpinBox()
        self.serviceTemplates = QComboBox()
        self.btnAddElement = QPushButton('Agregar elemento')
        self.btnCloseService = QPushButton()

        ##components configuration
        self.btnCloseService.setIcon(QtGui.QIcon('Res/Icons/remove1.png'))
        self.serviceName.setPlaceholderText('Nombre de servicio')
        self.nuGuests.setMinimum(1)
        self.nuGuests.setMaximum(999999)
        self.nuGuests.setMaximumWidth(40)
        self.nuGuests.setEnabled(False)
        self.nuHours.setMinimum(1)
        self.nuHours.setMaximum(999999)
        self.nuHours.setMaximumWidth(40)
        self.nuHours.setEnabled(False)
        hLayout3.setAlignment(QtCore.Qt.AlignLeft)
        #                         l  u  r  b
        label3.setContentsMargins(0,0,0,0)  #quantity
        label4.setContentsMargins(0,0,60,0) #visible
        label5.setContentsMargins(0,0,75,0) #name
        label6.setContentsMargins(0,0,15,0) #category
        label7.setContentsMargins(0,0,20,0) #price
        label8.setContentsMargins(0,0,20,0) #comments
        label9.setContentsMargins(0,0,0,0)  #btn close

        ##layout structure
        hLayout2.addWidget(self.serviceTemplates)
        hLayout2.addWidget(self.btnAddElement)

        vLayout2.addWidget(self.serviceName)
        vLayout2.addLayout(hLayout2)

        hLayout3.addWidget(label3)
        hLayout3.addWidget(label4)
        hLayout3.addWidget(label5)
        hLayout3.addWidget(label6)
        hLayout3.addWidget(label7)
        hLayout3.addWidget(label8)
        hLayout3.addWidget(label9)

        tLayout1.addWidget(self.checkXPerson, 1, 1)
        tLayout1.addWidget(self.nuGuests, 1, 2)
        tLayout1.addWidget(label1, 1, 3)
        tLayout1.addWidget(self.checkXHour, 2, 1)
        tLayout1.addWidget(self.nuHours, 2, 2)
        tLayout1.addWidget(label2, 2, 3)

        hLayout1.addLayout(vLayout2)
        hLayout1.addLayout(tLayout1)
        hLayout1.addWidget(self.btnCloseService)

        vLayout1.addLayout(hLayout1)
        vLayout1.addLayout(hLayout3)
        vLayout1.addLayout(self.vLayout3)

        self.setLayout(vLayout1)

