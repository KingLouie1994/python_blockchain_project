# Defining our global variables
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Luis'
participants = {'Luis'}


# Reusabele function to create a hashed block
def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


# Function to receive balance of a participant of the blockchain
def get_balances(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


# Function to return latest blockchain value
def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


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
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


# Function to mine a new block
def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
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
    print("-" * 20)
    for block in blockchain:
        print(block)
    else:
        print("-" * 20)


# A function used to validate if the blockchain is manipulated
def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True


while waiting_for_input:
    """ Printing out the different input options """
    print("Please choose!")
    print("1: Add a new transaction")
    print("2: Mine a new block")
    print("3: Output the blockchain transactions")
    print("4: Output participants")
    print("h: Manipulate the chain")
    print("q: Quit")

    """ Receiving users choice """
    user_choice = get_user_choice()

    """ Using conditions to invoke functions depending on users input """
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
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
    print(get_balances(owner))
else:
    print("User left!")
