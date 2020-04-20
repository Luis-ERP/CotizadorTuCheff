from firebase import firebase
from Database import firebaseAuth

class QueryManager:
    def __init__(self, dbURL):
        self.writeFirebase = firebase.FirebaseApplication(dbURL, None)

    #### -------------------------------------------- PRIVATE -------------------------------------------- ####
    ## BASIC QUERY FUNCTIONS
    def read(self):
        pass

    def write(self):
        pass

    ## COMPOUNDED QUERY FUNCTIONS
    def append(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    #### -------------------------------------------- PUBLIC -------------------------------------------- ####
    ## CONNECT TO FIREBASE
    def connect2Firebase(self):
        pass

    ## QUOTES
    def addNewQuote(self):
        pass

    def deleteQuote(self):
        pass

    def modifyQuote(self):
        pass

    ## SERVICES
    def addNewService(self):
        pass

    def deleteService(self):
        pass

    def modifyService(self):
        pass

    ## ELEMENTS
    def addNewElement(self):
        pass

    def deleteElement(self):
        pass

    def modifyElement(self):
        pass

    ## ACCESS CONFIGURATIONS JSON
    def parseConfiguration(self):
        pass

    def modifyConfiguration(self):
        pass