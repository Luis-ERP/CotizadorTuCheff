class Service:
    def __init__(self, name='', elements=[], description = ''):
        self.id = ''
        self.description = description
        self.name = name
        self.perPerson = False
        self.perHour = False
        self.elements = elements

    def toDict(self):
        return {'ServiceName': self.name, 'ServiceDescription': self.description, 'PerPerson': self.perPerson,
                'PerHour':self.perHour, 'Elements': self.elements}


    def fromDict(self, key, dictionary):
        self.id = key
        self.name = dictionary['ServiceName']
        self.description = dictionary['ServiceDescription']
        self.perPerson = dictionary['PerPerson']
        self.perHour = dictionary['PerHour']
        try:
            self.elements = dictionary['Elements']
        except:
            self.elements = []