# Estas librerías son propias del lenguaje, por eso tiene sentido usarlas en este caso
import datetime
import uuid

class Task():
    def __init__(self, text=''):
        self.id = uuid.uuid4()
        self.text = text
        self.created = self.modified = datetime.now()
        self.checked = False
        self.important = False
