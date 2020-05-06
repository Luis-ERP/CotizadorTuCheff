from Layouts.QuoteActivity.getNewQuote import GetNewQuote
from Source.Quote.newService import NewService
from Database import quote

from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class NewQuote(GetNewQuote):
    def __init__(self, parent, index):
        super(NewQuote, self).__init__(parent, index)

        ##events handler
        self.btnAddService.clicked.connect(self.addNewService)
        self.checkNuGuests.stateChanged.connect(self.enabledNuGuests)
        self.btnCloseQuote.clicked.connect(self.destroy)


    def enabledNuGuests(self, state):
        if state == QtCore.Qt.Checked:
            self.nuGuests.setEnabled(True)
        else:
            self.nuGuests.setEnabled(False)

    def addNewService(self):
        widget = NewService(self)
        self.vLayout3.addWidget(widget)

    def removeService(self):
        for i in range(self.vLayout3.count()):
            widget = self.vLayout3.itemAt(i)
            if not widget.widget().isEnabled():
                self.vLayout3.removeWidget(widget.widget())
                break

    def destroy(self):
        self.setEnabled(False)
        self.setVisible(False)
        self.parent.removeQuote()

    def getQuoteInformation(self):
        quoteObj = quote.Quote()
        quoteObj.services = []
        quoteObj.name = self.quoteName.text()
        if self.checkNuGuests.isChecked():
            quoteObj.chargeNumberGuests = self.nuGuests.value()
        else:
            quoteObj.chargeNumberGuests = False
        for i in range(self.vLayout3.count()):
            serv = self.vLayout3.itemAt(i).widget().getServiceInformation()
            quoteObj.services.append(serv)
        return quoteObj