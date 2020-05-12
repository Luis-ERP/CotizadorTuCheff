from Layouts.ConfigurationActivity.quoteConfig import QuoteConfig
from Database.quoteSettings import QuoteSettings, ClientType
from PyQt5.QtWidgets import *

from PyQt5 import QtGui, QtCore


class Quote(QuoteConfig):
    def __init__(self):
        super(Quote, self).__init__()

        self.retreiveInformation()

        ##event listeners
        self.setTestFont()
        self.btnAddRowClientType.clicked.connect(self.addRow)
        self.font.currentIndexChanged.connect(self.setTestFont)
        self.btnDeleteRow.clicked.connect(self.deleteRow)
        self.btnSaveChanges.clicked.connect(self.saveInformation)

    def retreiveInformation(self):
        information = self.db.getQuoteConfiguration()
        self.red.setValue(information.colorTheme[0])
        self.green.setValue(information.colorTheme[1])
        self.blue.setValue(information.colorTheme[2])
        self.alpha.setValue(information.colorTheme[3])
        self.greeting.setText(information.greeting)
        for i in range(self.bgImage.count()):
            if self.bgImage.itemText(i) == information.pickedImg:
                self.bgImage.setCurrentIndex(i)
                break
        for i in range(self.font.count()):
            if self.font.itemText(i) == information.font[:-4]:
                self.font.setCurrentIndex(i)
                break
        for i in range(len(information.clientTypes)):
            self.addRow()
            name = QTableWidgetItem()
            name.setText(information.clientTypes[i].name)
            self.tLayout1.setItem(i, 0, name)
            perc = QTableWidgetItem()
            perc.setText(str(information.clientTypes[i].percentage))
            self.tLayout1.setItem(i, 1, perc)

    def saveInformation(self):
        clientTypes = []
        for row in range(self.tLayout1.rowCount()):
            name = self.tLayout1.item(row, 0).text()
            value = self.tLayout1.item(row, 1).text()
            obj = ClientType(name, float(value))
            clientTypes.append(obj)
        colorTheme = [self.red.value(), self.green.value(), self.blue.value(), self.alpha.value()]
        pickedImg = self.bgImage.currentText()
        greeting = self.greeting.text()
        font = self.font.currentText() + '.ttf'
        obj = QuoteSettings()
        obj.clientTypes = clientTypes
        obj.colorTheme = colorTheme
        obj.pickedImg = pickedImg
        obj.greeting = greeting
        obj.font = font
        response = self.db.setQuoteConfiguration(obj)
        if response:
            self.displayMsg(msg='Guardado correctamente', colorStr='green', iterable=True)
        else:
            self.displayMsg(msg='Ocurrió un error', colorStr='red', iterable=True)

    def addRow(self):
        rowPosition = self.tLayout1.rowCount()
        self.tLayout1.insertRow(rowPosition)

    def deleteRow(self):
        selected = self.tLayout1.currentRow()
        self.tLayout1.removeRow(selected)

    def setTestFont(self):
        index = self.font.currentIndex()
        fontName = self.db.getFontNames()[index]
        fontFamily = self.db.getFontFamily(fontName)
        bold = 'normal'
        italic = 'normal'
        if 'Bold' in fontFamily[1]:
            bold = 'bold'
        elif 'Light' in fontFamily[1]:
            bold = '100'
        elif 'Medium' in fontFamily[1]:
            bold = '600'
        if 'Italic' in fontFamily[1]:
            italic = 'italic'
        self.testFontLabel.setStyleSheet("QLabel { color: black; font: 18pt '%s'; font-style: %s; font-weight: %s; }"
                                         %(fontFamily[0], italic, bold))

    def displayMsg(self, msg='', colorStr='black', iterable=False, time=4000):
        if iterable:
            self.message.setText(msg)
            self.message.setStyleSheet('QLabel {color: %s;}' %(colorStr))
            QtCore.QTimer.singleShot(time, self.displayMsg)
        else:
            self.message.setText('')
