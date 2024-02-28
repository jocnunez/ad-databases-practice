from datetime import datetime

class Task():
    def __init__(self, id, text=''):
        self.id = id
        self.text = text
        self.created = self.modified = datetime.now()
        self.checked = False
        self.important = False