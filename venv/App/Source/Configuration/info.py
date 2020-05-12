from Layouts.ConfigurationActivity.infoConfig import InfoConfig
from Database.businessInformation import BusinessInformation
from Source.queryManager import QueryManager

from PyQt5 import QtCore


class Info(InfoConfig):
    def __init__(self):
        super(Info, self).__init__()
        self.db = QueryManager()
        self.retreiveInformation()

        ##event handlers
        self.btnSaveChanges.clicked.connect(self.saveChanges)

    def saveChanges(self):
        info = BusinessInformation()
        info.address = self.address.text()
        info.phone = self.phone.text()
        info.telephone = self.telephone.text()
        info.email1 = self.email1.text()
        info.email2 = self.email2.text()
        info.rfc = self.rfc.text()
        info.taxName = self.name.text()
        try:
            self.db.setBusinessInformation(info)
            self.displayMsg(msg='Guardado correctamente', colorStr='green', iterable=True)
        except:
            self.displayMsg(msg='Ocurrió un error', colorStr='red', iterable=True)

    def retreiveInformation(self):
        info = self.db.getBusinessInformation()
        if info == False:
            self.displayMsg(msg='Ocurrió un error', colorStr='red', iterable=True)
            return
        self.address.setText(info.address)
        self.phone.setText(info.phone)
        self.telephone.setText(info.telephone)
        self.email1.setText(info.email1)
        self.email2.setText(info.email2)
        self.rfc.setText(info.rfc)
        self.name.setText(info.taxName)

    def displayMsg(self, msg='', colorStr='black', iterable=False, time=4000):
        if iterable:
            self.message.setText(msg)
            self.message.setStyleSheet('QLabel {color: %s;}' %(colorStr))
            QtCore.QTimer.singleShot(time, self.displayMsg)
        else:
            self.message.setText('')