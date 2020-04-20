from Layouts.QuoteActivity.getNewQuote import GetNewQuote
from Source.Quote.newService import NewService

from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class NewQuote(GetNewQuote):
    def __init__(self, parent, index):
        super(NewQuote, self).__init__(parent, index)

        ##events handler
        self.btnAddService.clicked.connect(self.addNewService)
        self.checkNuGuests.stateChanged.connect(self.enabledNuGuests)


    def enabledNuGuests(self, state):
        if state == QtCore.Qt.Checked:
            self.nuGuests.setEnabled(True)
        else:
            self.nuGuests.setEnabled(False)

    def destroyThisWidget(self):
        self.setEnabled(False)
        self.setVisible(False)
        self.parent.removeWidget()

    def addNewService(self):
        widget = NewService(self)
        self.vLayout3.addWidget(widget)