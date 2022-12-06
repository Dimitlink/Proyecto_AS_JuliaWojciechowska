#Paso 1: Descarga de imagen base
# Imagen base
FROM python:latest

#Paso 2: Preparación de la imagen
# Descarga  de la libería de python de orientDB
RUN pip install pyorient
#Copiado del script
COPY main.py .
#Creación de carpeta db
RUN mkdir db

#Paso 3: Ejecución del script
CMD ["python", "./main.py"]

