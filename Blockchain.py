from Crypto import hash_str
from GlobalAccountState import GlobalAccountState
from Block import Block
from TransactionPool import TransactionPool

class Blockchain:

    current_block = None
    tx_pool = None
    state = None

    def __init__(self):
        genesis = Block(block_number=0)
        self.current_block = genesis
        self.tx_pool = TransactionPool()
        self.state = GlobalAccountState()

    def add_block(self, block):
        self.state.record_block(block)
        self.current_block = block
        self.tx_pool = TransactionPool()
        print("\n=======================================")
        print(f"[-->] New block number {block.block_number}")

    def add_txn_to_pool(self, txn):
        self.tx_pool.add_transaction(txn)

    def get_block_by_num(self, block_num):
        if self.current_block != None \
            and block_num <= self.current_block.block_number \
            and block_num > 0:

            cur_block = self.current_block
            cur_num = cur_block.block_number

            while (cur_num != block_num):
                cur_block = self.state.blocks[cur_block.parent_hash]
                cur_num = cur_block.block_number

            return cur_block
        else:
            return None

    def to_string(self):
        return f"Current block number: {self.current_block.block_number}\n"
