from PyQt5.QtWidgets import *
from PyQt5 import QtGui

class GetNewElement(QWidget):
    def __init__(self, parent):
        super(GetNewElement, self).__init__()
        self.parent = parent

        ##declare layouts
        hLayout1 = QHBoxLayout()

        ##declare component
        self.quantity = QSpinBox()
        self.btnVisible = QPushButton()
        self.elementName = QLineEdit()
        self.category = QComboBox()
        label1 = QLabel('$')
        self.price = QDoubleSpinBox()
        self.comments = QLineEdit()
        self.btnCloseElement = QPushButton()

        ##components configuration
        self.btnCloseElement.setIcon(QtGui.QIcon('Res/Icons/remove1.png'))
        self.btnVisible.setIcon(QtGui.QIcon('Res/Icons/visibleOn.png'))
        self.elementName.setPlaceholderText('Nombre')
        self.comments.setPlaceholderText('Descripción')
        self.category.setMaximumWidth(60)
        self.elementName.setMinimumWidth(100)

        ##declare structure
        hLayout1.addWidget(self.quantity)
        hLayout1.addWidget(self.btnVisible)
        hLayout1.addWidget(self.elementName)
        hLayout1.addWidget(self.category)
        hLayout1.addWidget(label1)
        hLayout1.addWidget(self.price)
        hLayout1.addWidget(self.comments)
        hLayout1.addWidget(self.btnCloseElement)

        self.setLayout(hLayout1)