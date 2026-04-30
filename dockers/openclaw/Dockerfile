FROM python:3.11-slim

WORKDIR /app

# Copiar dependencias (asumiendo que existirá un requirements.txt en el futuro)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY ./openclaw /app/openclaw

# Comando por defecto (a ajustar según el entrypoint de OpenClaw)
CMD ["python", "-m", "openclaw"]
