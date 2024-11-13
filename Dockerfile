# Usa la imagen oficial de Python 3.12
FROM python:3.12-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt y las dependencias
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de tu proyecto al contenedor
COPY . /app

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 80

# Comando para iniciar el servidor de desarrollo de Django en el puerto 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
