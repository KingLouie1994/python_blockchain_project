# Defining our blockchain as a empty list
blockchain = [[1]]


# Build Function to add values to the blockchain
def add_value(transaction_amount):
    blockchain.append([blockchain[-1], transaction_amount])
    print(blockchain)


# Invoke Function
add_value(2)
add_value(0.9)
add_value(10.89)
