# Imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos al contenedor
COPY . /app

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
