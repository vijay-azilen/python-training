books = []

def add_book():
    book_id = int(input("Enter Book ID: "))
    
    for book in books:
        
        if book["id"]==book_id:
            print("Book id already exists.\n")
            return
        
    book = {
        "id":book_id,
        "title":input("Enter Title: " ),
        "author":input("Enter Author: "),
        "category":input("Enter Category: "),
        "available":True
    }
    
    books.append(book)
    
    print("Book added successfully.\n")
    
def view_books():
    if not books:
        print("No books available.\n")
        return
    print("\nLiabrary Books")
    print("-"*80)
    
    for book in books:
        status = "Available" if book["available"] else "Issued"
        
        print(
            f"{book['id']} | "
            f"{book['title']} | "
            f"{book['author']} | "
            f"{status}"            
        )
        
    print()
    
def search_book():
    keyword = input("Enter Book ID or Title : ").lower()
    
    for book in books:
        if (str(book["id"])==keyword or keyword in book["title"].lower()):
            print("\nBook Found:")
            print(f"ID: {book['id']}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print(
                f"Status : {'Available' if book['available'] else 'Issued'}"
            )
            print()
            return
    print("Book not found.\n")
    
def issue_book():
    
    book_id = int(input("Enter Book ID: "))
    
    for book in books:
        if book["id"]==book_id:
            if not book["available"]:
                print("Book is already issued.\n")
                
            book["available"]=False
            print("Book Issued successfully.\n")
            return
    print("Book not found.\n")
    
def return_book():
    book_id = int(input("Enter Book ID: "))
    
    for book in books:
        if book["id"]==book_id:
            if book["available"]:
                print("Book is already available.\n")
                return
            book["available"]=True
            print("Book returned succesfully.\n")
            return
    print("Book not found.\n")

def delete_book():
    book_id = int(input("Enter Book ID: "))
    for book in books:
        if book["id"]==book_id:
            books.remove(book)
            print("Book deleted succesfully.\n")
            return
    print("Book not found.\n")

def main():
    while True:
        print("========== Library Management System ==========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            issue_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            delete_book()

        elif choice == "7":
            print("Thank you for using Library Management System.")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
        
        
        
    
    
    