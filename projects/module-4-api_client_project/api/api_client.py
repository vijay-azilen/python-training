import requests
import time

from config.settings import(
    BASE_URL,
    REQUEST_TIMEOUT
)

MAX_RETRIES = 3

from utils.logger import logger

class APIClient:
    def request(
        self,
        method,
        endpoint,
        payload=None
    ):
        
        url = f"{BASE_URL}/{endpoint}"
        
        for attempt in range(MAX_RETRIES):
            try:
                response = requests.request(
                    method=method,
                    url=url,
                    json=payload,
                    timeout=REQUEST_TIMEOUT
                )

                response.raise_for_status()
                
                if response.text:
                    return response.json()
                
                return{}
            except requests.exceptions.RequestException as e:
                print(
                    f"Retry {attempt+1}/{MAX_RETRIES}"
                    f"Error: {e}"
                )
                
                if (attempt==MAX_RETRIES-1):
                    raise
                
                time.sleep(2)
    def get(self,endpoint):
        return self.request("GET",endpoint)
    
    def post(self,endpoint,payload):
        return self.request(
            "POST",
            endpoint,
            payload
        )

    def put(self,endpoint,payload):
        return self.request(
            "PUT",
            endpoint,
            payload
        )
        
    def delete(self,endpoint):
        return self.request(
            "DELETE",
            endpoint
        )
        
