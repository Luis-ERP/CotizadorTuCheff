from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

class ClientSegment(QGroupBox):
    def __init__(self):
        super(ClientSegment, self).__init__('Cliente')
        ##self configuration
        self.setMaximumHeight(200)
        self.setMaximumWidth(300)

        ##declare layouts
        self.fLayout1 = QFormLayout()

        ##declare component
        label1 = QLabel('Nombre:')
        label2 = QLabel('Apellido:')
        label3 = QLabel('Tipo de cliente*:')
        label4 = QLabel('E-mail:')
        label5 = QLabel('Teléfono:')
        label6 = QLabel('Empresa:')
        label7 = QLabel('RFC:')
        self.nameClient = QLineEdit()
        self.lastNameClient = QLineEdit()
        self.clientType = QComboBox()
        self.email = QLineEdit()
        self.phone = QLineEdit()
        self.enterprise = QLineEdit()
        self.rfc = QLineEdit()

        ##layout structure
        self.fLayout1.addRow(label1, self.nameClient)
        self.fLayout1.addRow(label2, self.lastNameClient)
        self.fLayout1.addRow(label6, self.enterprise)
        self.fLayout1.addRow(label7, self.rfc)
        self.fLayout1.addRow(label4, self.email)
        self.fLayout1.addRow(label5, self.phone)
        self.fLayout1.addRow(label3, self.clientType)

        self.setLayout(self.fLayout1)


class EventSegment(QGroupBox):
    def __init__(self):
        super(EventSegment, self).__init__('Evento')
        ##self configuration
        self.setMaximumHeight(200)
        self.setMaximumWidth(350)

        ##declare layouts
        fLayout = QFormLayout()

        ##declare components
        label1 = QLabel('Fecha del evento:')
        label2 = QLabel('Distancia al lugar (km):*')
        label3 = QLabel('Vehículos necesarios:*')
        label4 = QLabel('Nu. de invitados:*')
        label5 = QLabel('Horas de servicio:')
        self.date = QDateEdit()
        self.distance = QSpinBox()
        self.vehicles = QSpinBox()
        self.nuGuests = QSpinBox()
        self.hoursService = QSpinBox()
        self.checkWedding = QCheckBox('Boda o XV años')

        ##components configuration
        self.date.setDateTime(QtCore.QDateTime.currentDateTime())
        self.date.setMaximumWidth(100)
        self.distance.setMinimum(0)
        self.distance.setMaximum(99999)
        self.distance.setMaximumWidth(100)
        self.vehicles.setMinimum(1)
        self.vehicles.setMaximum(9)
        self.vehicles.setMaximumWidth(100)
        self.nuGuests.setMinimum(1)
        self.nuGuests.setMaximum(9999)
        self.nuGuests.setMaximumWidth(100)
        self.hoursService.setMinimum(1)
        self.hoursService.setMaximum(99999)
        self.hoursService.setMaximumWidth(100)

        #layout structure
        fLayout.addRow(label1, self.date)
        fLayout.addRow(label2, self.distance)
        fLayout.addRow(label3, self.vehicles)
        fLayout.addRow(label4, self.nuGuests)
        fLayout.addRow(label5, self.hoursService)
        fLayout.addRow(self.checkWedding)

        self.setLayout(fLayout)


class ConfigurationSegment(QGroupBox):
    def __init__(self, parent):
        super(ConfigurationSegment, self).__init__('Configuración general')
        ##self configuration
        self.parent = parent
        self.setMaximumHeight(200)

        ##declare layouts
        vLayout1 = QVBoxLayout()
        hLayout1 = QHBoxLayout()
        hLayout2 = QHBoxLayout()
        hLayout3 = QHBoxLayout()

        ##declare components
        label1 = QLabel('Precio de gasolina (x litro):')
        label2 = QLabel('Cotización vigente hasta:')
        self.btnGeneratePDF = QPushButton('Generar PDF')
        self.btnSaveQuote = QPushButton('Guardar plantilla')
        self.btnOpenQuote = QPushButton('Abrir plantilla')
        self.checkSeparatedQuotes = QCheckBox('Cotizaciones individuales')
        self.quoteValid = QDateEdit()
        self.checkShowElemPrices = QCheckBox('Mostrar precios individuales')
        self.checkIVA = QCheckBox('Cargar IVA')
        self.gasPrice = QDoubleSpinBox()
        self.checkTotalPrice = QCheckBox('Mostrar precio total')
        self.btnNewQuote = QPushButton('Agregar cotización')
        self.checkDeposit = QCheckBox('Incluir depósito reembolsable')

        ##components configuration
        self.gasPrice.setValue(20.0)
        self.gasPrice.setMaximumWidth(70)
        self.quoteValid.setDateTime(QtCore.QDateTime.currentDateTime())
        self.quoteValid.setMaximumWidth(80)

        ##declare spacers
        hSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        ##layout strucutre
        hLayout1.addWidget(self.btnSaveQuote)
        hLayout1.addWidget(self.btnOpenQuote)

        hLayout2.addWidget(self.checkIVA)
        hLayout2.addWidget(self.checkShowElemPrices)
        hLayout2.addWidget(self.checkSeparatedQuotes)
        hLayout2.addWidget(label2)
        hLayout2.addWidget(self.quoteValid)

        hLayout3.addWidget(label1)
        hLayout3.addWidget(self.gasPrice)
        hLayout3.addWidget(self.checkTotalPrice)
        hLayout3.addWidget(self.checkDeposit)
        hLayout3.addSpacerItem(hSpacer)

        vLayout1.addWidget(self.btnGeneratePDF)
        vLayout1.addLayout(hLayout1)
        vLayout1.addLayout(hLayout2)
        vLayout1.addLayout(hLayout3)
        vLayout1.addWidget(self.btnNewQuote)

        self.setLayout(vLayout1)
        self.setMinimumWidth(300)

        ##events handler
        self.btnNewQuote.clicked.connect(self.addQuoteToParent)

    def addQuoteToParent(self):
        self.parent.addNewQuote()


class CodeSegment(QGroupBox):
    def __init__(self):
        super(CodeSegment, self).__init__('Notas de venta y códigos')
        ##self configuration
        self.setMaximumHeight(200)
        self.setMaximumWidth(350)

        ##declare layouts
        vLayout1 = QVBoxLayout()
        hLayout1 = QHBoxLayout()

        ##declare components
        self.codeTextInput = QLineEdit()
        self.codeList = QListWidget()
        self.btnAddCode = QPushButton('Agregar')
        self.btnDeleteCode = QPushButton('Quitar')

        ##components configuration
        self.codeTextInput.setPlaceholderText('Agregar nota de venta o código, ej. DESC1000$, CARGO10%')

        ##layout structure
        hLayout1.addWidget(self.btnAddCode)
        hLayout1.addWidget(self.btnDeleteCode)

        vLayout1.addWidget(self.codeTextInput)
        vLayout1.addLayout(hLayout1)
        vLayout1.addWidget(self.codeList)

        self.setLayout(vLayout1)
