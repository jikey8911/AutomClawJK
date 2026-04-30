FROM python:3.11-slim

WORKDIR /app

# Copiar dependencias
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY ./platform/backend /app

# Exponer puerto para la API
EXPOSE 8000

# Comando por defecto
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
