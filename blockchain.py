# Defining our blockchain as a empty list
blockchain = []


# Function to return latest blockchain value
def get_last_blockchain_value():
    return blockchain[-1]


# Function to add values to the blockchain
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


# Function to let the user input the amount of the transaction
def get_user_input():
    return float(input('Your transaction amount please: '))


# Invoke Function with repetitive use of build-in input function
tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)
