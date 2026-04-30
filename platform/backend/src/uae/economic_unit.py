from src.uae.base_uae import BaseUAE
from src.scientific_method.engine import ScientificEngine, MethodStage
from src.core.openclaw_client import OpenClawClient
from loguru import logger
from typing import Any
import os

class EconomicOptimizationUnit(BaseUAE):
    """
    UAE especializada en la optimización económica y financiera.
    Utiliza el método científico para encontrar procesos rentables.
    """
    def __init__(self, name: str):
        super().__init__(name=name, sector="General Economics & Automation")
        self.engine = ScientificEngine(uae_id=self.agent_id)
        openclaw_url = os.getenv("OPENCLAW_URL", "http://openclaw:5000")
        self.claw_client = OpenClawClient(base_url=openclaw_url)

    async def evaluate_sector(self) -> Any:
        logger.info(f"[{self.name}] Solicitando análisis de mercado a OpenClaw...")
        
        # Le pedimos al agente 'researcher' de OpenClaw que busque sectores de alto crecimiento
        prompt = "Identifica 3 sectores económicos emergentes con alto potencial de automatización y crecimiento financiero en 2026."
        
        try:
            # Iniciamos una sesión de investigación
            session_id = await self.claw_client.spawn_session(agent_id="researcher", task=prompt)
            logger.info(f"Sesión de investigación iniciada: {session_id}")
            
            # En un sistema real, esperaríamos el resultado de la sesión. 
            # Por ahora, simulamos la recepción de datos estructurados basados en el prompt.
            opportunities = [
                {"sector": "AI-Driven Micro-SaaS", "efficiency": 0.5, "potential_growth": 0.95},
                {"sector": "Automated Logistics for Vertical Farming", "efficiency": 0.3, "potential_growth": 0.85}
            ]
            return opportunities
        except Exception as e:
            logger.error(f"Error en la evaluación del sector: {e}")
            return []

    async def formulate_hypothesis(self, observation: Any) -> Any:
        if not observation:
            return {"error": "No observations found"}

        sector = observation[0]["sector"]
        hypothesis = f"Implementar una línea de producción auto-generada para {sector} reducirá el tiempo de despliegue en un 50%."
        
        # Registrar en el motor científico
        exp_id = await self.engine.start_experiment(f"Optimización de {sector}")
        await self.engine.advance_stage(exp_id, new_data=observation)
        await self.engine.advance_stage(exp_id, new_data=hypothesis)
        
        # Enviar la hipótesis al Orchestrator de OpenClaw para validación experimental
        try:
            await self.claw_client.send_message(
                agent_id="orchestrator", 
                message=f"Inicia validación experimental para la hipótesis: {hypothesis}"
            )
        except Exception as e:
            logger.error(f"Error enviando hipótesis al Orchestrator: {e}")

        return {"experiment_id": exp_id, "hypothesis": hypothesis}

    async def process(self, input_data: Any) -> Any:
        # Ciclo principal de la UAE
        observations = await self.evaluate_sector()
        result = await self.formulate_hypothesis(observations)
        return result
