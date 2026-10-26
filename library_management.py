books = []

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter book ID: ")
        name = input("Enter book name: ")
        author = input("Enter author name: ")

        book = {
            "id": book_id,
            "name": name,
            "author": author,
            "status": "Available"
        }

        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print("\n--- Available Books ---")

            for book in books:
                print("Book ID:", book["id"])
                print("Book Name:", book["name"])
                print("Author:", book["author"])
                print("Status:", book["status"])
                print("----------------------")

    elif choice == "3":
        search_id = input("Enter book ID to search: ")
        found = False

        for book in books:
            if book["id"] == search_id:
                print("Book Found!")
                print("Name:", book["name"])
                print("Author:", book["author"])
                print("Status:", book["status"])
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == "4":
        issue_id = input("Enter book ID to issue: ")
        found = False

        for book in books:
            if book["id"] == issue_id:
                found = True

                if book["status"] == "Available":
                    book["status"] = "Issued"
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")

                break

        if not found:
            print("Book not found.")

    elif choice == "5":
        return_id = input("Enter book ID to return: ")
        found = False

        for book in books:
            if book["id"] == return_id:
                found = True

                if book["status"] == "Issued":
                    book["status"] = "Available"
                    print("Book returned successfully!")
                else:
                    print("This book was not issued.")

                break

        if not found:
            print("Book not found.")

    elif choice == "6":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
