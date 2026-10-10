# OTP XOR Cipher

A simple command-line implementation of the One-Time Pad (OTP) cipher in Python. The program uses XOR to encrypt and decrypt files with cryptographically secure random key material.

## How It Works

The program combines each byte of the input file with the corresponding byte of the key using XOR.

Encryption:

```text
ciphertext = plaintext XOR key
plaintext = ciphertext XOR key

## Security Requirements

For this implementation to function as a genuine One-Time Pad:

- The key must be generated using a cryptographically secure random source.
- The key must be the same length as the plaintext.
- The key must remain secret.
- The key must never be reused.
- The key must be exchanged through a secure method.

Reusing an OTP key can reveal relationships between encrypted messages and compromise their confidentiality.

## Usage

The program requires Python 3 and does not require any external packages.

### 1. Generate a Key

Generate a secure random key matching the size of the plaintext file:

```bash
python3 otp.py generate_key plaintext.txt key.bin
```

### 2. Encrypt the Plaintext

Encrypt the plaintext using the generated key:

```bash
python3 otp.py encrypt plaintext.txt key.bin ciphertext.bin
```

### 3. Decrypt the Ciphertext

Decrypt the ciphertext using the same key:

```bash
python3 otp.py decrypt ciphertext.bin key.bin recovered.txt
```

### 4. Verify the Result

Compare the original and recovered files:

```bash
diff plaintext.txt recovered.txt
```

If `diff` produces no output, the recovered file is identical to the original plaintext.

## Project Files

- `otp.py` — contains the key generation, XOR processing, and command-line interface.
- `plaintext.txt` — example plaintext used for testing.
- `key.bin` — generated secret key material.
- `ciphertext.bin` — encrypted binary output.
- `recovered.txt` — plaintext recovered during decryption.
- `.gitignore` — prevents secret and generated files from being committed.

The key, ciphertext, and recovered output files are generated locally and are not stored in the Git repository.