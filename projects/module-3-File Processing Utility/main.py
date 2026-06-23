from file_processor import (
    read_text_file,
    count_lines,
    count_words,
    count_characters,
    search_word    
)

from csv_converter import csv_to_json

def text_file_analysis():
    
    filename = input("Enter text file path: ")
    
    content = read_text_file(filename)
    
    if not content:
        return
    
    print("\nFile statistics")
    print("-"*30)
    
    print("Lines        :",count_lines(content))
    print("Words        :",count_words(content))
    print("Character    :",count_characters(content))
    
    word = input("\nEnter word to search: ")
    
    if search_word(content,word):
        print(f"'{word}' found.")        
    else:
        print(f"{word} not found.")

def convert_csv():

    csv_file = input("Enter CSV file path: ")
    json_file = input("Enter JSON output path: ")

    csv_to_json(csv_file, json_file)


def main():
    
    while True:
        
        print("\n=== File Processing Utitlity ===")
        print("1. Aanlyze Text file")
        print("2. Convert CSV to JSON")
        print("3. Exit")
        choice = input("Select option: ")

        if choice == "1":
            text_file_analysis()

        elif choice == "2":
            convert_csv()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
    
    