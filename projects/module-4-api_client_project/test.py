import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1",
    timeout=10
)

print("Status:",response.status_code)
print("Content:",response.text)

response.raise_for_status()