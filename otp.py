
"""
Simple One-Time Pad (OTP) Cipher Using XOR

This program encrypts and decrypts files using the XOR operation.
It reads the input data and key material from separate files, combines
their corresponding bytes using XOR, and writes the result to an
output file.

The program supports three operations:
1. Generate a cryptographically secure random key.
2. Encrypt a plaintext file using the key.
3. Decrypt a ciphertext file using the same key.

For proper OTP security, the key must:
- Be generated using a cryptographically secure random source.
- Be at least as long as the plaintext.
- Be kept secret.
- Never be reused.

Because XOR is reversible, the same operation is used for both
encryption and decryption.
"""

# Provides functions for generating cryptographically secure random bytes.
import secrets

# Provides tools for working with files and obtaining their sizes.
import os
import argparse
from pathlib import Path

def generate_key(input_file: Path, key_file: Path) -> None:
    """
    Generates a cryptographically secure random key for the One-Time Pad (OTP) cipher.

    The key is generated to be the same length as the input file, ensuring that
    it can be used for encryption and decryption without any loss of data.

    Args:
        input_file (Path): The path to the input file for which the key is generated.
        key_file (Path): The path where the generated key will be saved.

    Raises:
        FileNotFoundError: If the input file does not exist.
        IOError: If there is an error writing to the key file.
    """
    # Check if the input file exists
    if not input_file.is_file():
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

    # Get the size of the input file in bytes
    input_size = os.path.getsize(input_file)

    # Generate a random key of the same size as the input file
    key = secrets.token_bytes(input_size)

    # Write the generated key to the specified key file
    with open(key_file, 'wb') as kf:
        kf.write(key)

    print(f"Generated a random key of size {input_size} bytes and saved it to '{key_file}'.")

def xor_files(input_file: Path, key_file: Path, output_file: Path) -> None:
        """
        Encrypts or decrypts a file using the One-Time Pad (OTP) cipher with XOR operation.

        The function reads the input file and the key file, applies the XOR operation
        between corresponding bytes, and writes the result to the output file.

        Args:
            input_file (Path): The path to the input file (plaintext or ciphertext).
            key_file (Path): The path to the key file.
            output_file (Path): The path where the output (ciphertext or plaintext) will be saved.

        Raises:
            FileNotFoundError: If either the input file or key file does not exist.
            ValueError: If the sizes of the input file and key file do not match.
            IOError: If there is an error writing to the output file.
        """
        # Check if both input and key files exist
        if not input_file.is_file():
            raise FileNotFoundError(f"Input file '{input_file}' does not exist.")
        if not key_file.is_file():
            raise FileNotFoundError(f"Key file '{key_file}' does not exist.")

        # Get sizes of both files
        input_size = os.path.getsize(input_file)
        key_size = os.path.getsize(key_file)

        # Ensure that the sizes match
        if input_size != key_size:
            raise ValueError("Input file and key file must be of the same size for OTP.")

        # Read data from both files
        with open(input_file, 'rb') as inf, open(key_file, 'rb') as kf:
            input_data = inf.read()
            key_data = kf.read()

        # Perform XOR operation between corresponding bytes
        output_data = bytes(a ^ b for a, b in zip(input_data, key_data))

        # Write the result to the output file
        with open(output_file, 'wb') as outf:
            outf.write(output_data)

        print(f"Processed '{input_file}' with '{key_file}' and saved result to '{output_file}'.")


    
    
    # Test the key-generation function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="One-Time Pad (OTP) Cipher Using XOR"
    )

    parser.add_argument(
        "operation",
        choices=["generate_key", "encrypt", "decrypt"],
        help="Operation to perform",
    )

    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to the input file",
    )

    parser.add_argument(
        "key_file",
        type=Path,
        help="Path to the key file",
    )

    parser.add_argument(
        "output_file",
        type=Path,
        nargs="?",
        help="Path to the output file (required for encrypt/decrypt)",
    )

    args = parser.parse_args()

    if args.operation == "generate_key":
        generate_key(args.input_file, args.key_file)

    elif args.operation in ["encrypt", "decrypt"]:
        if not args.output_file:
            parser.error(
                "The output_file argument is required for "
                "encrypt and decrypt operations."
            )

        xor_files(
            args.input_file,
            args.key_file,
            args.output_file,
        )