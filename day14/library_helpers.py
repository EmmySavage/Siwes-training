def calculate_late_fee(days_late, fee_per_day=50):
    if days_late <=0:
        #if days late is 0 the functions stop.. second line never runs
        return 0
    #if it is false python skips it and run return line
    return days_late * fee_per_day
def describe_book(title,author,available=True):
    if available:
        return f"{title} by {author} is currently available"
    else :
        return  f"{title} by {author} is currently not available"
