"""
One-Time-Pad Key-Guess Demonstration

This program uses alphabetic OTP arithmetic with letters represented
by values from A = 0 to Z = 25.

It:
1. Checks whether Eve's second key decrypts the ciphertext to "LATER".
2. Calculates the corrected key if Eve's key is incorrect.
3. Calculates the key stream that makes the same ciphertext decrypt
   to "NEVER".

This demonstrates that different OTP keys can make the same ciphertext
decrypt into different meaningful plaintexts.
"""
CIPHERTEXT = "EQNVZ"
EVES_SECOND_KEY = "TRTSH"
EXPECTED_PLAINTEXT = "LATER"
ALTERNATE_PLAINTEXT = "NEVER"

def decypt(ciphertext: str, key: str) -> str:
    """Decrypts uppercase alphabetic ciphertext using Modulo-26 OTP arithmetic with the given key."""
    if len(ciphertext) != len(key):
        raise ValueError("Ciphertext and key must be the same length.")
    
    plaintext = ""
    for cipher_letter, key_letter in zip(ciphertext, key):
        cipher_value = ord(cipher_letter) - ord('A')
        key_value = ord(key_letter) - ord('A')
        plain_value = (cipher_value - key_value) % 26
        plaintext += chr(plain_value + ord('A'))
    return ''.join(plaintext)

def calculate_corrected_key(ciphertext: str, expected_plaintext: str) -> str:
    """Calculates the corrected key that would decrypt the ciphertext to the expected plaintext."""
    if len(ciphertext) != len(expected_plaintext):
        raise ValueError("Ciphertext and expected plaintext must be the same length.")
    
    corrected_key = ""
    for cipher_letter, plain_letter in zip(ciphertext, expected_plaintext):
        cipher_value = ord(cipher_letter) - ord('A')
        plain_value = ord(plain_letter) - ord('A')
        key_value = (cipher_value - plain_value) % 26
        corrected_key += chr(key_value + ord('A'))
    return ''.join(corrected_key)


if __name__ == "__main__":
    # Check what Eve's second key produces.
    decrypted_guess = decypt(CIPHERTEXT, EVES_SECOND_KEY)

   
    print(f"Ciphertext: {CIPHERTEXT}")
    print(f"Eve's Second Key: {EVES_SECOND_KEY}")
    print(f"Decrypted with Eve's second key: {decrypted_guess}")
   
   

    if decrypted_guess == EXPECTED_PLAINTEXT:
        print("Eve's second key is correct!")
    else:
        print("Eve's second key is incorrect because it does not produce LATER.")

        # Calculate the corrected key that would decrypt to EXPECTED_PLAINTEXT "LATER"
        corrected_key = calculate_corrected_key(CIPHERTEXT, EXPECTED_PLAINTEXT)

        corrected_result = decypt(CIPHERTEXT, corrected_key)
        
        print()
        print(f"Required plaintext: {EXPECTED_PLAINTEXT}")
        print(f"Corrected key:      {corrected_key}")
        print(f"Verification:       {corrected_result}")

    # Calculate the key stream that would decrypt the same ciphertext to ALTERNATE_PLAINTEXT "NEVER"
    alternate_key = calculate_corrected_key(CIPHERTEXT, ALTERNATE_PLAINTEXT)
    alternate_result = decypt(CIPHERTEXT, alternate_key)
    print()
    print(f"Required plaintext: {ALTERNATE_PLAINTEXT}")
    print(f"Alternate key:      {alternate_key}")
    print(f"Verification:       {alternate_result}")
    