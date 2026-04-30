from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from pydantic import BaseModel
import uuid

class AgentState(BaseModel):
    agent_id: str
    status: str = "idle"
    current_task: Optional[str] = None
    memory: Dict[str, Any] = {}

class BaseAgent(ABC):
    """
    Clase base para todos los agentes del sistema AutomClawJK.
    """
    def __init__(self, name: str, role: str):
        self.agent_id = str(uuid.uuid4())
        self.name = name
        self.role = role
        self.state = AgentState(agent_id=self.agent_id)

    @abstractmethod
    async def process(self, input_data: Any) -> Any:
        """
        Lógica principal de procesamiento del agente.
        """
        pass

    def update_state(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self.state, key):
                setattr(self.state, key, value)
            else:
                self.state.memory[key] = value

    def __repr__(self):
        return f"<{self.role} Agent: {self.name} ({self.agent_id})>"
