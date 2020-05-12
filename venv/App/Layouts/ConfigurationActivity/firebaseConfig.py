from PyQt5.QtWidgets import *

class FirebaseConfig(QGroupBox):
    def __init__(self):
        super(FirebaseConfig, self).__init__('Firebase')
        self.setMaximumWidth(500)

        ##declare layout
        fLayout1 = QFormLayout()

        ##declare components
        label1 = QLabel('apiKey')
        label2 = QLabel('authDomain')
        label3 = QLabel('databaseURL')
        label4 = QLabel('projectId')
        label5 = QLabel('storageBucket')
        label6 = QLabel('messagingSenderId')
        label7 = QLabel('appId')
        label8 = QLabel('measurementId')
        self.apiKey = QLineEdit()
        self.authDomain = QLineEdit()
        self.databaseURL = QLineEdit()
        self.projectId = QLineEdit()
        self.storageBucket = QLineEdit()
        self.messagingSenderId = QLineEdit()
        self.appId = QLineEdit()
        self.measurementId = QLineEdit()
        self.message = QLabel()
        self.btnSaveChanges = QPushButton('Guardar cambios')

        ## set layout structure
        fLayout1.addRow(label1, self.apiKey)
        fLayout1.addRow(label2, self.authDomain)
        fLayout1.addRow(label3, self.databaseURL)
        fLayout1.addRow(label4, self.projectId)
        fLayout1.addRow(label5, self.storageBucket)
        fLayout1.addRow(label6, self.messagingSenderId)
        fLayout1.addRow(label7, self.appId)
        fLayout1.addRow(label8, self.measurementId)
        fLayout1.addRow(self.message)
        fLayout1.addRow(self.btnSaveChanges)

        self.setLayout(fLayout1)

