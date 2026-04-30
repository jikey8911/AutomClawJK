import httpx
from loguru import logger
from typing import Any, Dict, Optional

class OpenClawClient:
    """
    Client to interact with the OpenClaw Gateway.
    """
    def __init__(self, base_url: str = "http://openclaw:5000"):
        self.base_url = base_url

    async def send_message(self, agent_id: str, message: str, session_id: Optional[str] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/v1/messages"
        payload = {
            "agent_id": agent_id,
            "content": message,
            "session_id": session_id
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, timeout=60.0)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.error(f"Error communicating with OpenClaw: {e}")
                raise

    async def spawn_session(self, agent_id: str, task: str) -> str:
        url = f"{self.base_url}/v1/sessions/spawn"
        payload = {
            "agent_id": agent_id,
            "task": task
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, timeout=30.0)
                response.raise_for_status()
                return response.json().get("session_id")
            except Exception as e:
                logger.error(f"Error spawning OpenClaw session: {e}")
                raise
