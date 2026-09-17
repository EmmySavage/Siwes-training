
book =[
    "Things Fall Apart",
    "The Hobbit",
    "Animal Farm"
]
for books in book:
    
    print (book)
    for i in range (5):
        print (i)

books =[
    "Take me home",
    "Sugar Girl",
    "Tempest"
]
#print each book with its position
for position, book in enumerate(books,start=1):
    print (position,book)
#pay a #1000 fine in #250 weekly installment
balance = 1000
payment = 250 
week = 1
while balance >0:
    balance = balance - payment
    print("week",week,"Remaining balance:",balance)
    week = week + 1
for book in books:
    if book =="Sugar Girl":
        print("Found It")
        break