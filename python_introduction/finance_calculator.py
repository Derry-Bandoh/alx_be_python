monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expense: "))

#Calculating monthly savings 
monthly_savings =  monthly_income - monthly_expenses

#Calculating annual projected savnigs 
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#printing results 
print(f"Your monthly savings are ${monthly_savings}.")

print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")