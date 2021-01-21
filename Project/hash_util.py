# Imports from libraries
import hashlib as hl
import json


# Function to hash strings
def hash_string_256(string):
    return hl.sha256(string).hexdigest()


# Reusabele function to create a hashed block
def hash_block(block):
    return hash_string_256((json.dumps(block, sort_keys=True).encode()))
