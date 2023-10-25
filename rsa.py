# By: Shuban Pal
# Algorithm: RSA
# Project: CSP Passion Project
# Date: 2023

# DISCLAIMER: This implementations follows RSA and is not a custom algorithm. And neither is the miller-rabin test.

import random

class RSA:
    def __init__(self, bits=2048):
        self.bits = bits
        self.public_key, self.private_key = self.rsa_keygen(bits)

    @staticmethod
    def is_prime(n, k=5):
        if n <= 1:
            return False
        if n <= 3:
            return True
        # Miler-Rabin primality test algorithm
        def miller_rabin(n, d):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                return True
            for _ in range(k - 1):  # Fix variable name 'k'
                x = pow(x, 2, n)
                if x == n - 1:
                    return True
            return False

        # Compute r = n - 1
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2
        # If it does not pass the miller rabin test, it is not prime
        for _ in range(k):
            if not miller_rabin(n, d):
                return False
        return True

    @staticmethod
    def generate_prime(bits):
        while True:
            p = random.getrandbits(bits)
            if p % 2 == 0:
                p += 1
            if RSA.is_prime(p):  # If it is a prime number, return it
                return p

    @staticmethod
    def mod_inverse(a, m):
        g, x, y = RSA.extended_gcd(a, m)  # Might be slow
        if g != 1:
            raise ValueError("DNE: Modular inverse does not exist")
        return x % m

    @staticmethod
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = RSA.extended_gcd(b % a, a)  # Call extended_gcd as a static method
            return (g, y - (b // a) * x, x)

    def rsa_keygen(self, bits):
        p = RSA.generate_prime(bits)  # Let P and Q be random prime numbers
        q = RSA.generate_prime(bits)  
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 65537
        d = RSA.mod_inverse(e, phi)  # Call mod_inverse as a static method
        return (n, e), (n, d)

    def rsa_encrypt(self, plaintext):
        n, e = self.public_key  # Access public_key as an instance attribute
        cipher = pow(plaintext, e, n)
        return cipher

    def rsa_decrypt(self, ciphertext):
        n, d = self.private_key  # Access private_key as an instance attribute
        plaintext = pow(ciphertext, d, n)
        return plaintext

if __name__ == "__main__":
    rsa = RSA(bits=2048)
    plaintext = input("Enter plaintext: ")
    plaintext = int.from_bytes(plaintext.encode(), byteorder='big')

    ciphertext = rsa.rsa_encrypt(plaintext)
    decrypted = rsa.rsa_decrypt(ciphertext)

    decrypted_text = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, byteorder='big').decode()

    print(f"Public Key (n, e): {rsa.public_key}")
    print(f"Private Key (n, d): {rsa.private_key}")
    print(f"Encrypted: {ciphertext}")
    print(f"Decrypted: {decrypted_text}")
