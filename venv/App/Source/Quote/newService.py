from Layouts.QuoteActivity.getNewService import GetNewService
from Source.Quote.newElement import NewElement

from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class NewService(GetNewService):
    def __init__(self, parent):
        super(NewService, self).__init__(parent)

        ##events handler
        self.btnAddElement.clicked.connect(self.addNewElement)
        self.checkXPerson.stateChanged.connect(self.enabledNuGuests)
        self.checkXHour.stateChanged.connect(self.enabledNuHours)

    def enabledNuGuests(self, state):
        if state == QtCore.Qt.Checked:
            self.nuGuests.setEnabled(True)
        else:
            self.nuGuests.setEnabled(False)

    def enabledNuHours(self, state):
        if state == QtCore.Qt.Checked:
            self.nuHours.setEnabled(True)
        else:
            self.nuHours.setEnabled(False)

    def addNewElement(self):
        widget = NewElement(self)
        self.vLayout3.addWidget(widget)