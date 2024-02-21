from flask import Flask
from dotenv import dotenv_values

MONGO_ROUTE = '/api/v1'
MARIADB_ROUTE = '/api/v2'
GRAPHQL_ROUTE = '/graphql'

env = dotenv_values()

# TODO: Rutas visibles según los Feature Toggles
app = Flask(__name__)
@app.route('/')
def loadRoutes():
    routes = { 'mongo': MONGO_ROUTE }
    if env['FT_GRAPHQL'] == 'true':
        routes['graphql'] = GRAPHQL_ROUTE
    if env['FT_API_SQL'] == 'true':
        routes['mariadb'] = MARIADB_ROUTE

    return routes

# Levantar el servicio si se ejecuta en modo App
if __name__ == "__main__":
    app.run()
