class Quote:
    def __init__(self, name='', services=[]):
        self.name = name
        self.chargeNumberGuests = False
        self.services = services

    def toDict(self):
        return {'QuoteName': self.name, 'ChargeNumberGuests': self.chargeNumberGuests, 'ServicesList':self.services}

    def fromDict(self, dictionary):
        self.name = dictionary['QuoteName']
        self.chargeNumberGuests = dictionary['ChargeNumberGuests']
        self.services = dictionary['ServicesList']