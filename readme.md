# Python RabbitMQ Simple App
Este proyecto es un ejemplo de cómo configurar y ejecutar una aplicación Python que se conecta a un servidor RabbitMQ utilizando Docker.
Este proyecto reemplaza al de Springboot pricipalmente porque no me gusta Java haha, pero tambíen porque mi lenguaje principal es Python y saber como hacerlo en este lenguaje me parece más útil profesionalmente, además de poner una dificultad extra al seguir el taller.

## Python RabbitMQ Multi App
Este proyecto es un ejemplo de cómo configurar y ejecutar dos aplicaicones de RabbitMQ como ejemplo de caso de uso, donde quiero enviar un mensaje por metodos rest desde una API o desde el navegador. 

## Requisitos

- Docker instalado en tu máquina
- Python 3.x instalado (3.10.0 recomendado)
- pip (Python package installer)

## Configuración del proyecto

    ```sh
    docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    python3.10 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python main.py
    ```

## Ejecución del proyecto simple

    ```sh
    python rabbit-simple-app/main.py
    ```

## Ejecución del proyecto con consumer y producer

    ```sh
    uvicorn rabbit-multi-app.consumer.main:app --host 0.0.0.0 --port 8000
    uvicorn rabbit-multi-app.producer.main:app --host 0.0.0.0 --port 8001
    ```
    Ir a http://localhost:8001/docs para ver la documentación de la API
    Mandar un mensaje
    Ver el console del consumer para ver el mensaje recibido