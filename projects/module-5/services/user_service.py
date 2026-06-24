import asyncio
import aiohttp


from api.user_client import UserClient

class UserService:
    
    def __init__(self):
        
        self.client = UserClient()
        
    async def fetch_users(
        self,
        user_ids:list[int]
    ):
        async with aiohttp.ClientSession() as session:
            
            tasks = [
                self.client.fetch_user(
                    session,
                    user_id
                )
                
                for user_id in user_ids
            ]
            
            #print(tasks.join(",")])
            
            
            users = await asyncio.gather(
                *tasks
            )
            
            return [
                user 
                for user in users
                if user
            ]
