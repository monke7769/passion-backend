# By: Shuban Pal
# Algorithm: RSA
# Project: CSP Passion Project
# Date: 2023

# DISCLAIMER: Work in progress, 
# TODO:
# - Implement random prime selection
# - Fix pubkeygen and privkeygen

# Segments like check_composite were inspired by AI


import math
import random
class rsa:
    def is_prime(n, k=5):
        if n <= 1:
            return False
        if n <= 3:
            return True

        def check_composite(a, d, n, s):
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                return False
            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    return False
            return True

        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2

        for _ in range(k):
            a = random.randint(2, n - 2)
            if check_composite(a, d, n, r):
                return False
        return True

    def genprime(n):
        while True:
            p = random.getrandbits(n)
            if is_prime(p):
                return p

    def mod_inverse(a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1

    def rsa():
        text = input("Enter plaintext: ")
        n = 1024  
        P = genprime(n)
        Q = genprime(n)
        key = P * Q
        phi = (P - 1) * (Q - 1)

        e = 65537
        if math.gcd(e, phi) != 1:
            return

        d = mod_inverse(e, phi)

        num = ""
        for char in text:
            num += str(ord(char))
        num = int(num)

        pubkey = pow(num, e, key)
        decrypted = pow(pubkey, d, key)

        print(f"Public Key (e, key): ({e}, {key})")
        print(f"Private Key (d, key): ({d}, {key})")
        print(f"Encrypted: {pubkey}")
        print(f"Decrypted: {decrypted}")
    def encryption(text):
        n = 1024  
        P = genprime(n)
        Q = genprime(n)
        key = P * Q
        phi = (P - 1) * (Q - 1)

        e = 65537
        if math.gcd(e, phi) != 1:
            return

        d = mod_inverse(e, phi)

        num = ""
        for char in text:
            num += str(ord(char))
        num = int(num)

        pubkey = pow(num, e, key)
        decrypted = pow(pubkey, d, key)
        return pubkey
    # if __name__ == "__main__":
    #     rsa()
