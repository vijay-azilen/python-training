from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent


load_dotenv()


@tool

def calculator(a:float,b:float) -> str:
    """useful for performing basic arithmetic calculations with numbers"""
    print("tool has been called")
    return f"The sum of {a} and {b} is {a + b}"

    


def main():
    #model = ChatOpenAI(temperature=0)
    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
        )
    
    tools = [calculator]
    
    agent_executer = create_agent(model, tools)
    
    print("Welcome! I'm your AI assitant. Type 'quit' to exit.")
    print("You can ask me to perform calculation or chat with me.")
    
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input=="quit":
            break
        
        response = agent_executer.invoke(
            {"messages": [HumanMessage(content=user_input)]}
        )

        print("\nAssistant:", response["messages"][-1].content)              
                
        print()
        
if __name__=="__main__":
    main()