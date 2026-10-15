"""
Generic RSA Encryption and Library Decryption

This program demonstrates that textbook RSA and a cryptographic library
perform the same underlying mathematical operation.

The program:
1. Generates an RSA key using PyCryptodome.
2. Converts a text message to bytes.
3. Adds manual zero padding to match the RSA block size.
4. Converts the padded bytes to an integer.
5. Encrypts the integer using generic RSA: C = M^E mod N.
6. Decrypts it using PyCryptodome's raw RSA operation.
7. Removes the padding and reconstructs the original text.

Raw RSA and zero padding are used only to demonstrate the assignment.
They are not secure for real applications.
"""

from Crypto.PublicKey import RSA

# Generate a 1024-bit RSA key pair using cryptographic library
private_key = RSA.generate(1024)
public_key = private_key.publickey()

# Extract the  RSA parameters
N = public_key.n  # Modulus
E = public_key.e  # Public exponent

# calculate the RSA block size in bytes
key_size_bytes = (N.bit_length() + 7) // 8

print(f"RSA Key Size: {N.bit_length()} bits ")
print(f"public exponent (E): {E}")
print(f"RSA Block Size: {key_size_bytes} bytes")

# Message used for the interoperability test
message = "Generic RSA and Library RSA are the same!"
message_bytes = message.encode('utf-8')

# Reserve at least one leading zero byte for padded integer is less than modulus N
if len(message_bytes) > key_size_bytes - 1:
    raise ValueError("Message is too long for the RSA block size.")

# Add manual zero padding to the message bytes until it matches the RSA block size
padding_length = key_size_bytes - len(message_bytes)
padded_message = (b'\x00' * padding_length) + message_bytes

# Convert the fixed-size byte block into a larger integer for RSA encryption
message_integer = int.from_bytes(padded_message, byteorder='big', signed=False)

print(f"Original Message: {message}")
print(f"Message length: {len(message_bytes)} bytes")
print(f"Manual padding length: {padding_length} bytes")
print(f"Padded block length: {len(padded_message)} bytes")
print(f"Message Integer is smaller than modulus: {message_integer < N}")

# Encrypt using the generic RSA algorithm from  exercise 4.
# C = M^E mod N
ciphertext_integer = pow(message_integer, E, N)

# Represent the ciphertext as a fixed-size byte array.
ciphertext_bytes = ciphertext_integer.to_bytes(key_size_bytes, byteorder='big', signed=False)
print(f"Ciphertext block length: {len(ciphertext_bytes)} bytes")
print("Ciphertext in Hexadecimal: (16 bytes per line):")
for offset in range(0, len(ciphertext_bytes), 16):
    block = ciphertext_bytes[offset:offset + 16]
    formatted_hex = block.hex(" ")
    print(f"{offset:04x}: {formatted_hex}")

# Decrypt using PyCryptodome's raw RSA private-key operation.
# This performs M = C^D mod N without applying or removing padding.
# The assignment needs an internal method, which some editor type checkers
# do not expose on RSA keys. Look it up explicitly for this demonstration.
raw_decrypt = getattr(private_key, "_decrypt")
decrypted_integer = int(raw_decrypt(ciphertext_integer))

# Convert the decrypted integer back into a fixed-size byte block.
decrypted_padded_message = decrypted_integer.to_bytes(
    key_size_bytes,
    byteorder="big",
    signed=False,
)

print(
    "Decrypted padded block matches original:",
    decrypted_padded_message == padded_message,
)

# Remove exactly the zero bytes added before encryption.
# Keeping the original padding length preserves any zero bytes in the message.
if decrypted_padded_message[:padding_length] != b'\x00' * padding_length:
    raise ValueError("Decrypted block does not contain the expected zero padding.")

recovered_message_bytes = decrypted_padded_message[padding_length:]
recovered_message = recovered_message_bytes.decode('utf-8')

print(f"Recovered Message: {recovered_message}")
print(f"Recovered message matches original: {recovered_message == message}")

assert decrypted_padded_message == padded_message
assert recovered_message == message
