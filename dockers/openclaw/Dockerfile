FROM node:22-slim

WORKDIR /app

# Instalar dependencias del sistema, incluyendo Python y herramientas de compilación
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    git \
    python3 \
    python3-pip \
    python3-venv \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instalar OpenClaw globalmente usando el nombre correcto del paquete
RUN npm install -g openclaw@latest

# Copiar el contenido del directorio openclaw
COPY ./openclaw /app/openclaw

WORKDIR /app/openclaw

# Instalar dependencias de Python si existe el archivo requirements.txt
RUN if [ -f requirements.txt ]; then \
    pip3 install --no-cache-dir -r requirements.txt --break-system-packages || true; \
    fi

# Exponer el puerto del gateway
EXPOSE 5000

# Comando para iniciar el gateway de OpenClaw
# Usamos 'openclaw gateway start' como indica la documentación
CMD [ "gateway", "start" ]
