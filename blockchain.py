# Imports of libraries
import functools
import hashlib as hl
import json

# Defining our global variables
MINING_REWARD = 10

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': [],
    'proof': 100
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Luis'
participants = {'Luis'}


# Reusabele function to create a hashed block
def hash_block(block):
    return hl.sha256(json.dumps(block).encode()).hexdigest()


def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hl.sha256(guess).hexdigest()
    print(guess_hash)
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


# Function to receive balance of a participant of the blockchain
def get_balances(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = functools.reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    # amount_sent = 0
    # for tx in tx_sender:
    #     if len(tx) > 0:
    #         amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['recipient'] == participant] for block in blockchain]
    # amount_received = 0
    # for tx in tx_recipient:
    #     if len(tx) > 0:
    #         amount_received += tx[0]
    amount_received = functools.reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
    # Return the total balance
    return amount_received - amount_sent


# Function to return latest blockchain value
def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# Function to verify if the sender has enough coins to make a transaction
def verify_transaction(transaction):
    sender_balance = get_balances(transaction['sender'])
    return sender_balance >= transaction['amount']


# Function to add transactions to the blockchain
def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain

    Arguments:
        :sender: The sender of the coins
        :recepient: Recipient of the coins
        :amount: The amount of coins sent with the transaction (Default: 1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


# Function to mine a new block
def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions,
        'proof': proof
    }
    blockchain.append(block)
    return True


# Function to let the user input the amount of the transaction
def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction: ')
    user_input = float(input('Your transaction amount please: '))
    return tx_recipient, user_input


# Function to receive users choices of inputs
def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


# Output the blockchain to the console using for loop
def print_blockchain_elements():
    print("-" * 50)
    for block in blockchain:
        print("-" * 20)
        print(block)
        print("-" * 20)
    else:
        print("-" * 50)


# A function used to validate if the blockchain is manipulated
def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            print("Proof of work is invalid")
            return False
    return True


# def verify_transactions():
#     is_valid = True
#     for tx in open_transactions:
#         if verify_transaction(tx):
#             is_valid = True
#         else:
#             is_valid = False
#     return is_valid


waiting_for_input = True


while waiting_for_input:
    """ Printing out the different input options """
    print("Please choose!")
    print("1: Add a new transaction")
    print("2: Mine a new block")
    print("3: Output the blockchain transactions")
    print("4: Output participants")
    # print("5: Check transaction validity")
    print("h: Manipulate the chain")
    print("q: Quit")

    """ Receiving users choice """
    user_choice = get_user_choice()

    """ Using conditions to invoke functions depending on users input """
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    # elif user_choice == '5':
    #     if verify_transactions():
    #         print('All transactions are valid')
    #     else:
    #         print("There are invalid transactions")
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 30.0}]
            }
    elif user_choice == 'q':
        print("Choice registered!")
        waiting_for_input = False
    else:
        print("Please choose one of the existing options")
    if not verify_chain():
        print("Invalid blockchain")
        break
    print('Balance of {}: {:6.2f}'.format(owner, get_balances(owner)))
else:
    print("User left!")
