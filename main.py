from finance.income import Income
from finance.expenses import Expenses

income = Income()
expenses = Expenses()

# Sample data
income.add_income(1000000, "Salary")
income.add_income(200000, "Freelance")
expenses.add_expense(300000, "Rent")
expenses.add_expense(50000, "Transport")

print("Total Income:", income.total_income())
print("Total Expenses:", expenses.total_expenses())
print("Balance:", income.total_income() - expenses.total_expenses())
