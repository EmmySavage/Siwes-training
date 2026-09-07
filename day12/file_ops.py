#writing to a file
'''
with open("notes.txt","w") as f:
    f.write("Hello, This is Day 12.\n")
    f.write("Learning file handling.\n")
# Reading a file
with open("notes.txt, (r)") as f:
    content = f.read()
    print(content)
#reading line by line
with open("notes.txt, (r)") as f:
    for line in f:
        print(line.strip())
        '''
with open("books_list.txt","w") as file:
    file.write("Things Fall Apart.\n")
    file.write("The Hobbit.\n")
    file.write("Animal Farm.\n")
    file.write("lion & the liar.\n")
with open ("books_list.txt","r") as file:
    books = file.readlines()
for number, book in enumerate(books,start=1):
    print(number, book.strip())
print("End of the first of list books")
#adding another book without deleting existing books
with open("books_list.txt","a") as file:
    file.write("Otello.\n")
# checking to see all 5 books
with open ("books_list.txt","r") as file:
    books = file.readlines()
    for number, book in enumerate(books,start=1):
     print(number, book.strip())
