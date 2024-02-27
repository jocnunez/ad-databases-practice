from dotenv import dotenv_values
from flask import Flask

from mongo import rest

ROUTES = {
    'MONGO': '/api/v1',
    'MARIADB': '/api/v2',
    'GRAPHQL': '/graphql'
}

ENV = dotenv_values()

app = Flask(__name__)

def enableRoute(moduleName = ''):
    if moduleName == 'MONGO':
        app.register_blueprint(rest.api_rest_bp, url_prefix='/test')
    print(moduleName)
    return moduleName

response = {}
for key, value in ROUTES.items():
    if ENV[key] == 'true':
        response[key] = value
        enableRoute(key)


@app.route('/')
def getRoutes():
    return response


# Levantar el servicio si se ejecuta en modo App
if __name__ == "__main__":
    app.run()
