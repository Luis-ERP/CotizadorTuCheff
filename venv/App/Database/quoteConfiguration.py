class QuoteConfiguration:
    def __init__(self, config, event, client, codes):
        self.configuration = config
        self.event = event
        self.client = client
        self.codes = codes

class Configuration:
    def __init__(self):
        self.iva = False
        self.showIndividualPrices = True
        self.individualQuotes = False
        self.dueDate = [0,0,0]
        self.gasPrice = 20
        self.showTotalPrice = False
        self.includeDeposit = False

class Client:
    def __init__(self):
        self.name = ''
        self.lastName = ''
        self.business = ''
        self.rfc = ''
        self.email = ''
        self.phone = ''
        self.clintType = ''

class Event:
    def __init__(self):
        self.date = ''
        self.distance = ''
        self.vehicles = ''
        self.guests = ''
        self.hours = ''
        self.weddingMode = ''

class Codes:
    def __init__(self, strings):
        self.codes = []
        self.comments = []
        self.processCodes(strings)
        self.processComments(strings)

    def processCodes(self, list):
        pass

    def processComments(self, list):
        pass
