# Práctica de Bases de Datos

## Entrega de la práctica
### Mínimo (5 puntos)
 - Estructura en Docker Compose:
    - Una Mongo con persistencia
    - Una MariaDB con persistencia
    - la(s) app(s) en python que conecten con las bbdd
 - API RESTful (crud completo) en python, con el driver pymongo, sobre MongoDB
 - API RESTful (crud completo) en python, con el driver mariadb, sobre MariaDB
 - GraphQL que permita al menos las mismas operaciones que las APIs
##### Los datos a guardar serán:
 - n usuarios
 - n listas de tareas por cada usuario
 - tareas:
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
 - FastAPI o django (1 punto)

### Otras valoraciones (2 puntos)
 - defensa de la práctica
 - limpieza en el código
 - seguir estructuras de diseño y buenas prácticas (feature toggles, clean, solid)

## Ejercicios de clase

### Sprint: MongoDB RESTful y GraphQL

-   Configura la app para leer variables de entorno al inicio (librería dotenv)
-   Diseña la app de forma modular
-   Añade a la ruta raíz en formato HATEOAS la ruta del READ de las notas de la API REST
-   Añade una variable de entorno que si está activa añada otra ruta más. La ruta devolverá:
    ```JSON
    {
        graphql: false
    }
    ```

# Preparación (Pendiente de actualización)

-   Instalar Python en local para facilitar la depuración
-   Crear Volumen con Docker Compose para la MongoDB
    -   Buscar en Docker Hub la imagen oficial de Mongo
    -   En nuestro caso usaremos mongo:6.0.13-jammy
    -   Expondremos el puerto por defecto de Mongo para poder acceder desde fuera del contenedor

### Entrega de la práctica

-   CRUD completa de MongoDB para ToDo App
-   Aplicación de JSON Schema para validar los ToDos

Formato de entrega: Grabar video con explicación (texto, subtitulos o voz)
