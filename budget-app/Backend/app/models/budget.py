from app.database import db
from sqlalchemy.orm import Mapped, mapped_column

class Budget:
    def __init__(self, monthly_income, checking_balance):
        self.monthly_income = monthly_income
        self.checking_balance = checking_balance
        self.expenses = {
            'housing': 0.0,
            'bills': 0.0,
            'utilities': 0.0,
            'phone_bill': 0.0,
            'subscriptions': 0.0,
            'memberships': 0.0,
            'insurance': 0.0,
            'mental_health': 0.0,
            'loan_payments': 0.0,
            'miscellaneous': 0.0
        }

    def set_expense(self, expense_name, amount):
        if expense_name in self.expenses:
            self.expenses[expense_name] = amount
        else:
            raise ValueError(f"Expense '{expense_name}' not recognized.")

    def add_expense(self, expense_name, amount):
        if expense_name in self.expenses:
            self.expenses[expense_name] += amount
        else:
            raise ValueError(f"Expense '{expense_name}' not recognized.")

    def remove_expense(self, expense_name, amount):
        if expense_name in self.expenses:
            if self.expenses[expense_name] >= amount:
                self.expenses[expense_name] -= amount
            else:
                raise ValueError(f"Cannot remove more than the current amount for '{expense_name}'.")
        else:
            raise ValueError(f"Expense '{expense_name}' not recognized.")

    def calculate_total_expenses(self):
        return sum(self.expenses.values())

    def calculate_remaining_balance(self):
        total_expenses = self.calculate_total_expenses()
        return self.monthly_income - total_expenses

    def budget_summary(self):
        total_expenses = self.calculate_total_expenses()
        remaining_balance = self.calculate_remaining_balance()
        summary = {
            'monthly_income': self.monthly_income,
            'checking_balance': self.checking_balance,
            'total_expenses': total_expenses,
            'remaining_balance': remaining_balance,
            'expenses_breakdown': self.expenses
        }
        return summary

# Example usage
my_budget = Budget(monthly_income=5000, checking_balance=1500)
my_budget.set_expense('housing', 1200)
my_budget.set_expense('bills', 150)
my_budget.add_expense('utilities', 100)
my_budget.add_expense('phone_bill', 60)
my_budget.add_expense('subscriptions', 40)
my_budget.set_expense('mental_health', 80)

print("Budget Summary:")
print(my_budget.budget_summary())
