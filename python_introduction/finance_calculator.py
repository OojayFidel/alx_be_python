# Personal Finance Calculator

# Get user's monthly income
monthly_income = int(input("Enter your monthly income:"))

# Get user's total monthly expenses
monthly_expenses = int(input("Enter your total monthly expenses:"))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

annual_interest_rate = 0.05

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")