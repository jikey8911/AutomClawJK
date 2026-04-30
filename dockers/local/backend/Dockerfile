FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar dependencias
COPY platform/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY platform/backend /app

# Exponer puerto para la API
EXPOSE 8000

# Comando por defecto (apuntando a src.main:app)
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
