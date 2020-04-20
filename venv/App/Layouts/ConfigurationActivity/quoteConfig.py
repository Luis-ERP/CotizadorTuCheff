from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class QuoteConfig(QGroupBox):
    def __init__(self):
        super(QuoteConfig, self).__init__('Cotizaciones')
        self.setMaximumWidth(300)


        ##declare layout
        vLayout1 = QVBoxLayout()
        fLayout1 = QFormLayout()
        self.vLayout2 = QVBoxLayout()

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
        self.btnSaveChanges = QPushButton('Guardar cambios')
        self.btnAddClientType = QPushButton('Nuevo tipo')

        ##components configuration
        vLayout1.setAlignment(QtCore.Qt.AlignLeft)

        ##layout structure
        fLayout1.addRow(label3, self.red)
        fLayout1.addRow(label4, self.green)
        fLayout1.addRow(label5, self.blue)
        fLayout1.addRow(label6, self.alpha)

        vLayout1.addWidget(label1)
        vLayout1.addWidget(self.bgImage)
        vLayout1.addWidget(label2)
        vLayout1.addLayout(fLayout1)
        vLayout1.addWidget(label7)
        vLayout1.addWidget(self.greeting)
        vLayout1.addWidget(label8)
        vLayout1.addWidget(self.font)
        vLayout1.addWidget(label9)
        vLayout1.addLayout(self.vLayout2)
        vLayout1.addWidget(self.btnSaveChanges)

        self.setLayout(vLayout1)



class NewClientType(QWidget):
    def __init__(self):
        super(NewClientType, self).__init__()