# Question 7: Menu-driven CRUD operations on a list of books.
books = []

def add_book():
    books.append({
        "book_id": input("Book ID: ").strip(),
        "title": input("Title: ").strip(),
        "author": input("Author: ").strip(),
    })
    print("Book added.")

def view_books():
    if not books:
        print("No books available.")
    for book in books:
        print(book)

def update_book():
    book_id = input("Book ID to update: ").strip()
    for book in books:
        if book["book_id"] == book_id:
            book["title"] = input("New title: ").strip()
            book["author"] = input("New author: ").strip()
            print("Book updated.")
            return
    print("Book not found.")

def delete_book():
    book_id = input("Book ID to delete: ").strip()
    for index, book in enumerate(books):
        if book["book_id"] == book_id:
            books.pop(index)
            print("Book deleted.")
            return
    print("Book not found.")

while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        update_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
