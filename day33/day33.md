Day 33 – Excel Functions
What I Learned
Today, I learned how to use Excel functions to perform calculations and analyse data without calculating everything manually.
I practised the following functions:
1. SUM()
The SUM() function adds numbers together.
Syntax:
=SUM(range)
Example:
=SUM(G2:G6)
This adds all the values from cells G2 to G6.
Use case: Calculating the total outstanding balance owed by customers.
2. AVERAGE()
The AVERAGE() function calculates the arithmetic mean of a group of numbers.
Syntax:
=AVERAGE(range)
Example:
=AVERAGE(G2:G6)
This calculates the average balance across the selected cells.
Important: Excel ignores blank cells but includes zero when calculating the average.
3. MIN()
The MIN() function returns the smallest numerical value in a range.
Example:
=MIN(G2:G6)
This finds the smallest customer balance.
4. MAX()
The MAX() function returns the largest numerical value in a range.
Example:
=MAX(G2:G6)
This identifies the highest customer balance.
5. COUNT()
The COUNT() function counts cells containing numbers.
Example:
=COUNT(G2:G6)
This counts how many cells in the selected range contain numerical values.
Important: It does not count cells containing only text.
6. COUNTA()
The COUNTA() function counts all non-empty cells, whether they contain text or numbers.
Example:
=COUNTA(A2:A6)
This counts the customer names entered in cells A2 to A6.
Practical Application
I applied these functions to a customer payment tracker for a small business.
My worksheet contains:
Customer Name
Item
Quantity
Unit Price
Total Amount
Amount Paid
Balance
Percentage
Payment Status
I can use these functions to analyse customer payments, identify outstanding balances, and calculate payment statistics.
Key Difference Between COUNT() and COUNTA()
Function
What it counts
COUNT()
Cells containing numbers
COUNTA()
All non-empty cells
What I Understand Now
SUM() adds values.
AVERAGE() calculates the average.
MIN() finds the smallest value.
MAX() finds the largest value.
COUNT() counts numerical cells.
COUNTA() counts non-empty cells.
These functions make it easier to summarise and analyse spreadsheet data.