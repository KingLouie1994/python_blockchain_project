# Defining our global variables
blockchain = []
open_transactions = []
owner = 'Luis'


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


def mine_block():
    pass


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
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print("-" * 20)


# A function used to validate if the blockchain is manipulated
def verify_chain():
    block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid


waiting_for_input = True


while waiting_for_input:
    """ Printing out the different input options """
    print("Please choose!")
    print("1: Add a new transaction")
    print("2: Output the blockchain transactions")
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
        print_blockchain_elements()
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        print("Choice registered!")
        waiting_for_input = False
    else:
        print("Please choose one of the existing options")
    if not verify_chain():
        print("Invalid blockchain")
        break
else:
    print("User left!")
