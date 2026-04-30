from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from loguru import logger
import datetime

class MethodStage(Enum):
    OBSERVATION = "observation"
    HYPOTHESIS = "hypothesis"
    EXPERIMENTATION = "experimentation"
    ANALYSIS = "analysis"
    CONCLUSION = "conclusion"

class ResourceMetrics(BaseModel):
    execution_time_ms: float = 0.0
    cpu_usage_avg: float = 0.0
    memory_peak_mb: float = 0.0
    estimated_cost_usd: float = 0.0

class ScientificExperiment(BaseModel):
    experiment_id: str
    title: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    stage: MethodStage = MethodStage.OBSERVATION
    observations: List[Any] = []
    hypothesis: Optional[str] = None
    experiment_details: Optional[Dict[str, Any]] = None
    results: Optional[Dict[str, Any]] = None
    metrics: ResourceMetrics = Field(default_factory=ResourceMetrics)
    is_successful: bool = False
    is_productive_line: bool = False # Meta: ¿Se puede convertir en una línea productiva?
    efficiency_gain_pct: float = 0.0

class ScientificEngine:
    """
    Orquestador avanzado del método científico para la optimización de procesos y economización de recursos.
    """
    def __init__(self, uae_id: str):
        self.uae_id = uae_id
        self.active_experiments: Dict[str, ScientificExperiment] = {}

    async def start_experiment(self, title: str) -> str:
        import uuid
        exp_id = str(uuid.uuid4())
        experiment = ScientificExperiment(experiment_id=exp_id, title=title)
        self.active_experiments[exp_id] = experiment
        logger.info(f"[{self.uae_id}] Iniciando ciclo científico: {title} ({exp_id})")
        return exp_id

    async def advance_stage(self, experiment_id: str, data: Any = None, metrics: Optional[ResourceMetrics] = None):
        if experiment_id not in self.active_experiments:
            raise ValueError("Experimento no encontrado")
        
        exp = self.active_experiments[experiment_id]
        current = exp.stage
        
        if metrics:
            exp.metrics = metrics

        if current == MethodStage.OBSERVATION:
            exp.stage = MethodStage.HYPOTHESIS
            exp.observations.append(data)
            logger.info(f"Exp {experiment_id}: Observación registrada. Pasando a Hipótesis.")
            
        elif current == MethodStage.HYPOTHESIS:
            exp.stage = MethodStage.EXPERIMENTATION
            exp.hypothesis = str(data)
            logger.info(f"Exp {experiment_id}: Hipótesis formulada. Iniciando Experimentación.")
            
        elif current == MethodStage.EXPERIMENTATION:
            exp.stage = MethodStage.ANALYSIS
            exp.experiment_details = data
            logger.info(f"Exp {experiment_id}: Experimentación completada. Iniciando Análisis.")
            
        elif current == MethodStage.ANALYSIS:
            exp.stage = MethodStage.CONCLUSION
            exp.results = data
            exp.is_successful = data.get("is_optimal", False)
            exp.efficiency_gain_pct = data.get("efficiency_gain", 0.0)
            exp.is_productive_line = exp.is_successful and exp.efficiency_gain_pct > 20.0
            logger.info(f"Exp {experiment_id}: Análisis finalizado. Éxito: {exp.is_successful}, Ganancia: {exp.efficiency_gain_pct}%")
            
        elif current == MethodStage.CONCLUSION:
            logger.warning(f"Exp {experiment_id} ya ha finalizado.")

    def get_productive_lines(self) -> List[ScientificExperiment]:
        """Retorna los experimentos que han resultado en líneas productivas viables."""
        return [exp for exp in self.active_experiments.values() if exp.is_productive_line]
