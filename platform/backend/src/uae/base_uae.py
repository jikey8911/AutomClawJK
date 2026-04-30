from src.core.agent import BaseAgent
from abc import abstractmethod
from typing import List, Any

class BaseUAE(BaseAgent):
    """
    Unidad Autónoma Estratégica (UAE).
    Agente de alto nivel encargado de la toma de decisiones estratégicas,
    identificación de sectores y optimización de procesos mediante el método científico.
    """
    def __init__(self, name: str, sector: str):
        super().__init__(name=name, role="Strategic Unit")
        self.sector = sector
        self.subordinates: List[BaseAgent] = []

    def assign_subordinate(self, agent: BaseAgent):
        self.subordinates.append(agent)

    @abstractmethod
    async def evaluate_sector(self) -> Any:
        """
        Analiza el sector económico asignado para encontrar oportunidades de optimización.
        """
        pass

    @abstractmethod
    async def formulate_hypothesis(self, observation: Any) -> Any:
        """
        Aplica el método científico para proponer una mejora o nuevo proceso.
        """
        pass
