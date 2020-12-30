# Defining our blockchain as a empty list
blockchain = []


# Function to return latest blockchain value
def get_last_blockchain_value():
    return blockchain[-1]


# Function to add values to the blockchain
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)


# Invoke Function
add_value(2)
add_value(0.9, get_last_blockchain_value())
add_value(10.89, get_last_blockchain_value())
