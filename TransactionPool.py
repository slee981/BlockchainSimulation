class TransactionPool:

    txns = []

    def __init__(self):
        pass

    def add_transaction(self, tx):
        self.txns.append(tx)

    def remove_transaction(self, tx):
        self.txns.remove(tx)
