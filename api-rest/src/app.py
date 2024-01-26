from pymongo import MongoClient
from flask import Flask

print('Hello World!')

client = MongoClient("mongodb://root:example@localhost:27017")
db = client.testdb

try: db.command("serverStatus")
except Exception as e: print(e)
else: print("You are connected!")

# TODO: Inicializar la base de Datos con lo necesario

## HTTP actions: GET, POST, PUT, DELETE
# API REST: READ, CREATE, UPDATE, DELETE

# TODO: Crear las rutas mínimas para tener un CRUD en flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return {"Hola": "Mundo"}

client.close()