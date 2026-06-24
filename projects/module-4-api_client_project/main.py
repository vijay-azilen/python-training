from services.user_service import UserService
from utils.file_helper import save_json


service = UserService()

def get_user():
    user_id = input("Enter User ID: ")
    
    user = service.get_user(user_id)
    
    print(user)
    
def get_all_user():
    
    users = service.get_users()
    
    print(f"Total users: {len(users)}")
    
    for user in users:
        print(
            user["id"],
            user["name"]
        )
        
    save = input("Save to file? (y/n): ")
    
    if save.lower()=='y':
        save_json(users,"users.json")
        
def create_user():
    name = input("Name: ")
    email = input("Email: ")
    
    payload = {
        "name":name,
        "email":email
    }
    
    response = service.create_user(
        payload
    )
    
    print(response)
    
def update_user():
    user_id = input("User ID: ")
    name = input("New User Name: ")
    payload = {"name":name}
    
    response = service.update_user(user_id,payload)
    
    print(response)
    
def delete_user():
    user_id = input("User ID: ")
    
    response = service.delete_user(user_id)
    
    print("Delete")
    
    print(response)
    
def menu():
    while True:
        
        print("\n")
        print("=" * 40)
        print("API CLI APPLICATION")
        print("=" * 40)
        
        print("1. Get User")
        print("2. Get All Users")
        print("3. Create User")
        print("4. Update User")
        print("5. Delete User")
        print("6. Exit")
        
        choise = input("Select Option:")
        
        try:
            if choise == "1":
                get_user()
                
            elif choise == "2":
                get_all_user()
                
            elif choise == "3":
                create_user()
                
            elif choise == "4":
                update_user()
                
            elif choise == "5":
                delete_user()
                
            elif choise=="6":
                print("Goodbye")
                break
            
            else:
                print("Invalid choice")
                
        except Exception as e:
            
            print("Error:",e)
            
if __name__ == "__main__":
    menu()