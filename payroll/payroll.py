# these rates are fictional (only loosely based on actual rates of 2013)
INCOME_TAX_RATE = 0.21
WEEKLY_EI_DEDUCTION = 120.00
WEEKLY_CP_DEDUCTION = 155.00

# input
salaryString = input("Enter the employee's yearly salary: ")

# determine salary for two week period
# Convert the str input to float
salary = float(salaryString) / 26

# processing
# Added str() to fix the concatenation issues
incomeTax = salary * INCOME_TAX_RATE
print("Bi-Weekly Income Tax Deduction: $" + str(incomeTax))
eiDeduction = WEEKLY_EI_DEDUCTION * 2
print("Bi-Weekly EI Deduction: $" + str(eiDeduction))
cpDeduction = WEEKLY_CP_DEDUCTION * 2
print("Bi-Weekly CP Deduction: $" + str(cpDeduction))

totalWithholding = incomeTax + eiDeduction + cpDeduction
takeHomePay = salary - totalWithholding


# output, added str() to fix concat issues, added round()
print("Bi-Weekly Total money withholding: $" + str(round(totalWithholding,2)))
print("Bi-Weekly Take-Home Pay: $" + str(round(takeHomePay,2)))

# output when trailing 0 needs to be displayed
# print(f"Bi-Weekly Total money withholding: ${totalWithholding:.2f}")
# print(f"Bi-Weekly Take-Home Pay: ${takeHomePay:.2f}")
