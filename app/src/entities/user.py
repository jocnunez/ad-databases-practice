import datetime

class TaskList():
    def __init__(self, email, password, lists):
        self.email = email #(id)
        self.password = password
        self.created = self.modified = datetime.now()
        self.lists = lists
        