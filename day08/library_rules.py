
age = 19

if age >= 18:
    print("You can register for a library card")
elif age >= 13:
    print("You need a guardian approval")
else:
    print("Too young to register")
    
def can_borrow (is_available,has_outstanding_fine):
    if not is_available:
        return "cannot borrow: book unavailable"
    elif has_outstanding_fine:
        return "cannot borrow: outstanding fine"
    else:
        return "book can be borrowed"
print (can_borrow(False,False))
print (can_borrow(True,True))
print (can_borrow(True,False))