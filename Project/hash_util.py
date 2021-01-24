# Imports from libraries
import hashlib as hl
import json


# Function to hash strings
def hash_string_256(string):
    return hl.sha256(string).hexdigest()


# Reusabele function to create a hashed block
def hash_block(block):
    hashable_block = block.__dict__.copy()
    hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
    return hash_string_256((json.dumps(hashable_block, sort_keys=True).encode()))
