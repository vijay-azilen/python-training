import csv
import json

def csv_to_json(csv_file,json_file):
    data=[]    
    try:
        with open(csv_file,mode="r",encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                data.append(row)
        
        with open(json_file,mode="w",encoding="utf-8") as file:
            json.dump(data,file,indent=4)
                
        print(f"JSON file created : {json_file}")
                
    except Exception as e:
        print("Error: ", e)