import aiohttp

from models.user import User

class UserClient:
    BASE_URL = ("https://jsonplaceholder.typicode.com")
    
    async def fetch_user(
        self,
        session,
        user_id:int
    )->User | None:
        url = f"{self.BASE_URL}/users/{user_id}"
        
        try:
            
            async with session.get(url) as response:
                
                if response.status != 200:
                    print(f"User {user_id} not found")
                    return None
                
                data = await response.json()
                
                return User(
                    id=data["id"],
                    name=data["name"],
                    username=data["username"],
                    email=data["email"]
                )
        except Exception as e:
            
            print(e)
            
            return None
        
                
                