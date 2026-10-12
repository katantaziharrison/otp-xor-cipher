"""
Generic Diffie-Hellman Key Exchange Demonstration

This program implements the same Diffie-Hellman scheme demonstrated
in the provided Java example.

Alice and Bob publicly share a prime number and a generator. Each
participant chooses a private secret and calculates a public value.
After exchanging their public values, both independently calculate
the same shared secret.

This implementation uses small values for educational purposes only.
Real Diffie-Hellman systems require large, carefully selected
parameters and secure random private values.
"""
class DH:
    """ 
    Diffie-Hellman Key Exchange Class

    Attributes:
        p (int): A prime number used as the modulus.
        g (int): A generator for the multiplicative group modulo p.
        private_key (int): The participant's private secret.
        public_key (int): The participant's public value derived from the private key.
    """

    def __init__(self, p: str, g: str , secret: int) -> None:
        """
        Initializes the Diffie-Hellman instance with a prime number, generator, and private key.

        Args:
            p (int): A prime number used as the modulus.
            g (int): A generator for the multiplicative group modulo p.
            private_key (int): The participant's private secret.
        """
        # Convert string inputs to integers
        self.p = int(p)
        self.g = int(g)
        self.secret = int (secret) 
        
        # The shared secret will be calculated after exchanging public keys
        self.shared_secret = None

    def calculate_public_key(self) -> int:
        """
        Calculates the public key based on the private key.

        Returns:
            int: The calculated public key.
        """
        return pow(self.g, self.secret, self.p)

    def calculate_shared_secret(self, other_public_key: int) -> None:
        """
        Calculates the shared secret using the other participant's public key.

        Args:
            other_public_key (int): The public key received from the other participant.

        The calculated shared secret is stored in self.shared_secret.
        """
        # Calculate the shared secret using the other participant's public key
        self.shared_secret = pow(other_public_key, self.secret, self.p)

    def __str__(self) -> str:
        
        """
        Returns a string representation of the Diffie-Hellman instance.

        Returns:
            str: A string containing the prime number, generator, private key, public key, and shared secret.
        """
        return (f"Diffie-Hellman Key Exchange:\n"
                f"  Prime (p): {self.p}\n"
                f"  Generator (g): {self.g}\n"
                #f"  Private Key: {self.secret}\n"
                #f"  Public Key: {self.calculate_public_key()}\n"
               )
    
if __name__ == "__main__":
    # Example usage of the DH class
    # Public parameters (small values for demonstration)
    p = "23"  # A small prime number
    g = "5"   # A small generator

    # Alice's private key
    alice_secret = 6
    alice = DH(p, g, alice_secret)
    alice_public_key = alice.calculate_public_key()

    # Bob's private key
    bob_secret = 15
    bob = DH(p, g, bob_secret)
    bob_public_key = bob.calculate_public_key()

    # Exchange public keys and calculate shared secrets
    alice.calculate_shared_secret(bob_public_key)
    bob.calculate_shared_secret(alice_public_key)

    # Display results
    #print(alice)
    print(bob)
    
    print(f"Alice's Public Key: {alice_public_key}")
    print(f"Bob's Public Key: {bob_public_key}")
    print(f"Alice's Shared Secret: {alice.shared_secret}")
    print(f"Bob's Shared Secret: {bob.shared_secret}")

    # Verify that both participants calculated the same secret.
    if alice.shared_secret == bob.shared_secret:
        print(f"Shared secret successfully established.")
    else:
        print("Error: Shared secrets do not match.")