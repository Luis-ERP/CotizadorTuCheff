from Layouts.QuoteActivity.quoteActivity import QuoteActivity
from Source.Quote.writerPDF import WriterPDF
from Database.quoteConfiguration import QuoteConfiguration
from Source.queryManager import QueryManager

import math

class Quote(QuoteActivity):
    def __init__(self):
        super(Quote, self).__init__()
        self.db = QueryManager()
        ##events handler
        self.configuration.btnGeneratePDF.clicked.connect(self.generatePDF)

    def addNewQuote(self):
        self.lowerSegment.addNewWidget()

    def generatePDF(self):
        quotesInfo = self.lowerSegment.getAllInformation()
        config = self.configuration.getConfigurationInformation()
        client = self.client.getClientInformation()
        event = self.event.getEventInformation()
        codes = self.code.getCodeInformation()
        quoteConfig = QuoteConfiguration(config, event, client, codes)

        ##modify the prices
        for q, quote in enumerate(quotesInfo):
            ##calculate number of guests
            nuGuests = quote.chargeNumberGuests
            if quote.chargeNumberGuests == False:
                nuGuests = quoteConfig.event.guests

            for s, service in enumerate(quote.services):
                quotesInfo[q].services[s] = self.applyConditionsServices(service, quote, quoteConfig, nuGuests)

                for e, element in enumerate(service.elements):
                    quotesInfo[q].services[s].elements[e] = self.applyQuantity(element)
                    quotesInfo[q].services[s].elements[e] = self.applyViaticos(element, quoteConfig, quotesInfo, nuGuests)
                    quotesInfo[q].services[s].elements[e] = self.applyClientType(element)
                    quotesInfo[q].services[s].elements[e] = self.applyCodes(element, quoteConfig)
                    quotesInfo[q].services[s].elements[e] = self.applyTaxes(element, quoteConfig)

        PDFwriter = WriterPDF(quotesInfo, quoteConfig)
        PDFwriter.drawContent()
        PDFwriter.buildDoc()
        PDFwriter.openBuild()

    def applyQuantity(self, element):
        price = element.price * element.quantity
        element.price = price
        return element

    def applyConditionsServices(self, service, quote, quoteConfig, nuGuests):
        ##check if conditions apply
        if service.perPerson==False and service.perHour==False:
            return service

        ##calculate modifiers
        reptPersons = 1
        if not(service.perPerson==False):
            reptPersons = math.ceil(nuGuests / service.perPerson)
        reptHours = 1
        if not(service.perHour==False):
            reptHours = math.ceil(quoteConfig.event.hours / service.perHour)

        ##modify all prices of elements
        for e in range(len(service.elements)):
            price = service.elements[e].price * max([reptPersons, reptHours])
            service.elements[e].price = price
        return service

    def applyViaticos(self, element, quoteConfig, quotesInfo, nuGuests):
        gasPrice = quoteConfig.configuration.gasPrice
        distance = quoteConfig.event.distance
        vehicles = quoteConfig.event.vehicles
        rendimiento = 14.75 / 100
        viaticos = gasPrice * distance * vehicles * rendimiento

        ##calculate how much is for each elements
        counter = 0
        for i in range(len(quotesInfo)):
            for ii in range(len(quotesInfo[i].services)):
                for iii in range(len(quotesInfo[i].services[ii].elements)):
                    counter += 1
        if not counter==0:
            counter = 1 #evitar division entre 0
        viaticos = viaticos / counter
        viaticos = viaticos / nuGuests
        element.price = element.price + viaticos
        return element

    def applyClientType(self, element):
        clientIndex = self.client.clientType.currentIndex()
        client = self.db.getQuoteConfiguration().clientTypes[clientIndex]
        number = client.number
        element.price = element.price * number
        return element

    def applyCodes(self, element, quoteConfig):
        codes = quoteConfig.codes.codes
        comments = quoteConfig.codes.comments
        for code in codes:
            processed = quoteConfig.codes.processCode(code)
            value = processed[1]
            if processed[0] == 'DESCU':
                value = -1 * value
            if processed[2] == '%':
                value = value / 100
                element.price = element.price + element.price*value
            elif processed[2] == '$':
                element.price = element.price + (value)
        return element

    def initialDeposit(self):
        pass

    def applyTaxes(self, element, quoteConfig):
        if not quoteConfig.configuration.iva:
            return element
        element.price = element.price * 0.16 + element.price
        return element