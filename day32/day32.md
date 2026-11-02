Day 32: Excel Multiplication, Division and Payment Tracking
Objective
Learn how to use multiplication and division formulas in Excel and extend the customer payment tracker.
1. Multiplication Formula
Introduced Quantity and Unit Price columns to the customer payment tracker.
The worksheet structure became:
Customer Name | Item | Quantity | Unit Price | Total Amount | Amount Paid | Balance | Payment Status
Used multiplication to calculate the total cost of items purchased.
Formula:
=Quantity*UnitPrice
Example:
Quantity: 3
Unit Price: ₦2,500
Total Amount: ₦7,500
Excel automatically calculates the total.
2. Division Formula
Learned how to use division to calculate the percentage of an order a customer has paid.
Formula:
=AmountPaid/TotalAmount
Example:
Total Amount: ₦7,500
Amount Paid: ₦5,000
Result: 0.6667
3. Percentage Formatting
Learned that Excel stores percentages as decimal values.
Applying Percentage formatting changes how the value is displayed without changing the underlying stored value.
Example:
Stored value: 0.6667
Percentage display: 67%
4. Fill Handle
Used the fill handle to copy formulas down multiple rows, allowing Excel to automatically adjust cell references for each customer.
Skills You'll Acquire
Excel multiplication and division.
Using formulas with cell references.
Calculating total purchase amounts.
Calculating payment percentages.
Percentage number formatting.
Understanding stored values versus displayed values.
Copying formulas using the fill handle.
Practical Application
Extended the customer payment tracker to calculate:
Total purchase amount based on quantity and unit price.
Amount paid.
Outstanding balance.
Percentage paid.
Payment status.
Conclusion
Learned how Excel formulas can automate business calculations and make customer payment tracking more efficient. Also observe the zero division error handler formular in case total amount=0.