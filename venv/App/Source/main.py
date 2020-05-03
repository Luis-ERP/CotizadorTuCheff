from Layouts import mainActivity
from Source.queryManager import QueryManager

class Main(mainActivity.MainActivity):
    def __init__(self):
        super().__init__()
        self.dbManager = QueryManager()