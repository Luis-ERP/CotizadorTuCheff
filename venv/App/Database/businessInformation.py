
class BusinessInformation:
    def __init__(self):
        self.address = ''
        self.phone = ''
        self.telephone = ''
        self.email1 = ''
        self.email2 = ''
        self.rfc = ''
        self.taxName = ''

    def toDict(self):
        return {'address': self.address,
                'phone': self.phone,
                'telephone': self.telephone,
                'email1': self.email1,
                'email2': self.email2,
                'rfc': self.rfc,
                'taxName': self.taxName}

    def fromDict(self, dictionary):
        self.address = dictionary['address']
        self.phone = dictionary['phone']
        self.telephone = dictionary['telephone']
        self.email1 = dictionary['email1']
        self.email2 = dictionary['email2']
        self.rfc = dictionary['rfc']
        self.taxName = dictionary['taxName']