# Imports from libraries
from collections import OrderedDict

# Imports from other files
from utility.printable import Printable


class Transaction(Printable):
    # Define Transaction
    def __init__(self, sender, recipient, signature, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature

    # Function to order a transaction always the same way
    def to_ordered_dict(self):
        return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('amount', self.amount)])
