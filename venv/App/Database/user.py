
class User:
    def __init__(self):
        self.id = ''
        self.name = ''
        self.email = ''
        self.password = ''
        self.phone = ''
        self.permissions = Permissions()
        self.loggedIn = False

    def toDict(self):
        permissions = self.permissions.toDict()
        return {'name': self.name, 'email': self.email, 'phone': self.phone, 'permissions': permissions}

    def fromDict(self, dictionary, id):
        permissionsObj = Permissions()
        permissionsObj.fromDict(dictionary['permissions'])
        self.id = id
        self.name = dictionary['name']
        self.email = dictionary['email']
        self.phone = dictionary['phone']
        self.permissions = permissionsObj


class Permissions:
    def __init__(self):
        self.createPDFQuotes = False
        self.saveQuoteTemplates = False
        self.openQuoteTemplates = False
        self.createFactura = False

        self.accessServicesDatabase = False
        self.accessElementsDatabase = False

        self.readQuoteConfiguration = False
        self.readUsers = False
        self.readBusinessInformation = False
        self.readFirebaseConfiguration = False
        self.readClientTypes = False
        self.writeQuoteConfiguration = False
        self.writeUsers = False
        self.writeBusinessInformation = False
        self.writeFirebaseConfiguration = False
        self.createSecurityBackup = False
        self.writeClientTypes = False

    def toDict(self):
        return {
            'createPDFQuotes': self.createPDFQuotes,
            'saveQuoteTemplates': self.saveQuoteTemplates,
            'openQuoteTemplates': self.openQuoteTemplates,
            'createFactura': self.createFactura,

            'accessServicesDatabase': self.accessServicesDatabase,
            'accessElementsDatabase': self.accessElementsDatabase,

            'readQuoteConfiguration': self.readQuoteConfiguration,
            'readUsers': self.readUsers,
            'readBusinessInformation': self.readBusinessInformation,
            'readFirebaseConfiguration': self.readFirebaseConfiguration,
            'readClientTypes': self.readClientTypes,
            'writeQuoteConfiguration': self.writeQuoteConfiguration,
            'writeUsers': self.writeUsers,
            'writeBusinessInformation': self.writeBusinessInformation,
            'writeFirebaseConfiguration': self.writeFirebaseConfiguration,
            'createSecurityBackup': self.createSecurityBackup,
            'writeClientTypes': self.writeClientTypes
        }

    def fromDict(self, dictionary):
        self.createPDFQuotes = dictionary['createPDFQuotes']
        self.saveQuoteTemplates = dictionary['saveQuoteTemplates']
        self.openQuoteTemplates = dictionary['openQuoteTemplates']
        self.createFactura = dictionary['createFactura']

        self.accessServicesDatabase = dictionary['accessServicesDatabase']
        self.accessElementsDatabase = dictionary['accessElementsDatabase']

        self.readQuoteConfiguration = dictionary['readQuoteConfiguration']
        self.readUsers = dictionary['readUsers']
        self.readBusinessInformation = dictionary['readBusinessInformation']
        self.readFirebaseConfiguration = dictionary['readFirebaseConfiguration']
        self.readClientTypes = dictionary['readClientTypes']
        self.writeQuoteConfiguration = dictionary['writeQuoteConfiguration']
        self.writeUsers = dictionary['writeUsers']
        self.writeBusinessInformation = dictionary['writeBusinessInformation']
        self.writeFirebaseConfiguration = dictionary['writeFirebaseConfiguration']
        self.createSecurityBackup = dictionary['createSecurityBackup']
        self.writeClientTypes = dictionary['writeClientTypes']


class Anonymous(Permissions):
    def __init__(self):
        super(Anonymous, self).__init__()
        self.createPDFQuotes = True
        self.openQuoteTemplates = True

class Developer(Permissions):
    def __init__(self):
        self.createPDFQuotes = True
        self.saveQuoteTemplates = True
        self.openQuoteTemplates = True
        self.createFactura = True

        self.accessServicesDatabase = True
        self.accessElementsDatabase = True

        self.readQuoteConfiguration = True
        self.readUsers = True
        self.readBusinessInformation = True
        self.readFirebaseConfiguration = True
        self.readClientTypes = True
        self.writeQuoteConfiguration = True
        self.writeUsers = True
        self.writeBusinessInformation = True
        self.writeFirebaseConfiguration = True
        self.createSecurityBackup = True
        self.writeClientTypes = True

class MainAdmin(Permissions):
    def __init__(self):
        super(MainAdmin, self).__init__()
        self.createPDFQuotes = True
        self.saveQuoteTemplates = True
        self.openQuoteTemplates = True
        self.createFactura = True

        self.accessServicesDatabase = True
        self.accessElementsDatabase = True

        self.readQuoteConfiguration = True
        self.readUsers = True
        self.readBusinessInformation = True
        self.readClientTypes = True
        self.writeQuoteConfiguration = True
        self.writeUsers = True
        self.writeBusinessInformation = True
        self.createSecurityBackup = True
        self.writeClientTypes = True

class Admin(Permissions):
    def __init__(self):
        super(Admin, self).__init__()
        self.createPDFQuotes = True
        self.saveQuoteTemplates = True
        self.openQuoteTemplates = True
        self.createFactura = True

        self.accessServicesDatabase = True
        self.accessElementsDatabase = True

        self.readQuoteConfiguration = True
        self.readBusinessInformation = True
        self.readClientTypes = True
        self.writeQuoteConfiguration = True
        self.writeClientTypes = True

class Worker(Permissions):
    def __init__(self):
        super(Worker, self).__init__()
        self.createPDFQuotes = True
        self.saveQuoteTemplates = True
        self.openQuoteTemplates = True

        self.accessServicesDatabase = True
        self.accessElementsDatabase = True

        self.readQuoteConfiguration = True
        self.readClientTypes = True
        self.writeQuoteConfiguration = True

class Capturador(Permissions):
    def __init__(self):
        self.saveQuoteTemplates = True
        self.openQuoteTemplates = True

        self.accessServicesDatabase = True
        self.accessElementsDatabase = True