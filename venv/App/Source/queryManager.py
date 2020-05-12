import json, os, requests, pyrebase, re

from PyQt5.QtGui import QFontDatabase

from Database.user import User, Permissions
from Database.quote import Quote
from Database.service import Service
from Database.element import Element
from Database.quoteSettings import QuoteSettings
from Database.configuration import Configuration
from Database.businessInformation import BusinessInformation
from Database.firebaseConfiguration import FirebaseConfiguration


class QueryManager:
    def __init__(self):
        with open('Database/Json/firebase_configuration.json') as f:
            firebaseConfig = json.load(f)
        self.firebaseApp = pyrebase.initialize_app(firebaseConfig)
        self.db = self.firebaseApp.database()
        self.auth = self.firebaseApp.auth()
        self.uploadAllFontsToQT()

    #### -------------------------------------------- PUBLIC -------------------------------------------- ####

    ## SERVICES
    def getServiceById(self, id):
        service = self.db.child('Service').child(id).get().val()
        servObj = Service()
        servObj.fromDict(id, service)
        return servObj

    def getAllServices(self):
        keys = self.db.child('Service').get().val()
        if keys == None:
            return []
        servObjs = []
        for key in keys:
            serv = self.getServiceById(str(key))
            servObjs.append(serv)
        return servObjs

    def addNewService(self, service):
        baseService = Service()
        if type(service) != type(baseService):
            return None
        newService = service.toDict()
        self.db.child('Service').push(newService)

    def deleteService(self, id):
        self.db.child('Service').child(id).remove()

    def modifyService(self, service):
        baseService = Service()
        if type(service) != type(baseService):
            return None
        self.db.child('Service').child(service.id).update(service)


    ## ELEMENTS
    def getElementById(self, id):
        element = self.db.child('Element').child(id).get().val()
        elemObj = Element()
        elemObj.fromDict(id, element)
        return elemObj

    def getAllElements(self):
        keys = self.db.child('Element').get().val()
        if keys == None:
            return []
        elemObjs = []
        for key in keys:
            elem = self.getElementById(str(key))
            elemObjs.append(elem)
        return elemObjs

    def addNewElement(self, element):
        baseElement = Element()
        if type(baseElement) != type(element):
            return None
        newElem = element.toDict()
        self.db.child('Element').push(newElem)

    def deleteElement(self, id):
        self.db.child('Element').child(id).remove()

    def deleteElementInServices(self, elementId, indexId):
        allServices = self.getAllServices()
        for service in allServices:
            for elem in service.elements:
                if elem['Id'] == elementId:
                    self.db.child('Service').child(service.id).child('Elements').child(indexId).remove()

    def modifyElement(self, element):
        baseElement = Element()
        if type(baseElement) != type(element):
            return None
        self.db.child('Element').child(element.id).update(element)


    ##AUTHENTICATION
    def createNewUser(self, user, confimEmail, confirmPass):
        success1 = self.confirmEmail(user.email, confimEmail)
        success2 = self.confirmPassword(user.password, confirmPass)
        if not (success1 and success2):
            return 'PASSWORD_OR_EMAIL_DOESNT_MATCH'

        try:
            newUser = self.auth.create_user_with_email_and_password(user.email, user.password) #register user
            userToken = self.auth.sign_in_with_email_and_password(user.email, user.password) #sign in user
            info = self.auth.get_account_info(userToken['idToken']) #get user information
            uid = info['users'][0]['localId'] # retreive uid to make id in the other DB
            user.id = uid
            userToDB = self.createNewUserDB(user)
        except requests.HTTPError as e:
            response = e.args[0].response
            error = response.json()['error']['message']
            return error
        if not (userToDB == True):
            return userToDB
        return True

    def createNewUserDB(self, user):
        try:
            userDict = user.toDict()
            self.db.child('Users').child(user.id).set(userDict)
            return True
        except requests.HTTPError as e:
            response = e.args[0].response
            error = response.json()['error']['message']
            return error

    def confirmEmail(self, email, confimation):
        return email == confimation

    def confirmPassword(self, password, confirmation):
        return password == confirmation

    def signIn(self, user):
        try:
            userToken = self.auth.sign_in_with_email_and_password(user.email, user.password) #sign in
            usersInfo = self.auth.get_account_info(userToken['idToken']) #retreive uid from auth
            uid = usersInfo['users'][0]['localId']
            fromFirebaseDB = self.db.child('Users').child(uid).get().val() #get user from my db
            permissions = Permissions() #create permissions obj
            permissions.fromDict(fromFirebaseDB['permissions']) #fill it with the info from db
            user.id = uid
            user.name = fromFirebaseDB['name']
            user.permissions = permissions
            userDict = user.toDict()
            with open('Database/Json/user_account.json', 'w') as f:
                json.dump(userDict, f)
            return True
        except requests.HTTPError as e:
            response = e.args[0].response
            error = response.json()['error']['message']
            return error

    def signOut(self):
        pass


    ## ACCESS CONFIGURATIONS JSON
    def getActiveUsers(self): # firebase
        try:
            usersDict = self.db.child('Users').get().val()
            usersList = []
            for key in usersDict:
                user = User()
                user.fromDict(usersDict[key], key)
                usersList.append(user)
            return usersList
        except:
            return False

    def getBusinessInformation(self): # firebase
        try:
            infoDict = self.db.child('BusinessInformation').get().val()
            info = BusinessInformation()
            info.fromDict(infoDict)
            return info
        except:
            return False

    def getFirebaseConfiguration(self): # local
        try:
            with open('Database/Json/firebase_configuration.json') as f:
                jsonFile = json.load(f)
                _object = FirebaseConfiguration()
                _object.fromDict(jsonFile)
                return _object
        except:
            return False

    def getNewUserRequests(self): # firebase
        pass

    def getQuoteConfiguration(self): # local
        with open('Database/Json/quote_settings.json') as f:
            jsonFile = json.load(f)
            _object = QuoteSettings()
            _object.fromDict(jsonFile)
            return _object

    def getUserAccount(self): # local
        try:
            with open('Database/Json/user_account.json') as f:
                jsonFile = json.load(f)
                object = User()
                object.fromDict(jsonFile)
                return object
        except:
            return False

    def changeActiveUser(self, user): # firebase
        baseUser = User()
        if type(baseUser) != type(user):
            return None
        allUsers = self.getActiveUsers()
        key = ''
        for item in allUsers:
            if item.email == user.email:
                key = item.key
        if not key: #if empty
            return None
        userDict = user.toDict()
        self.db.child('Users').child(key).update(userDict)

    def setBusinessInformation(self, _object): # firebase
        baseObj = BusinessInformation()
        if type(baseObj) != type(_object):
            return None
        infoDict = _object.toDict()
        self.db.child('BusinessInformation').set(infoDict)

    def setFirebaseConfiguration(self, _object): # local
        baseObj = FirebaseConfiguration()
        if type(baseObj) != type(_object):
            return None
        infoDict = _object.toDict()
        print(infoDict)
        with open('Database/Json/firebase_configuration.json', 'w') as f:
            json.dump(infoDict, f)

    def setNewUserRequests(self): # firebase
        pass

    def setQuoteConfiguration(self, _object): # local
        try:
            baseObj = QuoteSettings()
            if type(baseObj) != type(_object):
                return False
            infoDict = _object.toDict()
            with open('Database/Json/quote_settings.json', 'w') as f:
                json.dump(infoDict, f)
                return True
        except:
            return False

    def setUserAccount(self, _object): # local
        baseObj = User()
        if type(baseObj) != type(_object):
            return None
        infoDict = _object.toDict()
        with open('Database/Json/user_account.json', 'w') as f:
            json.dump(infoDict, f)


    ## BACKGROUND IMAGES
    def getBGImages(self):
        imgs = os.listdir('Res/Img/')
        return imgs

    def getBGImagesNames(self):
        imgs = self.getBGImages()
        imgNames = []
        for i in imgs:
            imgNames.append(i[:-4])
        return imgNames

    def getBGImagesDir(self):
        imgs = self.getBGImages()
        imgsDir = []
        for i in imgs:
            imgsDir.append('Res/Img/' + i)
        return imgsDir


    ## FONTS
    def getFonts(self):
        fontFileNames = os.listdir('Res/Fonts/')
        return fontFileNames

    def getFontNames(self):
        fonts = self.getFonts()
        fontsNames = []
        for i in fonts:
            fontsNames.append(i[:-4])
        return fontsNames

    def getFontsDir(self):
        fonts = self.getFonts()
        fontsDir = []
        for i in fonts:
            fontsDir.append('Res/Fonts/' + i)
        return fontsDir

    def uploadAllFontsToQT(self):
        fontsDir = self.getFontsDir()
        for fontDir in fontsDir:
            self.uploadFontToQT(fontDir)

    def uploadFontToQT(self, fontDir):
        fontDB = QFontDatabase()
        uploaded = fontDB.addApplicationFont(fontDir)
        return uploaded

    def getFontFamily(self, fontName): # AmaticSC-bold
        regularSplitted = fontName.split('-') # [AmaticSC, bold]
        fontSplitted = self.camelCaseSplit(regularSplitted[0]) # [Amatic, SC]
        strNoCamelCase = ' '.join(fontSplitted) # Amatic SC
        if len(regularSplitted) > 1:
            return (strNoCamelCase, regularSplitted[1])
        return (strNoCamelCase)

    def camelCaseSplit(self, identifier):
        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
        return [m.group(0) for m in matches]