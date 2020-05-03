from PyQt5.QtWidgets import *
from Source.Quote.upperSegment import *
from Layouts.QuoteActivity.lowerSegment import LowerSegment

class QuoteActivity(QWidget):
    def __init__(self):
        super().__init__()

        #declare layouts
        self.vLayout1 = QVBoxLayout()
        self.hLayout1 = QHBoxLayout()

        #declare components
        self.upperLeftSegment = ClientSegment()
        self.upperCenterLeftSegment = EventSegment()
        self.upperCenterRightSegment = ConfigurationSegment(self)
        self.upperRightSegment = CodeSegment()
        self.lowerSegment = LowerSegment()

        #layout structure
        self.hLayout1.addWidget(self.upperCenterRightSegment)
        self.hLayout1.addWidget(self.upperLeftSegment)
        self.hLayout1.addWidget(self.upperCenterLeftSegment)
        self.hLayout1.addWidget(self.upperRightSegment)

        self.vLayout1.addLayout(self.hLayout1)
        self.vLayout1.addWidget(self.lowerSegment)
        self.setLayout(self.vLayout1)

    def addNewQuote(self):
        self.lowerSegment.addNewWidget()
