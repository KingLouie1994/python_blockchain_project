# Defining our blockchain as a empty list
blockchain = []


# Function to return latest blockchain value
def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    return blockchain[-1]


# Function to add values to the blockchain
def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    blockchain.append([last_transaction, transaction_amount])


# Function to let the user input the amount of the transaction
def get_user_input():
    return float(input('Your transaction amount please: '))


# Invoke get_user_input function for the first time
tx_amount = get_user_input()
add_value(tx_amount)

# Using while loop to start an inifinite loop to add 'transactions' to the blockchain
while True:
    tx_amount = get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

    # Output the blockchain to the console using for loop
    for block in blockchain:
        print('Outputting Block')
        print(block)

print("Done!")
