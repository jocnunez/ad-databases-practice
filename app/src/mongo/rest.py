from flask import Blueprint, request

api_rest_bp = Blueprint('api_rest_bp', __name__)

@api_rest_bp.route('/notes')
def notes():
    return { "notes": "ok" }

# def post():
#     request_data = request.json
#     # TODO: Validar el formato
#     # TODO: Insertar en la mongo
#     print("data: ", request_data)
#     return request_data


# TODO: Inicializar la base de Datos con lo necesario

## HTTP actions: GET, POST, PUT, DELETE
# API REST: READ, CREATE, UPDATE, DELETE


# Levantar el servicio si se ejecuta en modo App
#if __name__ == "__main__":
    # levantarServicio()
