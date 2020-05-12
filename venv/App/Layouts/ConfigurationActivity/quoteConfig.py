from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from Source.queryManager import QueryManager

class QuoteConfig(QGroupBox):
    def __init__(self):
        super(QuoteConfig, self).__init__('Cotizaciones')
        self.setMaximumWidth(300)
        self.db = QueryManager()

        ##declare layout
        vLayout1 = QVBoxLayout()
        hLayout1 = QHBoxLayout()
        fLayout1 = QFormLayout()
        self.tLayout1 = QTableWidget(0, 2)

        ##declare components
        label1 = QLabel('Imagen de fondo')
        label2 = QLabel('Color de franja')
        label3 = QLabel('Rojo')
        label4 = QLabel('Verde')
        label5 = QLabel('Azul')
        label6 = QLabel('Alfa')
        label7 = QLabel('Saludo')
        label8 = QLabel('Tipo de fuente')
        label9 = QLabel('Tipos de cliente')

        self.bgImage = QComboBox()
        self.red = QDoubleSpinBox()
        self.green = QDoubleSpinBox()
        self.blue = QDoubleSpinBox()
        self.alpha = QDoubleSpinBox()
        self.greeting = QLineEdit()
        self.font = QComboBox()
        self.testFontLabel = QLabel('Prueba del Fondo #@?')
        self.btnSaveChanges = QPushButton('Guardar cambios')
        self.btnAddRowClientType = QPushButton('Añadir')
        self.btnDeleteRow = QPushButton('Quitar')
        self.message = QLabel()

        ##components configuration
        vLayout1.setAlignment(QtCore.Qt.AlignTop)
        self.btnAddRowClientType.setMaximumWidth(60)
        self.btnDeleteRow.setMaximumWidth(60)
        self.tLayout1.setHorizontalHeaderLabels(['Tipo', '% total'])
        header = self.tLayout1.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)

        imgs = self.db.getBGImagesNames()
        self.bgImage.addItems(imgs)
        fonts = self.db.getFontNames()
        self.font.addItems(fonts)

        ##layout structure
        fLayout1.addRow(label3, self.red)
        fLayout1.addRow(label4, self.green)
        fLayout1.addRow(label5, self.blue)
        fLayout1.addRow(label6, self.alpha)

        hLayout1.addWidget(label9)
        hLayout1.addWidget(self.btnAddRowClientType)
        hLayout1.addWidget(self.btnDeleteRow)

        vLayout1.addWidget(label1)
        vLayout1.addWidget(self.bgImage)
        vLayout1.addWidget(label2)
        vLayout1.addLayout(fLayout1)
        vLayout1.addWidget(label7)
        vLayout1.addWidget(self.greeting)
        vLayout1.addWidget(label8)
        vLayout1.addWidget(self.testFontLabel)
        vLayout1.addWidget(self.font)
        vLayout1.addLayout(hLayout1)
        vLayout1.addWidget(self.tLayout1)
        vLayout1.addWidget(self.message)
        vLayout1.addWidget(self.btnSaveChanges)

        self.setLayout(vLayout1)