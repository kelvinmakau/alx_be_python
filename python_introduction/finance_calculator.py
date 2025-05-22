income = input("Enter your monthly income: ")
expenses = input("Enter your total monthly expenses: ")
savings = float(income) - float(expenses)
annual_savings = savings * 12 + (savings * 12 * 0.05)

print("Your monthly savings are $" + str(savings))
print("Projected savings after one year, with interest, is: $" + str(annual_savings))