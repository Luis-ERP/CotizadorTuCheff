from reportlab.platypus import (BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate, Spacer, Flowable)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import A4, letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from PIL import Image
from datetime import date
from time import time, strftime, localtime
import locale
import os


class WriterPDF:
    ## --------------------------------------------------- PUBLIC FUNCTIONS -------------------------------------------------------------- ##
    def __init__(self, quotes, quoteConfig, tuCheffInformation):
        ##storage vairbales
        self.quotes = quotes
        self.quoteConfig = quoteConfig
        self.tuCheffInformation = tuCheffInformation
        self.story = []

        ##pdf settings variables
        self.filePath = ''
        self.pageSize = letter
        self.fontName = ''
        self.color = [.56,0,0,.8]
        self.imgDir = 'Res/Img/mesa1.png'
        self.colorPalette = Color(self.color[0], self.color[1], self.color[2], alpha=self.color[3])

        self.currentDate = self.getCurrentDate()
        self.eventDate = self.processEventDate()
        self.dueDate = self.processDueDate()

        ##init settings
        pdfmetrics.registerFont(TTFont('Cordia', 'Res/Fonts/CORDIA.ttf'))
        pdfmetrics.registerFont(TTFont('Cordia-bold', 'Res/Fonts/CordiaNewBold.ttf'))
        pdfmetrics.registerFont(TTFont('Cordia-bold-italic', 'Res/Fonts/CordiaNewBoldItalic.ttf'))
        self.fontName = 'Cordia'
        self.makeFilePath()
        self.setParagraphStyles()

    def openBuild(self):
        os.system(self.filePath)

    def buildDoc(self):
        frameN = Frame(185, 130, 395, 525, id='normal', showBoundary=0)
        PTUnaColumna = PageTemplate(id='UnaColumna', frames=frameN, onPage=self.header, onPageEnd=self.footer)
        doc = BaseDocTemplate(self.filePath, pageTemplates=[PTUnaColumna], pagesize=self.pageSize)
        doc.build(self.story)

    def header(self, canvas, doc):
        canvas.saveState()
        self.drawBackground(canvas, self.imgDir, self.colorPalette)  # 'fondo1.png'
        pageW, pageH = canvas._pagesize
        self.drawCurrentDate(canvas, self.fontName, self.currentDate[0], self.currentDate[1], self.currentDate[2])
        canvas.restoreState()

    def footer(self, canvas, doc):
        canvas.saveState()
        self.drawFooter(canvas, self.fontName, self.dueDate[1], self.dueDate[2])
        self.drawAddressBox(canvas, self.fontName, self.tuCheffInformation['address'],
                            self.tuCheffInformation['cellPhones'], self.tuCheffInformation['email1'],
                            self.tuCheffInformation['email2'])
        canvas.restoreState()

    def drawContent(self):
        self.drawGreeting()
        self.drawQuotes(self.quotes)

    ## --------------------------------------------------- PRIVATE FUNCTIONS -------------------------------------------------------------- ##
    def getCurrentDate(self):
        locale.setlocale(locale.LC_ALL, "")
        _time = localtime(time())
        day = str(strftime("%d", _time))
        month = str(strftime("%B", _time))
        year = str(strftime("%Y", _time))
        return [day, month, year]

    def processEventDate(self):
        day = self.quoteConfig.event.date.strftime("%d")
        month = self.quoteConfig.event.date.strftime("%B")
        year = self.quoteConfig.event.date.strftime("%Y")
        return [day, month, year]

    def processDueDate(self):
        day = self.quoteConfig.configuration.dueDate.strftime("%d")
        month = self.quoteConfig.configuration.dueDate.strftime("%B")
        year = self.quoteConfig.configuration.dueDate.strftime("%Y")
        return [day, month, year]

    def makeFilePath(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        fileName = 'COTIZACION_%s%s%s%s.pdf' %(self.quoteConfig.client.lastName, self.quoteConfig.client.name, self.eventDate[1], self.eventDate[2])
        filePath = os.path.join(desktop, fileName)
        self.filePath = filePath

    def setParagraphStyles(self):
        self.titleStyle = ParagraphStyle(name='titleStyle',
                                    fontSize=20,
                                    textColor=(0, 0, 0),
                                    fontName=self.fontName + '-bold')
        self.introStyle = ParagraphStyle(name='introStyle',
                                    fontSize=17,
                                    textColor=(0, 0, 0),
                                    leading=20,
                                    fontName=self.fontName)
        self.quoteTitleStyle = ParagraphStyle(name='quoteTitleStyle',
                                         fontSize=22,
                                         textColor=self.colorPalette,
                                         fontName=self.fontName)
        self.serviceTitleStyle = ParagraphStyle(name='serviceTitleStyle',
                                           fontSize=16,
                                           textColor=(.4, 0, 0),
                                           fontName=self.fontName,
                                           leftIndent=10)
        self.elementTitleStyle = ParagraphStyle(name='elementTitleStyle',
                                           fontSize=14,
                                           textColor=(0.2, 0.2, 0.2),
                                           leftIndent=20,
                                           bulletIndent=10,
                                           bulletFontSize=15,
                                           fontName=self.fontName)
        self.quotePriceStyle = ParagraphStyle(name='quotePriceStyle',
                                         fontSize=17,
                                         textColor=self.colorPalette,
                                         leftIndent=5,
                                         fontName=self.fontName + '-bold')
        self.quoteTotalPriceStyle = ParagraphStyle(name='quotePriceStyle',
                                              fontSize=19,
                                              textColor=self.colorPalette,
                                              leftIndent=5,
                                              fontName=self.fontName + '-bold')

    def flowableFigure(self, color):
        flowable = Flowable
        flowable.canv.setFillColor(color)
        self.canv.rect(0, 0, width=130, height=draw_height, fill=True, stroke=False)

    def drawCurrentDate(self, canvas, font, day, month, year):
        pageW, pageH = canvas._pagesize
        canvas.setFillColorRGB(0, 0, 0)
        canvas.setFont(font, 14)
        textLen = canvas.stringWidth("Santiago de Querétaro a %s de %s de %s" % (day, month, year), font, 14)
        canvas.drawString(pageW - textLen - 20, pageH - 146, "Santiago de Querétaro a %s de %s de %s" % (day, month, year))

    def drawBackground(self, canvas, imgURL, color):
        pageW, pageH = canvas._pagesize
        image = Image.open(imgURL)
        imageW, imageH = image.size
        if imageW > imageH:
            pageW, pageH = pageH, pageW  # flip width/height
            canvas.setPageSize((pageW, pageH))
        canvas.drawImage(imgURL, 0, 0, width=pageW, height=pageH)

    def drawFooter(self, canvas, font, month, year):
        pageW, pageH = canvas._pagesize
        canvas.setFillColorRGB(0, 0, 0)
        canvas.setFont(font, 12)
        str1 = 'Para factura considerar costo más IVA.'
        str2 = 'Los costos incluyen IVA.'
        str3 = 'Cotización vigente hasta %s de %s'
        str4 = 'Se requiere del 50% de anticipo  para bloquear fecha'
        str5 = 'del servicio y el resto una semana antes del evento.'
        str6 = 'Para bodas y XV años se requiere de un 30% de'
        str7 = 'anticipo para reservar la fecha, y haberse liquidado'
        str8 = 'en su totalidad 15 días antes del evento.'

        x1 = 180
        y = 100
        x2 = 50
        if not self.quoteConfig.configuration.iva: # <----------------------------------------------------------------------------CAMBIAR
            canvas.drawString(x1, y, str1)
            canvas.drawString(x1, y - 15, str3  %(month, year))
        else:
            canvas.drawString(x1, y, str2)
            canvas.drawString(x1, y - 15, str3 %(month, year))

        if not self.quoteConfig.event.weddingMode:
            textLen = canvas.stringWidth(str4, font, 12)
            canvas.drawString(pageW - textLen - x2, y, str4)
            textLen = canvas.stringWidth(str5, font, 12)
            canvas.drawString(pageW - textLen - x2, y - 15, str5)
        else:
            textLen = canvas.stringWidth(str6, font, 12)
            canvas.drawString(pageW - textLen - x2, y, str6)
            textLen = canvas.stringWidth(str7, font, 12)
            canvas.drawString(pageW - textLen - x2, y - 15, str7)
            textLen = canvas.stringWidth(str8, font, 12)
            canvas.drawString(pageW - textLen - x2, y - 30, str8)

    def drawAddressBox(self, canvas, font, address, cellPhones, email1, email2):
        pageW, pageH = canvas._pagesize
        canvas.setFillColorRGB(0, 0, 0)
        canvas.setFont(font, 14)

        textLen = canvas.stringWidth(address, font, 14)
        canvas.drawString(pageW / 2 - textLen / 2 + 85, 40, address)
        textLen = canvas.stringWidth(cellPhones, font, 14)
        canvas.drawString(pageW / 2 - textLen / 2 + 85, 25, cellPhones)
        textLen = canvas.stringWidth(email1, font, 14)
        canvas.drawString(pageW / 2 - textLen / 2 + 85, 10, email1)
        textLen = canvas.stringWidth(email2, font, 14)
        canvas.drawString(pageW / 2 - textLen / 2 + 85, 0, email2)

    def drawGreeting(self):
        #box = self.flowableFigure(self.colorPalette)
        # self.story.append(box)
        self.story.append(Paragraph('Estimado cliente' + '\n', self.titleStyle))
        self.story.append(Spacer(1, 0.3 * inch))
        self.story.append(Paragraph(
            'A continuación le presento la cotización del servicio para %s invitados, solicitado para el mes de %s de %s.' % (
                self.quoteConfig.event.guests, self.eventDate[1], self.eventDate[2]) + '\n', self.introStyle))
        self.story.append(Spacer(1, 0.3 * inch))

    def drawQuotes(self, listQuotes):
        self.accumulatedPrice = 0
        for quote in listQuotes:
            self.story.append(Paragraph(quote.name + '\n', self.quoteTitleStyle))
            self.story.append(Spacer(1, 0.25 * inch))
            self.drawServices(quote.services)
            if not self.quoteConfig.configuration.individualQuotes:
                continue
            nuGuests = quote.chargeNumberGuests
            if quote.chargeNumberGuests == False:
                nuGuests = self.quoteConfig.event.guests

            self.story.append(Paragraph('COSTO total $%.2f por persona' % (self.accumulatedPrice), self.elementTitleStyle ))
            self.story.append(Spacer(1, 0.35 * inch / 2))
            if self.quoteConfig.configuration.showTotalPrice:
                self.story.append(Paragraph('COSTO total por %i personas $%.2f' %(nuGuests, self.accumulatedPrice*nuGuests), self.quoteTotalPriceStyle))
                self.story.append(Spacer(1, 0.35 * inch / 2))
            self.accumulatedPrice = 0

    def drawServices(self, listServices):
        for service in listServices:
            self.story.append(Paragraph(service.name + '\n', self.serviceTitleStyle))
            self.story.append(Spacer(1, 0.25 * inch / 2))
            self.drawElements(service.elements)

    def drawElements(self, listElements):
        for element in listElements:
            # if not visible continue next iteration
            self.accumulatedPrice += element.price
            if not element.visible:
                continue

            # if no comments, empty comments
            if element.comments == False:
                comments = ''
            else:
                comments = ' (%s)'%(element.comments)

            # if individual prices
            price = ''
            if self.quoteConfig.configuration.showIndividualPrices:
                price = ' ....................$%.2f' %(element.price) + ' /por persona'

            retultingString = element.name + comments + price
            self.story.append(Paragraph('<bullet>&bull;</bullet>' + retultingString, self.elementTitleStyle))
            self.story.append(Spacer(1, 0.25 * inch / 2))