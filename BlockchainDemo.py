from Crypto import get_pub_key
from GlobalAccountState import GlobalAccountState
from Transaction import Transaction
from Blockchain import Blockchain
from Block import Block
from Miner import Miner
from datetime import datetime
from random import randint

def get_account_state(blockchain):
    blockchain.state.get_state()

def get_unprocessed_txns(blockchain):
    txns = blockchain.tx_pool.txns
    if len(txns) > 0:
        print("Pending Transactions:\n")
        for tx in txns:
            tx.to_string()
    else:
        print("No pending transactions\n")

def get_current_blockchain_state(blockchain):
    print(blockchain.current_block.to_string())

def get_block_info(blockchain):
    block_num = prompt_user("\nEnter the block number you would like to explore.\n >> ")
    block = blockchain.get_block_by_num(block_num)
    try:
        print(block.to_string())
    except:
        print("No blocks yet")

def add_user_account(blockchain):
    privateKey = input("\nPlease enter a private key for your account.\n >> ")
    blockchain.state.add_account(privateKey)

def add_miner_account(blockchain):
    privateKey = input('\nPlease enter a private key for your account.\n >> ')
    blockchain.state.add_miner(privateKey)

def add_transaction(blockchain):
    privateKey = input("Please enter your private key to verify the transaction >> ")
    to = input("Please enter an address for the recepient >> ")
    value = prompt_user("Please enter a value to transfer >> ")
    sender = get_pub_key(privateKey)
    try:
        nonce = blockchain.state.accts[sender].nonce
        tx = Transaction(sender, to, value, nonce)
        blockchain.add_txn_to_pool(tx)
    except:
        print("\nERROR: invalid private key")

def time_to_mine(last_block_time):
    blocktime = randint(5,10)
    curr_time = datetime.now().timestamp()
    delta = curr_time - last_block_time
    if (delta >= blocktime):
        return True
    else:
        return False

def mine(blockchain):
    txns = blockchain.tx_pool
    miner = blockchain.state.choose_miner()
    block = miner.mine_block(blockchain)

    blockchain.add_block(block)
    get_account_state(blockchain)

def prompt_user(message):
    valid = False
    while not valid:
        selection = input(message)
        try:
            selection = int(selection)
            valid = True
        except:
            print("\nERROR: invalid selection")
    return selection

def user_menu(blockchain):

    valid = False
    while not valid:
        print("=======================================")
        print("= Select an option from the menu below:")
        print("=======================================")
        print("  1. Add a user account.")
        print("  2. Add a miner account.\n")
        print("  3. Broadcast a transaction.\n")
        print("  4. See account info.")
        print("  5. See unprocessed transactions.")
        print("  6. See specific block.")
        print("  7. See current block.\n")
        print("  8. Find proof of work (i.e. mine new block).")
        print("  9. Increase work difficulty.")
        print(" 10. Decrease work difficulty.\n")
        print(" 11. Exit simulation.")
        selection = prompt_user("\n >> ")
        print("\n=======================================")
        if (selection > 0 and selection < 12):
            return selection
        else:
            print("\nERROR: invalid selection")

def main():

    blockchain = Blockchain()

    done = False
    while not done:

        choice = user_menu(blockchain)

        if (choice == 1):
            add_user_account(blockchain)

        elif (choice == 2):
            add_miner_account(blockchain)

        elif (choice == 3):
            add_transaction(blockchain)

        elif (choice == 4):
            get_account_state(blockchain)

        elif (choice == 5):
            get_unprocessed_txns(blockchain)

        elif (choice == 6):
            get_block_info(blockchain)

        elif (choice == 7):
            get_current_blockchain_state(blockchain)

        elif (choice == 8):
            mine(blockchain)

        elif (choice == 9):
            blockchain.state.increase_difficulty()

        elif (choice == 10):
            blockchain.state.decrease_difficulty()

        else:
            done = True
            print("\nGoodbye.\n")


###############################################################
if __name__ == "__main__":
    main()
