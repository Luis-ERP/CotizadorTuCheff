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
        self.client = ClientSegment()
        self.event = EventSegment()
        self.configuration = ConfigurationSegment(self)
        self.code = CodeSegment()
        self.lowerSegment = LowerSegment()

        #layout structure
        self.hLayout1.addWidget(self.configuration)
        self.hLayout1.addWidget(self.client)
        self.hLayout1.addWidget(self.event)
        self.hLayout1.addWidget(self.code)

        self.vLayout1.addLayout(self.hLayout1)
        self.vLayout1.addWidget(self.lowerSegment)
        self.setLayout(self.vLayout1)
