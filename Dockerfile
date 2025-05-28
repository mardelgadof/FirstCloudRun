# This Dockerfile is used to define the environment and instructions
# for building a Docker image. It specifies the base image, copies
# necessary files, installs dependencies, and configures the container
# to run the desired application or service.
"""
This Dockerfile is used to build a Docker image for a Python application.
Aquí:
    - especifico la imagen base
    - copio los archivos necesarios
    - instalo dependencias
    - configuro el contenedor para ejecutar la aplicación o servicio deseado


"""

# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim 
#esta version de python es una muy liviana para que se pueda utilizar
#en TI hay reglas para descargar imágenes.


# Copy local code to the container image.
#definimos una var de ambiente de nombre APP_HOME
ENV APP_HOME /app
# toma como work directory o work space la variable de entorno
WORKDIR $APP_HOME
#que copie todo de la raiz de nosotros a la raiz del contenedor
COPY . ./
# que copie el requirements.txt al contenedor también
COPY requirements.txt ./



# Install production dependencies.
#correremos el requirements.txt en un contenedor
RUN pip install -r requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.

#con esto despliega ese container utilizando una librería de nombre gunicorn
#gunicorn es un servidor WSGI para aplicaciones; 
#maneja voluen alto de peticiones
#el rendimiento de aplicaciones web en Python.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
