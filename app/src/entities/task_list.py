# Estas librerías son propias del lenguaje, por eso tiene sentido usarlas en este caso
import datetime
import uuid

class TaskList():
    def __init__(self, name='', tasks=[]):
        self.id = uuid.uuid4()
        self.name = name
        self.created = self.modified = datetime.now()
        self.tasks = tasks
