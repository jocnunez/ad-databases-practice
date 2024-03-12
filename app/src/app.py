# from dotenv import dotenv_values
# from flask import Flask
# from graphene import GraphQLApp, GraphQLRouter
# from interfaces import rest

# # ROUTES = {
# #     'MONGO': '/api/v1',
# #     'MARIADB': '/api/v2',
# #     'GRAPHQL': '/graphql'
# # }

# # ENV = dotenv_values()

# # app = Flask(__name__)

# # def enableRoute(moduleName = ''):
# #     if moduleName == 'MONGO':
# #         app.register_blueprint(rest.api_rest_bp, url_prefix='/test')
# #     print(moduleName)
# #     return moduleName

# # response = {}
# # for key, value in ROUTES.items():
# #     if ENV[key] == 'true':
# #         response[key] = value
# #         enableRoute(key)


# # @app.route('/')
# # def getRoutes():
# #     return response


# # # Levantar el servicio si se ejecuta en modo App
# # if __name__ == "__main__":
# #     app.run()

import strawberry
 
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
 
 
@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"
 
 
schema = strawberry.Schema(Query)
 
graphql_app = GraphQLRouter(schema)
 
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

# Levantar el servicio si se ejecuta en modo App
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)