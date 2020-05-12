from Layouts.QuoteActivity import upperSegment
from Database.quoteConfiguration import *

from PyQt5 import QtCore


class ConfigurationSegment(upperSegment.ConfigurationSegment):
    def __init__(self, parent):
        super(ConfigurationSegment, self).__init__(parent)

    def getConfigurationInformation(self):
        config = Configuration()
        config.iva = self.checkIVA.isChecked()
        config.showIndividualPrices = self.checkShowElemPrices.isChecked()
        config.individualQuotes = self.checkSeparatedQuotes.isChecked()
        config.dueDate = self.quoteValid.date().toPyDate()
        config.gasPrice = self.gasPrice.value()
        config.showTotalPrice = self.checkTotalPrice.isChecked()
        config.includeDeposit = self.checkDeposit.isChecked()
        return config

    def displayMsg(self, msg='', colorStr='black', iterable=False, time=4000):
        if iterable:
            self.message.setText(msg)
            self.message.setStyleSheet('QLabel {color: %s;}' %(colorStr))
            QtCore.QTimer.singleShot(time, self.displayMsg)
        else:
            self.message.setText('')


class ClientSegment(upperSegment.ClientSegment):
    def __init__(self):
        super(ClientSegment, self).__init__()

    def getClientInformation(self):
        client = Client()
        client.name = self.nameClient.text()
        client.lastName = self.lastNameClient.text()
        client.business = self.enterprise.text()
        client.rfc = self.rfc.text()
        client.email = self.email.text()
        client.phone = self.phone.text()
        client.clintType = self.clientType.currentText()
        return client

    def displayMsg(self, msg='', colorStr='black', iterable=False, time=4000):
        if iterable:
            self.message.setText(msg)
            self.message.setStyleSheet('QLabel {color: %s;}' %(colorStr))
            QtCore.QTimer.singleShot(time, self.displayMsg)
        else:
            self.message.setText('')


class EventSegment(upperSegment.EventSegment):
    def __init__(self):
        super(EventSegment, self).__init__()

    def getEventInformation(self):
        event = Event()
        event.date = self.date.date().toPyDate()
        event.distance = self.distance.value()
        event.vehicles = self.vehicles.value()
        event.guests = self.nuGuests.value()
        event.hours = self.hoursService.value()
        event.weddingMode = self.checkWedding.isChecked()
        return event

    def displayMsg(self, msg='', colorStr='black', iterable=False, time=4000):
        if iterable:
            self.message.setText(msg)
            self.message.setStyleSheet('QLabel {color: %s;}' %(colorStr))
            QtCore.QTimer.singleShot(time, self.displayMsg)
        else:
            self.message.setText('')


class CodeSegment(upperSegment.CodeSegment):
    def __init__(self):
        super(CodeSegment, self).__init__()

        ##event handlers
        self.btnAddCode.clicked.connect(self.addTextToList)
        self.btnDeleteCode.clicked.connect(self.deleteFromList)

    def addTextToList(self):
        text = self.codeTextInput.text()
        if len(text) > 0:
            self.codeList.addItem(text)

    def deleteFromList(self):
        index = self.codeList.currentRow()
        self.codeList.takeItem(index)

    def getCodeInformation(self):
        codes = []
        comments = []
        for i in range(self.codeList.count()):
           text = self.codeList.item(i).text()
           if text[0] == '#':
               codes.append(text)
           else:
               comments.append(text)
        obj = Code()
        obj.codes = codes
        obj.comments = comments
        return obj

    def displayMsg(self, msg='', colorStr='black', iterable=False, time=4000):
        if iterable:
            self.message.setText(msg)
            self.message.setStyleSheet('QLabel {color: %s;}' %(colorStr))
            QtCore.QTimer.singleShot(time, self.displayMsg)
        else:
            self.message.setText('')