from Layouts.ConfigurationActivity.firebaseConfig import FirebaseConfig
from Database.firebaseConfiguration import FirebaseConfiguration
from Source.queryManager import QueryManager

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox, QPushButton

class Firebase(FirebaseConfig):
    def __init__(self):
        super(Firebase, self).__init__()
        self.db = QueryManager()
        self.retreiveInformation()

        ##event handlers
        self.btnSaveChanges.clicked.connect(self.warningMessageDisplay)

    def warningMessageDisplay(self):
        str1 = '¿Migrar la base de datos de Firebase?'
        str2 = 'No tendrá acceso a todo lo que \n' \
               'haya guardado previamente. \n' \
               'Si no se realiza correctamente \n' \
               'puede ocacionar errores fatales \n' \
               'en la aplicación.'
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        reply = msg.question(self, str1, str2,
                            msg.Cancel | msg.Save, msg.Cancel)

        if reply == msg.Save:
            self.migratedMessageDisplay()
        else:
            pass


    def migratedMessageDisplay(self):
        try:
            self.saveChanges()
            str1 = 'Datos guardados correctamente'
            str2 = 'Los datos de Firebase han sido actualizados. \n' \
                   'Cierre y vuelva a abrir la aplicación para \n' \
                   'realizar la migración.'
            msg = QMessageBox()
            reply = msg.question(self, str1, str2,
                                 msg.Ok, msg.Ok)

        except:
            str1 = 'Error'
            str2 = 'Ocurrió un error al intentar guardar los datos. \n' \
                   'Inténtelo después o contacte al técnico.'
            msg = QMessageBox()
            reply = msg.question(self, str1, str2,
                                 msg.Ok, msg.Ok)


    def saveChanges(self):
        obj = FirebaseConfiguration()
        obj.apiKey = self.apiKey.text()
        obj.authDomain = self.authDomain.text()
        obj.databaseURL = self.databaseURL.text()
        obj.projectId = self.projectId.text()
        obj.storageBucket = self.storageBucket.text()
        obj.messagingSenderId = self.messagingSenderId.text()
        obj.appId = self.appId.text()
        obj.measurementId = self.measurementId.text()
        try:
            self.db.setFirebaseConfiguration(obj)
            self.displayMsg(msg='Guardado correctamente', colorStr='green', iterable=True)
        except:
            self.displayMsg(msg='Ocurrió un error', colorStr='red', iterable=True)

    def retreiveInformation(self):
        info = self.db.getFirebaseConfiguration()
        if info == False:
            self.displayMsg(msg='Ocurrió un error', colorStr='red', iterable=True)
            return
        self.apiKey.setText(info.apiKey)
        self.authDomain.setText(info.authDomain)
        self.databaseURL.setText(info.databaseURL)
        self.projectId.setText(info.projectId)
        self.storageBucket.setText(info.storageBucket)
        self.messagingSenderId.setText(info.messagingSenderId)
        self.appId.setText(info.appId)
        self.measurementId.setText(info.measurementId)

    def displayMsg(self, msg='', colorStr='black', iterable=False, time=4000):
        if iterable:
            self.message.setText(msg)
            self.message.setStyleSheet('QLabel {color: %s;}' % (colorStr))
            QtCore.QTimer.singleShot(time, self.displayMsg)
        else:
            self.message.setText('')