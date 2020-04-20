from Source.Quote.newService import NewService

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore



class GetNewQuote(QGroupBox):
    def __init__(self, parent, index):
        super(GetNewQuote, self).__init__('Cotización %s' %(str(index)))
        self.parent = parent
        self.setMaximumWidth(600)
        self.setMinimumWidth(520)

        ##declare layouts
        vLayout1 = QVBoxLayout()
        hLayout1 = QHBoxLayout()
        scrollArea = QScrollArea()
        vLayout2 = QVBoxLayout()
        wLayout = QWidget()
        self.vLayout3 = QVBoxLayout()

        ##declare components
        self.btnAddService = QPushButton('Agregar servicio')
        self.quoteName = QLineEdit()
        self.checkNuGuests = QCheckBox('Cambiar # invitados:')
        self.nuGuests = QSpinBox()
        self.btnCloseQuote = QPushButton()

        #declare spacers
        hSpacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        vSpacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        ##components configuration
        scrollArea.setStyleSheet('QScrollArea{ background-color: rgba(255,255,255,0); }')
        scrollArea.setWidgetResizable(True)
        self.quoteName.setPlaceholderText('Título de la cotización')
        self.btnCloseQuote.setIcon(QtGui.QIcon('Res/Icons/remove1.png'))
        self.nuGuests.setMinimum(1)
        self.nuGuests.setMaximum(999999)
        self.nuGuests.setMaximumWidth(40)
        self.nuGuests.setEnabled(False)

        ##layout structure
        hLayout1.addWidget(self.btnAddService)
        hLayout1.addWidget(self.quoteName)
        hLayout1.addWidget(self.checkNuGuests)
        hLayout1.addWidget(self.nuGuests)
        hLayout1.addSpacerItem(hSpacer1)
        hLayout1.addWidget(self.btnCloseQuote)

        vLayout2.addLayout(self.vLayout3)
        vLayout2.addSpacerItem(vSpacer1)
        wLayout.setLayout(vLayout2)
        scrollArea.setWidget(wLayout)

        vLayout1.addLayout(hLayout1)
        vLayout1.addWidget(scrollArea)

        self.setLayout(vLayout1)