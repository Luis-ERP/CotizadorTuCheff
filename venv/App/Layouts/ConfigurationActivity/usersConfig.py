from PyQt5.QtWidgets import *


class UsersConfig(QGroupBox):
    def __init__(self):
        super(UsersConfig, self).__init__('Administrador de usuarios')
        self.setMaximumWidth(700)

        ##declare layouts
        hLayout1 = QHBoxLayout()
        vLayout1 = QVBoxLayout()
        vLayout2 = QVBoxLayout()

        ##declare components
        label1 = QLabel('Usuarios activos')
        label2 = QLabel('Solicitudes de usuarios') #aqui van chingos de labels
        self.actualUsersTable = QTableWidget(1, 6)
        self.userRequestsTable = QTableWidget(1, 6)
        self.btnUpdateInfo = QPushButton()

        ##components configuration
        self.actualUsersTable.setHorizontalHeaderLabels(['Nombre completo', 'E-mail', 'Teléfono', 'Permisos', 'Editar', 'Borrar'])
        self.userRequestsTable.setHorizontalHeaderLabels(['Nombre completo', 'E-mail', 'Teléfono', 'Permisos', 'Aceptar', 'Rechazar'])

        ##layout structure
        vLayout1.addWidget(label1)
        vLayout1.addWidget(self.actualUsersTable)
        vLayout1.addWidget(label2)
        vLayout1.addWidget(self.userRequestsTable)

        vLayout2.addWidget(self.btnUpdateInfo)

        hLayout1.addLayout(vLayout1)
        hLayout1.addLayout(vLayout2)

        self.setLayout(hLayout1)
