# Imports from libraries
from uuid import uuid4

# Imports from other files
from blockchain import Blockchain
from utility.verification import Verification
from wallet import Wallet


class Node:
    def __init__(self):
        # self.id = str(uuid4())
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)

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
            print("5: Create wallet")
            print("6: Load wallet")
            print("7: Save keys")
            print("q: Quit")

            """ Receiving users choice """
            user_choice = self.get_user_choice()

            """ Using conditions to invoke functions depending on users input """
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                signature = self.wallet.sign_transaction(
                    self.wallet.public_key, recipient, amount)
                if self.blockchain.add_transaction(recipient, self.wallet.private_key, signature, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(self.blockchain.get_open_transactions())
            elif user_choice == '2':
                if not self.blockchain.mine_block():
                    print('Mining failer. Got no wallet?')
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balances):
                    print("All transactions are valid")
                else:
                    print("There are invalid transactions")
            elif user_choice == '5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '6':
                self.wallet.load_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif user_choice == '7':
                self.wallet.save_keys()
            elif user_choice == 'q':
                print("Choice registered!")
                waiting_for_input = False
            else:
                print("Please choose one of the existing options")
            if not Verification.verify_chain(self.blockchain.chain):
                print("Invalid blockchain")
                break
            print('Balance of {}: {:6.2f}'.format(
                self.wallet.public_key, self.blockchain.get_balances()))
        else:
            print("User left!")


if __name__ == '__main__':
    node = Node()
    node.liste_for_input()
