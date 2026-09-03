#List operations
books = ["Things Fall Apart","Chike and the river"]
books.append("1984")
books.remove("Chike and the river")
books[0]
len (books)
"1984" in books
#dictionary operations
book = {"title": "1984", "author": "George Orwell", "available": True}
book["title"]                  # access by key → "1984"
book["available"] = False      # update a value
book["year"] = 1949            # add a new key
book.get("genre", "Unknown")   # safe access — returns "Unknown" if key doesn't exist (no crash)
# List of dictionaries representing books
library = [
    {"title": "1984", "author": "George Orwell", "available": True},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "available": False},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "available": True},
    {"title": "Dune", "author": "Frank Herbert", "available": False},
]

# Print titles of available books
print("Available books:")
for book in library:
    if book["available"]:
        print(book["title"])

#find_book function
def find_book(library, title):
    for book in library:
        if book["title"] == title:
            return book
    return "Book not found"

print(find_book(library, "Dune"))          # exists
print(find_book(library, "Moby Dick"))     # doesn't exist

#Add "year" key to one book
library[0]["year"] = 1949
print(library[0])
book = {"title": "Dune", "author": "Frank Herbert", "available": False}

#book["year"]        # KeyError: 'year'
book.get("year")     # None — no crash
book.get("year", "Unknown")  # "Unknown" — custom fallback
for book in library:
    print(book.get("year", "Year unknown"))
