# Imports from other files
from hash_util import hash_string_256, hash_block

class Verification:
    # Function to validate the proof of a block
    def valid_proof(self, transactions, last_hash, proof):
        guess = (str([tx.to_ordered_dict() for tx in transactions]) +
                str(last_hash) + str(proof)).encode()
        guess_hash = hash_string_256(guess)
        print(guess_hash)
        return guess_hash[0:2] == '00'

    # A function used to validate if the blockchain is manipulated
    def verify_chain(self, blockchain):
        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue
            if block.previous_hash != hash_block(blockchain[index - 1]):
                return False
            if not self.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                print("Proof of work is invalid")
                return False
        return True

    # Function to verify if the sender has enough coins to make a transaction
    def verify_transaction(self, transaction, get_balances):
        sender_balance = get_balances()
        return sender_balance >= transaction.amount

    # A function that verifies all open transactions
    def verify_transactions(self, open_transactions, get_balances):
        return all([self.verify_transaction(tx, get_balances) for tx in open_transactions])

