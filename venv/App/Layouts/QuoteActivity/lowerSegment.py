from Source.Quote.newQuote import NewQuote

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui


class LowerSegment(QScrollArea):
    def __init__(self):
        super(LowerSegment, self).__init__()
        self.setStyleSheet('QScrollArea{ background-color: rgba(255,255,255,0); }')
        self.setWidgetResizable(True)

        ##declare layouts
        mainWidget = QWidget()
        self.hLayout1 = QHBoxLayout()

        ##components configuration
        self.hLayout1.setAlignment(QtCore.Qt.AlignLeft)

        ##layout structure
        mainWidget.setLayout(self.hLayout1)
        self.setWidget(mainWidget)


    def addNewWidget(self):
        widget = NewQuote(self, self.hLayout1.count()+1)
        self.hLayout1.addWidget(widget)

    def removeQuote(self):
        for i in range(self.hLayout1.count()):
            widget = self.hLayout1.itemAt(i)
            if not widget.widget().isEnabled():
                self.hLayout1.removeWidget(widget.widget())
                break

    def getAllInformation(self):
        quotes = []
        for i in range(self.hLayout1.count()):
            quotes.append(self.hLayout1.itemAt(i).widget().getQuoteInformation())
        return quotes