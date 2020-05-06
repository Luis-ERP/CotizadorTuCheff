from Layouts.QuoteActivity.getNewElement import GetNewElement
from Database import element

from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class NewElement(GetNewElement):
    def __init__(self, parent):
        super(NewElement, self).__init__(parent)
        ##storage variables
        self.parent = parent
        self.visibility = True
        self.categories = []
        self.currentCategoryId = ''
        self.nameStr = ''
        self.commentsStr = ''

        ##event handlers
        self.btnVisible.clicked.connect(self.changeVisibility)
        self.category.currentIndexChanged.connect(self.fillWithCategoryInfo)
        self.btnCloseElement.clicked.connect(self.destroy)

    def setCategoriesToComboBox(self):
        for cat in self.categories:
            self.category.addItem(cat['name'])
        self.setDefaultCategory()

    def setDefaultCategory(self):
        for i in range(len(self.categories)):
            if self.categories[i]['id'] == self.currentCategoryId:
                self.category.setCurrentIndex(i)

    def fillWithCategoryInfo(self):
        info = self.categories[self.category.currentIndex()]
        self.elementName.setText(self.nameStr)
        self.comments.setText(self.commentsStr)
        self.price.setValue(info['price'])
        self.elementName.setText('%s (%s)' %(self.nameStr, info['name']))

    def changeVisibility(self):
        visible = not self.visibility
        self.setVisibility(visible)

    def setVisibility(self, visible):
        self.visibility = visible
        if self.visibility:
            self.btnVisible.setIcon(QtGui.QIcon('Res/Icons/visibleOn.png'))
        else:
            self.btnVisible.setIcon(QtGui.QIcon('Res/Icons/visibleOff.png'))

    def destroy(self):
        self.setEnabled(False)
        self.setVisible(False)
        self.parent.removeElement()

    def getElementInformation(self):
        elemObj = element.Element()
        elemObj.name = self.elementName.text()
        elemObj.visible = self.visibility
        elemObj.quantity = self.quantity.value()
        elemObj.price = self.price.value()
        elemObj.comments = self.comments.text()
        return elemObj

