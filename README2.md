# What Is Hashing?

### Hashing is the process of transforming an input (or "message") into a fixed-size string of bytes, typically a hash value. The output is usually a hexadecimal string.

## Key Properties of Hash Functions:
- Deterministic: The same input will always produce the same hash.

- Fast Computation: Efficiently computes the hash for any given data.

- Irreversibility: It’s infeasible to reverse the hash to get the original input.

- Avalanche Effect: A small change in input drastically changes the hash.

- Unique Output: Different inputs should not produce the same hash (low collision probability)

## Why Use SHA-256?

SHA-256 (Secure Hash Algorithm 256-bit) is part of the **SHA-2** family and is widely used in security protocols **(like SSL/TLS)** and blockchain technologies. It produces a 256-bit (64 hexadecimal characters) hash.

# Step-by-Step Breakdown:

1. Importing the Library:

<pre> ```python import hashlib ``` </pre>
*The hashlib library provides common hashing algorithms like MD5, SHA-1, and SHA-256.*

### SHA-256 is being used because it’s secure and collision-resistant.

2. Function Definition:

<pre> ```python def simple_hash(data):``` </pre>
*This function takes a single input, data, which is a string.*

3. Encoding the String:

<pre>```python data_bytes = data.encode()``` </pre>
*Hash functions in Python operate on bytes, not strings.*

### The **encode()** method converts the string into a bytes object.

4. Creating the Hash Object:

<pre>```python hash_object = hashlib.sha256(data_bytes)``` </pre>
- *We use **hashlib.sha256()** to create a new hash object.*

- The input bytes are passed to this function to generate the hash.

5. Getting the Hash Hexadecimal:

<pre>```python hash_hex = hash_object.hexdigest()``` </pre>
**hexdigest()** returns the hash as a hexadecimal string.

- A SHA-256 hash is 256 bits or 64 hexadecimal characters long.

6. Returning the Hash:

<pre>```python return hash_hex``` </pre>
- The function returns the resulting hash.

#### Example Demonstration:
You enter a string when prompted: blockchain

**Enter a string to hash: blockchain**
The output shows the hash:

***Original String: blockchain**
**SHA-256 Hash: cbcf6c8dfb10f1b7b1566c9a8c9e3165c8d29e0c6c3dd9cf82e1ffde839f9889***

- Interesting Fact: The Avalanche Effect
#### One fascinating property of cryptographic hash functions is the avalanche effect, where a tiny change in the input drastically changes the hash.

Example:
Input 1: "Hello, World!"
Hash: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b53dc337c6a727ae8

Input 2: "Hello, world!" (Notice the lowercase w)
Hash: 64ec88ca00b268e5ba1a35678a1b5316d212f4f366b247724e5f7e1c0eea32e8

A single letter change completely alters the hash!

