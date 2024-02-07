from pymongo import MongoClient
from flask import Flask, request
from dotenv import load_dotenv, dotenv_values


print("Hello World!")

env = dotenv_values()
user = env["USER"]
password = env["PASSWORD"]
host = env["HOST"]
port = env["PORT"]
print(user)

 client = MongoClient(f"mongodb://{user}:{password}@{host}:{port}")
# db = client.testdb

# try: db.command("serverStatus")
# except Exception as e: print(e)
# else: print("You are connected!")

# client.close()

# TODO: Inicializar la base de Datos con lo necesario

## HTTP actions: GET, POST, PUT, DELETE
# API REST: READ, CREATE, UPDATE, DELETE

# TODO: Crear las rutas mínimas para tener un CRUD en flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return {"Hola": "Mundo"}

# POST
@app.route("/notes", methods=["POST"])
def post():
    request_data = request.json
    # TODO: Validar el formato
    # TODO: Insertar en la mongo
    print("data: ", request_data)
    return request_data

# Levantar el servicio si se ejecuta en modo App
if __name__ == "__main__":
    app.run()
