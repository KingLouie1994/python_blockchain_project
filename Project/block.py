# Imports from libraries
from time import time

# Imports from other files
from utility.printable import Printable


class Block(Printable):
    # Define Block
    def __init__(self, index, previous_hash, transactions, proof, time=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof = proof
