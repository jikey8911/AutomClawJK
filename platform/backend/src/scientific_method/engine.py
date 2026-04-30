from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from loguru import logger

class MethodStage(Enum):
    OBSERVATION = "observation"
    HYPOTHESIS = "hypothesis"
    EXPERIMENTATION = "experimentation"
    ANALYSIS = "analysis"
    CONCLUSION = "conclusion"

class ScientificExperiment(BaseModel):
    experiment_id: str
    title: str
    stage: MethodStage = MethodStage.OBSERVATION
    data_points: List[Any] = []
    hypothesis: Optional[str] = None
    results: Optional[Dict[str, Any]] = None
    is_successful: bool = False

class ScientificEngine:
    """
    Orquestador del método científico para la optimización de procesos.
    """
    def __init__(self, uae_id: str):
        self.uae_id = uae_id
        self.active_experiments: Dict[str, ScientificExperiment] = {}

    async def start_experiment(self, title: str) -> str:
        import uuid
        exp_id = str(uuid.uuid4())
        experiment = ScientificExperiment(experiment_id=exp_id, title=title)
        self.active_experiments[exp_id] = experiment
        logger.info(f"Iniciando experimento: {title} ({exp_id})")
        return exp_id

    async def advance_stage(self, experiment_id: str, new_data: Any = None):
        if experiment_id not in self.active_experiments:
            raise ValueError("Experimento no encontrado")
        
        exp = self.active_experiments[experiment_id]
        current = exp.stage
        
        if current == MethodStage.OBSERVATION:
            exp.stage = MethodStage.HYPOTHESIS
            exp.data_points.append(new_data)
        elif current == MethodStage.HYPOTHESIS:
            exp.stage = MethodStage.EXPERIMENTATION
            exp.hypothesis = str(new_data)
        elif current == MethodStage.EXPERIMENTATION:
            exp.stage = MethodStage.ANALYSIS
            exp.results = new_data
        elif current == MethodStage.ANALYSIS:
            exp.stage = MethodStage.CONCLUSION
            exp.is_successful = new_data.get("is_optimal", False)
            
        logger.info(f"Experimento {experiment_id} avanzado a etapa: {exp.stage.value}")
