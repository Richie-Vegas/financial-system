class Expenses:
    def __init__(self):
        self.records = []

    def add_expense(self, amount, category):
        self.records.append({'amount': amount, 'category': category})

    def total_expenses(self):
        return sum(item['amount'] for item in self.records)
