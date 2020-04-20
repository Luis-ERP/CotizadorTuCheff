from Layouts import mainActivity
from Source.queryManager import QueryManager

class Main(mainActivity.MainActivity):
    def __init__(self):
        super().__init__()

        firebase = QueryManager('https://prueba-cotizador-dd3fb.firebaseio.com/')