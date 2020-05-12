class QuoteSettings:
    def __init__(self):
        self.allBgImgs = []
        self.allFonts = []
        self.clientTypes = []
        self.colorTheme = []
        self.pickedImg = ''
        self.greeting = ''
        self.font = ''

    def toDict(self):
        clientTypes = []
        for client in self.clientTypes:
            clientTypes.append(client.toJson())
        return {
            'pickedImg': self.pickedImg,
            'greeting': self.greeting,
            'font': self.font,
            'colorTheme': self.colorTheme,
            'clientTypes': clientTypes
        }

    def fromDict(self, dictionary):
        clientTypes = []
        for client in dictionary['clientTypes']:
            clientType = ClientType(client['name'], client['percentage'])
            clientType.fromJson(client)
            clientTypes.append(clientType)

        self.pickedImg = dictionary['pickedImg']
        self.greeting = dictionary['greeting']
        self.font = dictionary['font']
        self.colorTheme = dictionary['colorTheme']
        self.clientTypes = clientTypes


class ClientType:
    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage
        self.number = self.percentage / 100

    def toJson(self):
        return { 'name': self.name, 'percentage': self.percentage, 'number': self.number }

    def fromJson(self, dictionary):
        self.name = dictionary['name']
        self.percentage = dictionary['percentage']
        self.number = dictionary['number']
