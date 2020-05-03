class Element:
    def __init__(self, name='', price=0.0, categories=[], description='', visibility=True, id='', defaultCatId=''):
        self.id = id
        self.name = name
        self.visible = visibility
        self.price = price
        self.description = description
        self.defaultCategoryID = defaultCatId
        self.quantity = 1
        self.categories = categories
        self.categorySelectedName = ''
        self.comments = ''

    def toDict(self):
        return {'ElementName': self.name, 'Visible': self.visible, 'Price': self.price,
                'Description': self.description, 'Categories': self.categories}

    def getElementReference(self):
        return {'Id': self.id, 'Visible': self.visible, 'DefaultCategoryId': self.defaultCategoryID}

    def fromDict(self, key, dictionary):
        self.id = key
        self.name = dictionary['ElementName']
        self.visible = dictionary['Visible']
        self.price = dictionary['Price']
        self.description = dictionary['Description']
        self.comments = dictionary['Description']
        self.categories = dictionary['Categories']
