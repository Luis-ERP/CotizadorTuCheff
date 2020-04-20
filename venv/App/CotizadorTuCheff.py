"""
Name: Cotizador TuCheff Eventos
Author: Luis Edgar Ramirez
Last update: 04/11/2020
License: Common Free License
Company: TuCheff Eventos

To create the executable, run the following command on CMD
pyinstaller --onefile -w --icon=Img/icon.ico CotizadorTuCheff.py
"""

#system imports
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
#other systems imports
from Source import main

class Application(QMainWindow):

    def __init__(self):
        super(Application, self).__init__()

        self.setGeometry(10, 35, 1580, 820)
        self.setWindowTitle("Cotizador TuCheff Eventos")
        #self.setWindowIcon(QtGui.QIcon('Img/Imagen1.png'))
        window = main.Main()
        self.setCentralWidget(window)


if __name__ == "__main__":
    import sys
    app = QApplication([])
    window = Application()
    window.show()
    app.exec_()
