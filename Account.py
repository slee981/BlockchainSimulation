from Crypto import get_pub_key

class Account:

    nonce = 0
    balance = 0
    acct_id = None

    def __init__(self, privateKey):
        self.acct_id = get_pub_key(privateKey)
