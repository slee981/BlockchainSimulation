from Crypto import get_pub_key, hash_str
from Account import Account
from Block import Block

class Miner(Account):

    def __init__(self, privateKey):
        super().__init__(privateKey)

    def mine_block(self, blockchain):
        difficulty = blockchain.state.difficulty
        beneficiary = self.acct_id
        txns = blockchain.tx_pool.txns
        new_parent_hash = blockchain.current_block.to_hash()
        new_block_num = blockchain.current_block.block_number + 1

        tx_string = ''
        for tx in txns:
            tx_string += tx.tx_hash

        tx_hashes = hash_str(tx_string)
        nonce, block = self.find_proof_of_work(difficulty, new_parent_hash, beneficiary, new_block_num, tx_hashes)

        self.process_txns(blockchain)

        return block

    def find_proof_of_work(self, difficulty, parent_hash, beneficiary, block_num, tx_hashes):

        nonce = 1
        valid = False
        while not valid:
            block = Block(parent_hash, beneficiary, block_num, tx_hashes, nonce)
            h = block.to_hash()
            print(block.to_string())
            print(f"Current block hash..... {h}")
            if h[2:difficulty+2] == '0'*difficulty:
                valid = True
            else:
                nonce += 1
        return (h, block)

    def process_txns(self, blockchain):

        def _add_miner_reward(blockchain):
            blockchain.state.accts[self.acct_id].balance += 5

        def _update_state(blockchain, sender, to, fee, value):
            blockchain.state.accts[sender].balance -= value
            blockchain.state.accts[sender].nonce += 1
            blockchain.state.accts[to].balance += value
            blockchain.state.accts[self.acct_id].balance += fee

        _add_miner_reward(blockchain)

        txns = blockchain.tx_pool.txns
        for tx in txns:
            sender = tx.sender
            to = tx.to
            fee = tx.fee
            nonce = tx.nonce
            value = tx.value
            if blockchain.state.accts[sender].nonce != nonce:
                print(f"\nERROR: Invalid nonce for sender {sender}")
                continue
            if blockchain.state.accts[sender].balance < value + fee:
                print(f"\nERROR: Not enough funds for sender {sender}")
                continue

            blockchain.tx_pool.remove_transaction(tx)
            _update_state(blockchain, sender, to, fee, value)
