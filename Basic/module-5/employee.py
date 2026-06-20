import argparse


parser = argparse.ArgumentParser(description="Employee Management CLI")
parser.add_argument("--add", action="store_true", help="Add a new employee")

parser.add_argument("--name", type=str, help="Employee's name")
parser.add_argument("--age", type=int, help="Employee's age")

args = parser.parse_args()

if args.add:
    if args.name and args.age:
        print(f"Adding employee: {args.name}, Age: {args.age}")
    else:
        print("Please provide both name and age to add a new employee.")
