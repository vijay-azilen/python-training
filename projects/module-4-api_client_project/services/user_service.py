from api.api_client import APIClient

client = APIClient()

class UserService:
    
    def get_user(self,user_id):
        
        return client.get(
            f"users/{user_id}"
        )
        
    def get_users(self):
        
        return client.get(
            "users"            
        )
        
    def create_user(self, data):
        return client.post(
            "users",
            data
        )
        
    def update_user(self,user_id,data):
        return client.put(
            f"users/{user_id}",
            data
        )
    
    def delete_user(self, user_id):
        return client.delete(
            f"users/{user_id}"
        )
    