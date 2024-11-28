import requests
from typing import Dict, Any
#from config import Config

class OllamaService:
    def __init__(self, host: str):
        self.host = host
        
    async def generate_response(self, prompt: str, model: str = "mistral") -> Dict[str, Any]:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = requests.post(
            f'{self.host}/api/generate',
            json={
                'model': model,
                'prompt': prompt,
                'stream': False
            },
            headers=headers,
            timeout=30
        )
        
        if response.status_code != 200:
            raise Exception(f"Ollama error (Status {response.status_code}): {response.text}")
            
        return response.json() 