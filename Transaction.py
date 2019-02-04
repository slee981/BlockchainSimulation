from Crypto import hash_str

class Transaction:

    nonce = None
    data = None
    to = None
    value = None
    sender = None
    fee = 0
    tx_hash = None

    def __init__(self, sender, to, value, nonce, fee=0, data=None):
        self.sender = sender
        self.to = to
        self.value = value
        self.fee = fee
        self.nonce = nonce
        self.data = data
        self.get_hash()

    def get_hash(self):
        str_to_hash = f"{self.sender}{self.to}{self.value}{self.fee}{self.nonce}{self.data}"
        self.tx_hash = hash_str(str_to_hash)

    def to_string(self):
        print(f"Tx..... {self.tx_hash}")
        print(f"To..... {self.to}")
        print(f"From... {self.sender}")
        print(f"Value.. {self.value}")
        print(f"Nonce.. {self.nonce}")
        print(f"Fee.... {self.fee}")
        print(f"Data... {self.data}\n")
