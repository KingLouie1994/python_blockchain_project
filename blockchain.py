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
def get_transaction_value():
    return float(input('Your transaction amount please: '))


# Function to receive users choices of inputs
def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


# Output the blockchain to the console using for loop
def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)


# Invoke get_user_input function to add a first value to the blockchain
tx_amount = get_transaction_value()
add_value(tx_amount)


while True:
    """ Printing out the different input options """
    print("Please choose!")
    print("1: Add a new transaction value")
    print("2: Output the blockchain values")
    print("q: Quit")

    """ Receiving users choice """
    user_choice = get_user_choice()

    """ Using conditions to invoke functions depending on users input """
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        print("Choice registered!")
        break
    else:
        print("Please choose one of the existing options")
    print("Choice registered!")

print("Done!")
