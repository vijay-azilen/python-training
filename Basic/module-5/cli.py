import argparse

parser = argparse.ArgumentParser(description="A simple CLI tool")
parser.add_argument("--name", type=str, help="Your name")
parser.add_argument("--environment", type=str, choices=["dev", "prod"], help="Set the environment")

args = parser.parse_args()

if args.name:
    print(f"Hello, {args.name}!")
else:
    print("Hello, World!")
    

if args.environment:
    print(f"Environment set to: {args.environment}")
    
employee: tuple[int, str, float] = (
    101,
    "Vijay",
    75000.50
)

print(employee)

employees: list[dict[str, str]] = [
    {
        "name": "Vijay",
        "department": "IT"
    },
    {
        "name": "Rahul",
        "department": "HR"
    }
]

print(employees[0]["name"])

department: dict[str, list[str]] = {
    "Developers": [
        "Vijay",
        "Rahul"
    ],
    "QA": [
        "Amit",
        "Neha"
    ]
}

print(department["Developers"])
