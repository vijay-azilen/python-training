import json
import os

os.makedirs("data",exist_ok=True)

def save_json(data,filename):
    
    with open(
        f"data/{filename}",
        "w",
        encoding="utf-8"
    ) as file:
        
        json.dump(
            data,
            file,
            indent=4
        )
        
    print("file saved successfully")