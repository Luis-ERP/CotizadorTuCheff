class FirebaseConfiguration:
    def __init__(self):
        self.apiKey = ''
        self.authDomain = ''
        self.databaseURL = ''
        self.projectId = ''
        self.storageBucket = ''
        self.messagingSenderId = ''
        self.appId = ''
        self.measurementId = ''

    def toDict(self):
        return {
            "apiKey": self.apiKey,
            "authDomain": self.authDomain,
            "databaseURL": self.databaseURL,
            "projectId": self.projectId,
            "storageBucket": self.storageBucket,
            "messagingSenderId": self.messagingSenderId,
            "appId": self.appId,
            "measurementId": self.measurementId
        }

    def fromDict(self, dictionary):
        self.apiKey = dictionary['apiKey']
        self.authDomain = dictionary['authDomain']
        self.databaseURL = dictionary['databaseURL']
        self.projectId = dictionary['projectId']
        self.storageBucket = dictionary['storageBucket']
        self.messagingSenderId = dictionary['messagingSenderId']
        self.appId = dictionary['appId']
        self.measurementId = dictionary['measurementId']
