from Crypto import hash_str
from datetime import datetime

class Block:

    parent_hash = None
    beneficiary = None
    block_number = None
    tx_hashes = None
    nonce = None
    timestamp = None

    def __init__(self, parent_hash=None,\
                 beneficiary=None, block_number=None,\
                 tx_hashes=None, nonce=None):

        self.parent_hash = parent_hash
        self.beneficiary = beneficiary
        self.block_number = block_number
        self.tx_hashes = tx_hashes
        self.nonce = nonce
        self.timestamp = datetime.now().timestamp()

    def to_string(self):
        return f"\nBlock Number........... {self.block_number}\
                 \nParent Hash............ {self.parent_hash}\
                 \nWinning Miner.......... {self.beneficiary}\
                 \nTx Hashes.............. {self.tx_hashes}\
                 \nNonce (Proof of Work).. {self.nonce}\n"

    def to_hash(self):
        return hash_str(self.to_string())
