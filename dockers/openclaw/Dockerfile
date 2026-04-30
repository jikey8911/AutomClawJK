FROM node:22-slim

WORKDIR /app

# Instalar dependencias del sistema para el navegador y herramientas
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    git \
    python3 \
    make \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Instalar pnpm
RUN npm install -g pnpm

# Instalar OpenClaw globalmente o localmente
RUN npm install -g @openclaw/gateway @openclaw/cli

# Copiar configuración y agentes
COPY ./openclaw /app/openclaw

WORKDIR /app/openclaw

# Exponer el puerto del gateway
EXPOSE 5000

# Comando para iniciar el gateway usando la configuración local
CMD ["openclaw", "gateway", "start", "--config", "openclaw.json"]
