from firebase import firebase
import pyrebase
import requests

from Database.quote import Quote
from Database.service import Service
from Database.element import Element
from Database.configuration import Configuration


config = {
    "apiKey": "AIzaSyAjm9GAUbdlpN1KtjY_AOLjR9OcnvYExxg",
    "authDomain": "prueba-cotizador-dd3fb.firebaseapp.com",
    "databaseURL": "https://prueba-cotizador-dd3fb.firebaseio.com",
    "projectId": "prueba-cotizador-dd3fb",
    "storageBucket": "prueba-cotizador-dd3fb.appspot.com",
    "messagingSenderId": "452704216145",
    "appId": "1:452704216145:web:a5d2883ccf4de7a4d60470",
    "measurementId": "G-8DL2NKTSW0"
}


class QueryManager:
    def __init__(self):
        """
        Firebase rules
        append: push()
        retreive: get()
        update: update()
        get value: val()
        get key: key()
        remove: remove()
        parse children: each()
        """
        self.firebaseApp = pyrebase.initialize_app(config)
        self.db = self.firebaseApp.database()
        self.auth = self.firebaseApp.auth()

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


    ## ACCESS CONFIGURATIONS JSON
    def getConfiguration(self):
        configuration = self.db.child('Configuration').get().val()
        return configuration

    def modifyConfiguration(self, newConfig):
        base = Configuration()
        if type(newConfig) != type(base):
            return None
        self.db.child('Configuration').update(newConfig)


    ##AUTHENTICATION
    def createNewUser(self, user, confimEmail, confirmPass):
        success1 = self.confirmEmail(user.email, confimEmail)
        success2 = self.confirmPassword(user.password, confirmPass)
        if not (success1 and success2):
            return 'PASSWORD_OR_EMAIL_DOESNT_MATCH'

        try:
            newUser = self.auth.create_user_with_email_and_password(user.email, user.password)
        except requests.HTTPError as e:
            response = e.args[0].response
            error = response.json()['error']['message']
            return error

        userToDB = self.createNewUserDB(user)
        if not (userToDB == True):
            return userToDB
        return True

    def createNewUserDB(self, user):
        try:
            userDict = user.toDict()
            self.db.child('Users').push(userDict)
            return True
        except requests.HTTPError as e:
            response = e.args[0].response
            error = response.json()['error']['message']
            return error

    def confirmEmail(self, email, confimation):
        return email == confimation

    def confirmPassword(self, password, confirmation):
        return password == confirmation

    def signIn(self, email, password):
        try:
            login = self.auth.sign_in_with_email_and_password(email, password)
            return True
        except requests.HTTPError as e:
            response = e.args[0].response
            error = response.json()['error']['message']
            return error

    def signOut(self):
        pass