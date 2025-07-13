monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total monthly expense: "))

#Calculating monthly savings 
monthly_savings =  monthly_income - monthly_expense

#Calculating annual projected savnigs 
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#printing results 
print("Your monthly savings are $",monthly_savings,".")

print("Projected savings after one year, with interest, is: $",projected_savings)