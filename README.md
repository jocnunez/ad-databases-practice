# Práctica de Bases de Datos

## Mínimo (5 puntos)

- Estructura en Docker Compose:
  - Una Mongo con persistencia
  - Una MariaDB con persistencia
  - la(s) app(s) en python que conecten con las bbdd
- API RESTful (crud completo) en python, con el driver pymongo, sobre MongoDB
- API RESTful (crud completo) en python, con el driver mariadb, sobre MariaDB
- GraphQL que permita al menos las mismas operaciones que las APIs

### Los datos a guardar serán

- n usuarios
  - usuario:
    - id: email (no permitiremos repetir email)
    - pwd
- n listas de tareas por cada usuario
  - tarea:
    - id: uuid
    - text: el texto de la tarea
    - created: fecha de creación
    - updated: fecha de última modificación
    - checked: si la tarea está finalizada o no
    - important: si la tarea es importante o no

### Extra (5 puntos)

- Seguridad (2 puntos):
  - autenticación de usuarios
  - autorización de usuarios controlada
  - permitir creación de usuario con email y confirmación de email (fake)
- Complicar estrucura de datos (2 punto)
  - [añadiendo campos como el orden (con su lógica) ...]
  - [usando la estructura de la práctica anterior ...]
  - [tu propio caso de uso que se te pueda ocurrir ...]
  - [...]
- FastAPI o django (1 punto)

### Otras valoraciones (2 puntos)

- defensa de la práctica
- limpieza en el código
- seguir estructuras de diseño y buenas prácticas (feature toggles, clean, SOLID, ...)

### Formato de entrega

Grabar video con explicación (texto, subtitulos o voz)

## Explicación de este codebase (Pendiente de actualización)
