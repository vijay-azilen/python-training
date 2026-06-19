from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()  # Load environment variables from .env file

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting...")
        break
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    
    assistant_reply = response.choices[0].message.content
    print(f"Assistant: {assistant_reply}")