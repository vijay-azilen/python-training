import json
import os

from dataclasses import asdict

os.makedirs("output",exist_ok=True)

def save_users(users, filename="users.json"):
    data = [
        asdict(user)
        for user in users
    ]
    
    with open(
        f"output/{filename}",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            data,file,indent=4
        )
        
    print(f"Saved {len(users)} users")