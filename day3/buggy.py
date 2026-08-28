def calculate_average(numbers):
    '''
    Calculates the average of a list of numbers.
    Returns a message instead of crashing if the list is empty.
    '''
    #returns early to avoid dividing by zero on an empty set
    if len(numbers) == 0:
        return "no scores to average"
    total = 0
    for n in numbers:
        total = total + n
    average = total / len(numbers)
    return average

scores = [80, 90, 70, 100]
print("Average score:", calculate_average(scores))

empty_list = []
print("Average of empty list:", calculate_average(empty_list))