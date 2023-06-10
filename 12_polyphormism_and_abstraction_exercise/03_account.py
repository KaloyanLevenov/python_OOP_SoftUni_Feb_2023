class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @property
    def balance(self):  # a property that returns the sum between the amount and all the transactions
        return self.amount + sum(self._transactions)

    def handle_transaction(self, transaction_amount: int):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        else:
            self._transactions.append(transaction_amount)
            return f"New balance: {self.balance}"

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        else:
            self.handle_transaction(amount)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return self._transactions[::-1]

    # (>, <, >=, <=, ==, !=)

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        name = f"{self.owner}&{other.owner}"
        starting_amount = self.amount + other.amount
        new_instance = Account(name, starting_amount)
        new_instance._transactions.extend(self._transactions)
        new_instance._transactions.extend(other._transactions)
        return new_instance
