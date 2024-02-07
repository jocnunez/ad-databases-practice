# Práctica de Bases de Datos

## Ejercicios de clase

### Sprint: MongoDB RESTful y GraphQL

-   Configura la app para leer variables de entorno al inicio
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
