import hashlib

def simple_hash(data):
    # Convert the input string to bytes
    data_bytes = data.encode()
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256(data_bytes)
    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()
    return hash_hex

# Demonstrate the hashing function
user_input = input("Enter a string to hash: ")
hash_result = simple_hash(user_input)

print(f"Original String: {user_input}")
print(f"SHA-256 Hash: {hash_result}")
