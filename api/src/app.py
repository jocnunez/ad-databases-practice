from dotenv import dotenv_values
from flask import Flask

env = dotenv_values('../../.env')

print(env['USER'])

app = Flask(__name__)
@app.route("/")
def hello_world():
    return {"Hola": "Mundo"}

# Levantar el servicio si se ejecuta en modo App
if __name__ == "__main__":
    app.run()
