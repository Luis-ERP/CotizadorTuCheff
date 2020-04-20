from Layouts.QuoteActivity.getNewElement import GetNewElement

from PyQt5.QtWidgets import *


class NewElement(GetNewElement):
    def __init__(self, parent):
        super(NewElement, self).__init__(parent)
        self.parent = parent