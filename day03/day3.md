Debugging a python function and learning how to read error  to narrow down to the exact line of code the bug or error was made.
 Reviewed a python a function that calculates average lists of numbers,ran the program and encountered a ZerodivisionError,when dividing zero by zero. Read the error it produced and traced it back to the line it happened and the event that triggered the error.
Corrected it by using -if len(numbers) == 0:
        return "No scores to average"
The fix works by checking whether the list is empty before attempting the division. If it is, the function returns early with a message, so the division line is never reached avoiding the ZeroDivisionError entirely.