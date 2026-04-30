FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema para scraping/browser
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Copiar dependencias de OpenClaw
COPY openclaw/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY ./openclaw /app/openclaw

# Comando por defecto para iniciar el gateway de OpenClaw
CMD ["python", "-m", "openclaw.gateway"]
