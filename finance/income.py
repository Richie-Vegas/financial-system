class Income:
    def __init__(self):
        self.records = []

    def add_income(self, amount, source):
        self.records.append({'amount': amount, 'source': source})

    def total_income(self):
        return sum(item['amount'] for item in self.records)
