Day 14  Modules and Imports

 Why split code across multiple files?

It is useful to split code across multiple files because it keeps a program organized and easier to understand.

For example, I put calculate_late_fee()and describe_book() inside library_helpers.py and then imported them into main.py.

If I copied both functions directly into main.py, the file would contain both the main program logic and the helper functions. As the project becomes bigger, this would make main.py longer, harder to read, and harder to maintain.

By separating the functions into library_helpers.py, I can keep related helper functions together and reuse them in other Python files by importing them.

This also makes it easier to find and modify a function without searching through one large file.
I learnt 
A Python file can be used as a module.
I can import functions from another Python file.
Splitting code into modules makes programs more organized.
Functions in a separate module can be reused instead of being copied and pasted.
I tested calculate_late_fee(20, 5)and got 100.
I also tested describe_book() with both available=True and available=False.