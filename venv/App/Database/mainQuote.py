class MainQuote:
    def __init__(self, quoteValidity=[], gasPrice=20, clientType='', eventDate=[], eventDistance=0,
                 neededVehicles=1):
        self.chargeIVA = True
        self.showIndividPrices = True
        self.quoteValidity = quoteValidity
        self.gasPrice = gasPrice
        self.showTotalPrice = True
        self.refundedDeposit = False
        self.clientFirstName = ''
        self.clientLastName = ''
        self.clientEnterprise = ''
        self.clientRFC = ''
        self.clientEmail = ''
        self.clientPhone = ''
        self.clientType = clientType
        self.eventDate = eventDate
        self.eventDistance = eventDistance
        self.neededVehicles = neededVehicles
        self.nuGuests = 1
        self.nuHours = 1
        self.eventWedding = False
        self.codes = []
        self.comments = []
        self.quotes = []