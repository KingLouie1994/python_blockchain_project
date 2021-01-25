"""Provides verification helper methods"""

# Imports from other files
from utility.hash_util import hash_string_256, hash_block
from wallet import Wallet

class Verification:
    @staticmethod
    # Function to validate the proof of a block
    def valid_proof(transactions, last_hash, proof):
        guess = (str([tx.to_ordered_dict() for tx in transactions]) +
                str(last_hash) + str(proof)).encode()
        guess_hash = hash_string_256(guess)
        print(guess_hash)
        return guess_hash[0:2] == '00'

    # A function used to validate if the blockchain is manipulated
    @classmethod
    def verify_chain(cls, blockchain):
        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue
            if block.previous_hash != hash_block(blockchain[index - 1]):
                return False
            if not cls.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                print("Proof of work is invalid")
                return False
        return True

    # Function to verify if the sender has enough coins to make a transaction
    @staticmethod
    def verify_transaction(transaction, get_balances, check_funds=True):
        if check_funds:
            sender_balance = get_balances()
            return sender_balance >= transaction.amount and Wallet.verify_transaction(transaction)
        else:
            return Wallet.verify_transaction(transaction)

    # A function that verifies all open transactions
    @classmethod
    def verify_transactions(cls, open_transactions, get_balances):
        return all([cls.verify_transaction(tx, get_balances, False) for tx in open_transactions])

