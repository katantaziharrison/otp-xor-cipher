"""
Simple RSA Cipher Demonstration

This program demonstrates RSA key generation, encryption, and decryption
using the prime numbers P = 7 and Q = 11.

It calculates:
1. The modulus N.
2. Euler's totient W.
3. A valid public exponent E.
4. The corresponding private exponent D.
5. An example of RSA encryption and decryption.

The small prime numbers used here are suitable only for learning.
They are not secure enough for real cryptographic applications.
"""

# gcd() checks whether two numbers are relatively prime.
from math import gcd

p = 7  # First prime number
q = 11  # Second prime number

# Calculate the modulus N
N = p * q  # N = 7 * 11 = 77

# Calculate Euler's totient W
W = (p - 1) * (q - 1)  # W = (7 - 1) * (11 - 1) = 6 * 10 =
# Display the calculated values
print(f"P={p}")
print(f"Q={q}")
print(f"N={N}")
print(f"W={W}")

# Find a valid public exponent E
E = 7  # E must be greater than 1 and less than W, and gcd(E, W) must be 1

# E must be between 1 and W and relatively prime to W
if not (1 < E < W and gcd(E, W) == 1):
    raise ValueError(f"E={E} is not valid. It must be >1, <W, and gcd(E, W) must be 1.")    
print(f"E={E}")
print(f"gcd(E, W)={gcd(E, W)}")

# Calculate D as the modular inverse of E modulo W
D = pow(E, -1, W)  # D is the modular inverse of E mod W

#Vreify that E X D mod W = 1
verification = (E * D) % W

# Display the calculated values
print(f"D={D}")
print(f"Verification (E * D mod W)={verification}")

# Construct the public and private keys
public_key = (E, N)  # Public key is a tuple (E, N)
private_key = (D, N)  # Private key is a tuple (D, N)

print(f"Public Key (E, N) = {public_key}")
print(f"Private Key (D, N) = {private_key}")

# Select a numerical message smaller than N 
m = 9  # Example message (must be less than N)

# RSA requires the message t be between 0 and N-1. Encrypt the message using the public key.
c = pow(m, E, N)  # c = m^E mod N

print(f"Original Message (m) = {m}")
print(f"Encrypted Message (c) = {c}")

# Decrypt the message using the private key
m_decrypted = pow(c, D, N)  # m = c^D mod N

print(f"Decrypted Message (m) = {m_decrypted}")