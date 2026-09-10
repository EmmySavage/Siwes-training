try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero!")

try:
    number = int("abc")
except ValueError:
    print("That's not a valid number!")
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("That position doesn't exist in the list!")
except ZeroDivisionError:
    print("You can't divide by zero!")
def safe_divide(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return "cannot divide by zero"
print(safe_divide(10,2))
print(safe_divide(10,0))
library = [
    {"title": "1984", "author": "George Orwell", "available": True},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "available": False},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "available": True},
    {"title": "Dune", "author": "Frank Herbert", "available": False},
]
def get_book_by_index(library,index):
    try:
        return library [index]["title"]
    except IndexError:
        return "An invalid position"
print(get_book_by_index(library, 1))
print(get_book_by_index(library, 10))
'''
return library [index],["title"]
mistakenly added a comma and it changed my output.
This-> ({'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'available': False}, ['title'])
instead of just-> To Kill a Mockingbird
'''
