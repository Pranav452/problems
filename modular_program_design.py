books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "genre": "Fiction",
        "rating": 4.5
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genre": "Dystopian",
        "rating": 4.0
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "genre": "Southern Gothic",
        "rating": 4.8
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813,
        "genre": "Romance",
        "rating": 4.7
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951,
        "genre": "Coming-of-age",
        "rating": 4.2
    }
]
def add_book(title,author,year,genre,rating):
    books.append({"title":title,"author":author,"year":year,"genre":genre,"rating":rating})

def search_book(query):
    for book in books:
        if query in book["title"] or query in book["author"] or query in book["year"] or query in book["genre"] or query in book["rating"]:
            return book
    return None
def display_inventory():
    for book in books:
        print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - Rating: {book['rating']}")

def main():
    while True:
        print("1. Add Book")
        print("2. Search Book")
        print("3. Display Inventory")
        print("4. Exit") 
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            genre = input("Enter genre: ")
            rating = input("Enter rating: ")
            add_book(title,author,year,genre,rating)
        elif choice == "2":
            query = input("Enter search query: ")
            book = search_book(query)
            if book:
                print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - Rating: {book['rating']}")
            else:
                print("Book not found")
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            break
        else:
            print("Invalid choice")
            continue
        print("--------------------------------")

if __name__ == "__main__":
    main()