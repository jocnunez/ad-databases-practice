from dotenv import dotenv_values
from flask import Flask, request
from pymongo import MongoClient

env = dotenv_values()

user = env["USER"]
password = env["PASSWORD"]
host = env["HOST"]
port = env["PORT"]

client = MongoClient(f"mongodb://{user}:{password}@{host}:{port}")
db = client.testdb

try: db.command("serverStatus")
except Exception as e: print(e)
else: print("You are connected!")

# POST
@app.route("/notes", methods=["POST"])
def post():
    request_data = request.json
    # TODO: Validar el formato
    # TODO: Insertar en la mongo
    print("data: ", request_data)
    return request_data

client.close()

# TODO: Inicializar la base de Datos con lo necesario

## HTTP actions: GET, POST, PUT, DELETE
# API REST: READ, CREATE, UPDATE, DELETE
