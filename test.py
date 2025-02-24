from datetime import datetime


class Account:
    def __init__(self):
        self.transactions = []

    def deposit(self, amount: int, date: str):
        self.transactions.append((date, amount))

    def withdraw(self, amount: int, date: str):
        self.transactions.append((date, -amount))

    def print_statement(self):
        print("Date       | Amount | Balance")
        print("----------------------------")
        balance = 0
        statement = []
        for date, amount in sorted(self.transactions, key=lambda x: datetime.strptime(x[0], "%d-%m-%Y")):
            balance += amount
            statement.append(f"{date} | {amount:6} | {balance:7}")

        for line in reversed(statement):
            print(line)


if __name__ == "__main__":
    account = Account()
    account.deposit(1000, "10-01-2012")
    account.deposit(2000, "13-01-2012")
    account.withdraw(500, "14-01-2012")
    account.print_statement()
