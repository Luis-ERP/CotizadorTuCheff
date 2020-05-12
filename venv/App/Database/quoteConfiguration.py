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

class Code:
    def __init__(self):
        self.codes = []
        self.comments = []

    def processCode(self, text):
        text = text[1:]
        action = text[:5]  # get action (DESCU/CARGO)
        text = text[5:]
        value = []
        symbol = ''
        quote = []
        service = []
        element = []

        for n in text:
            if '%' in n or '$' in n:
                symbol = n
                break
            else:
                value.append(n)
        text = text[len(value) + 1:]
        value = int(''.join(value))

        if len(text) <= 0:
            return (action, value, symbol, 0, 0, 0)

        for n in text:
            if n == '.':
                break
            else:
                quote.append(n)

        text = text[len(quote) + 1:]
        try:
            quote = int(''.join(quote))
        except:
            quote = 0
        if len(text) <= 0:
            return (action, value, symbol, quote, 0, 0)

        for n in text:
            if n == '.':
                break
            else:
                service.append(n)

        text = text[len(service) + 1:]
        service = int(''.join(service))
        if len(text) <= 0:
            return (action, value, symbol, quote, service, 0)

        for n in text:
            if n == '.':
                break
            else:
                element.append(n)
        element = int(''.join(element))
        return (action, value, symbol, quote, service, element)