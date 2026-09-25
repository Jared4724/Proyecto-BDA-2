# Proyecto Final - Desarrollo Basado en Plataformas
## Sistema de Carnet Cultural 
# Integrantes:


377043 – Angel Rodriguez Palomino

377304 – Zahid Alberto Jimenes Pérez

377061 – Jared Isai López Espino




# Requisitos para el Proyecto Final:
* Implementación sobre el framework Spring Boot
* Manejo de base de datos (altas, bajas, cambios y consultas )
* Implementación de almenas 2 rutas de Apache Camel
* Plantilla de estilo admin
* Conexión con RabbitMq
* Opcional conexión a REDIS

# Puertos usados:
- 8080 - Aplicacion
- 6379 - REDIS
- 5672 - RabbitMQ 
- 1521 - Oracle 

# Interfaz
## Plantilla de estilo Admin 

![Captura de pantalla interfaz](img/interfaz_imagen.JPG)

# Base de datos:
## Conexion a base de datos oracle 

![Captura de pantalla conexion a oracle](img/conexion_oracle.JPG)

## Ejemplo repositorio para acceder a base de datos 

![ejemplo repositorio para acceder a base de datos](img/ejemplo_repositorio.JPG)

# Apache camel:
## Implementación de ruta 1
En esta implementacion de ruta  Se utiliza el componente 'spring-rabbitmq' de Apache Camel para consumir mensajes de forma asíncrona desde un exchange de RabbitMQ.

![ruta 1 apache camel](img/ruta1_apache_camel.JPG)

## Implementación de ruta 2
En esta implementacion de ruta donde se usa SEDA, el cual es un componente de Camel que crea colas asíncronas en la memoria de la aplicación. Es perfecto para simulaciones rápidas sin depender de RabbitMQ.

![ruta 2 apache camel](img/ruta2_apache_camel.JPG)

# RabbitMQ
## Conexión con RabbitMq

 ![Captura de pantalla conexion a rabbitMQ](img/conexion_rabbitMQ.JPG)


# REDIS
## Conexión a REDIS

 ![Captura de pantalla conexion a oracle](img/conexion_redis.JPG)

## Redis config

![Captura de pantalla uso de redis](img/uso_redis.JPG)

## Cache config

![Captura de pantalla uso de cache](img/cache_config.JPG)



