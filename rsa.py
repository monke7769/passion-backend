# By: Shuban Pal
# Algorithm: RSA
# Project: CSP Passion Project
# Date: 2023

# DISCLAIMER: This implementations follows RSA and is not a custom algorithm. And neither is the miller-rabin test.


import random
import math

# Test whether or not number is prime
class rsa:
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
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

  
    # Compute r = n - 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # If it does not pass the miller rabin test, it is not prime. Else it is prime
    for _ in range(k):
        if not miller_rabin(n, d):
            return False
    return True

# Generate RSA bits (if p is a prime number)
def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if p % 2 == 0:
            p += 1
        if is_prime(p):
            return p

# Modular inverse must exist for decryption
def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("DNE: Modular inverse does not exist")
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

# Main rsa keygen algorithm
def rsa_keygen(bits=2048):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = mod_inverse(e, phi)
    return (n, e), (n, d)

# Encrypt with public key
def rsa_encrypt(public_key, plaintext):
    n, e = public_key
    cipher = pow(plaintext, e, n)
    return cipher

# Decrypt with private key
def rsa_decrypt(private_key, ciphertext):
    n, d = private_key
    plaintext = pow(ciphertext, d, n)
    return plaintext

if __name__ == "__main__":
    public_key, private_key = rsa_keygen(bits=2048)
    plaintext = input("Enter plaintext: ")
    plaintext = int.from_bytes(plaintext.encode(), byteorder='big')

    ciphertext = rsa_encrypt(public_key, plaintext)
    decrypted = rsa_decrypt(private_key, ciphertext)

    decrypted_text = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, byteorder='big').decode()

    print(f"Public Key (n, e): "+str(public_key))
    print(f"Private Key (n, d): "+str(private_key))
    print(f"Encrypted: "+str(ciphertext))
    print(f"Decrypted: "+str(decrypted_text))

