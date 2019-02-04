###############################################
# Contents
###############################################
0. README.txt
1. Account.py
2. Block.py
3. Blockchain.py
4. Crypto.py
5. GlobalAccountState.py
6. Miner.py
7. Transaction.py
8. TransactionPool.py

9. BlockchainDemo.py

###############################################
# Quick Use
###############################################
0. Unzip folder
1. cd into folder
2. type...........'python3 BlockchainDemo.py'

3. mine first block.. choose '8' from option menu
4. add account....... choose '1' or '2'
   a) enter a password for the account

5. bradcast txn...... choose '3' (follow prompts)
6. view txns......... choose '5' (txn should appear)
7. mine block........ choose '8'
8. view txns......... choose '5' (txn should be empty)

###############################################
# Description
###############################################
These files simulate a blockchain. Notably this
demo shows a simplification of some of the
harder to understand details in order to shed
light. Key elements that can be seen here:

  0. How Ethereum prevents double spending
  1. How the proof-of-work algorithm creates blocks
  2. How blocks are chained together
  3. How accounts update state
