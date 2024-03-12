from dataclasses import dataclass
import datetime

@dataclass
class User():
    id: str #TODO: the id is an email so ... regex validation
    password: str #TODO: hash the password?
    name: str
    created:datetime
    modified:datetime
    
    def __post_init__(self):
        self.created = self.modified = datetime.now()
