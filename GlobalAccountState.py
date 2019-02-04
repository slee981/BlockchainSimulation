from Crypto import get_pub_key
from Account import Account
from Miner import Miner
from random import randint

class GlobalAccountState:

    accts = {}
    blocks = {}
    miners = []
    difficulty = 3

    def __init__(self):
        self.add_miner("password")

    def get_accts(self):
        return self.accts

    def get_state(self):
        print("=======================================")
        print("Current state of accounts:\n")
        for acct_id, acct in self.accts.items():
            print(f"Account {acct_id}:\nNonce {acct.nonce}, Balance {acct.balance}\n")

    def add_account(self, privateKey):
        account = Account(privateKey)
        self.accts[account.acct_id] = account
        print(f"\nAdded account {account.acct_id}\n")

    def add_miner(self, privateKey):
        miner = Miner(privateKey)
        self.accts[miner.acct_id] = miner
        self.miners.append(miner)
        print(f"\nAdded miner {miner.acct_id}\n")

    def record_block(self, block):
        self_hash = block.to_hash()
        self.blocks[self_hash] = block

    def choose_miner(self):
        m = randint(0, len(self.miners) - 1)
        return self.miners[m]

    def get_block(self, hsh):
        return self.blocks[hsh]

    def increase_difficulty(self):
        self.difficulty += 1

    def decrease_difficulty(self):
        self.difficulty -= 1
