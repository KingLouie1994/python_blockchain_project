# Imports from libraries
from uuid import uuid4

# Imports from other files
from blockchain import Blockchain
from verification import Verification

class Node:
    def __init__(self):
        # self.id = str(uuid4())
        self.id = 'Luis'
        self.blockchain = Blockchain(self.id)

    # Function to let the user input the amount of the transaction
    def get_transaction_value(self):
        tx_recipient = input('Enter the recipient of the transaction: ')
        user_input = float(input('Your transaction amount please: '))
        return tx_recipient, user_input

    # Function to receive users choices of inputs
    def get_user_choice(self):
        user_input = input("Your choice: ")
        return user_input

    # Output the blockchain to the console using for loop

    def print_blockchain_elements(self):
        print("-" * 50)
        for block in self.blockchain.chain:
            print("-" * 20)
            print(block)
            print("-" * 20)
        else:
            print("-" * 50)

    def liste_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            """ Printing out the different input options """
            print("Please choose!")
            print("1: Add a new transaction")
            print("2: Mine a new block")
            print("3: Output the blockchain transactions")
            print("4: Verify all open transactions")
            print("q: Quit")

            """ Receiving users choice """
            user_choice = self.get_user_choice()

            """ Using conditions to invoke functions depending on users input """
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(self.blockchain.open_transactions)
            elif user_choice == '2':
                self.blockchain.mine_block()    
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                verifier = Verification()
                if verifier.verify_transactions(self.blockchain.open_transactions, self.blockchain.get_balances):
                    print("All transactions are valid")
                else:
                    print("There are invalid transactions")
            elif user_choice == 'q':
                print("Choice registered!")
                waiting_for_input = False
            else:
                print("Please choose one of the existing options")
            verifier = Verification()
            if not verifier.verify_chain(self.blockchain.chain):
                print("Invalid blockchain")
                break
            print('Balance of {}: {:6.2f}'.format(self.id, self.blockchain.get_balances()))
        else:
            print("User left!")


node = Node()
node.liste_for_input()