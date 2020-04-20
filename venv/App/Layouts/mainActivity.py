from PyQt5.QtWidgets import QTabWidget

from Layouts.QuoteActivity.quoteActivity import QuoteActivity
from Source.Databases import databases
from Source.Configuration import configuration
from Source.Help import help as helpModule

class MainActivity(QTabWidget):
    def __init__(self):
        super().__init__()

        ## declare tabs
        tab1 = QuoteActivity()
        tab2 = databases.Databases()
        tab3 = configuration.Configuration()
        tab4 = helpModule.Help()

        ## define structure
        self.addTab(tab1, "Nueva Cotización")
        self.addTab(tab2, "Bases de datos")
        self.addTab(tab3, "Configuración")
        self.addTab(tab4, "Ayuda")



