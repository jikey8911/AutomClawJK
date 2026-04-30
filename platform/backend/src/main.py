from fastapi import FastAPI
from src.uae.economic_unit import EconomicOptimizationUnit
from src.core.openclaw_bridge import OpenClawBridge
import os

app = FastAPI(title="AutomClawJK API", description="Sistema Multiagéntico de Optimización de Procesos")

# Inicialización de componentes (Configuración básica)
OPENCLAW_PATH = os.getenv("OPENCLAW_PATH", "../../openclaw")
bridge = OpenClawBridge(OPENCLAW_PATH)
master_uae = EconomicOptimizationUnit(name="Alpha-Strategist")

@app.get("/")
async def root():
    return {
        "status": "online",
        "system": "AutomClawJK",
        "version": "0.1.0",
        "master_uae": master_uae.name,
        "sector": master_uae.sector
    }

@app.get("/status/experiments")
async def get_experiments():
    return master_uae.engine.active_experiments

@app.post("/trigger/optimization")
async def trigger_optimization():
    result = await master_uae.process(None)
    return {"message": "Optimización iniciada", "result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
