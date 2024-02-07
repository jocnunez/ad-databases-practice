from flask import Flask, request
from dotenv import dotenv_values

env = dotenv_values()
#env["GRAPHQL"]

# TODO: Crear las rutas mínimas para tener un CRUD en flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return {"Hola": "Mundo"}



# Levantar el servicio si se ejecuta en modo App
if __name__ == "__main__":
    app.run()
