def apply_discount(price,discount_percent=10):
    discount_amount = price * (discount_percent /100 )
    final_price = price - discount_amount
    return final_price
#overriding the default percent value
result = apply_discount(5000,20)
print (result)
def calculate_late_fee(days_late, fee_per_day=50):
    if days_late <=0:
        #if days late is 0 the functions stop.. second line never runs
        return 0
    #if it is false python skips it and run return line
    return days_late * fee_per_day
#using default fee(arguement)  
result1 = calculate_late_fee(10)
print(result1)
#less than 0 days
result2 = calculate_late_fee(-5)
print(result2)
#using  both arguement 
result3 = calculate_late_fee(10,100)
print (result3)
#using both arguements in keywords and reversed manners  
result4 = calculate_late_fee(fee_per_day=100,days_late=10)
print(result4)
def describe_book(title,author,available=True):
    if available:
        return f"{title} by {author} is currently available"
    else :
        return  f"{title} by {author} is currently not available"
print (describe_book ("Things Fall Apart","Chinua Achebe"))
print (describe_book ("Things Fall Apart","Chinua Achebe", False))