import random
import math

# Mengecek bilangan prima
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Mengambil bilangan prima acak
def random_prime(a, b):
    while True:
        x = random.randint(a, b)
        if is_prime(x):
            return x

# Mencari invers modulo
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

print("=== RSA LATIHAN 2 (p, q, e acak) ===")

# 1. Pilih p dan q acak
p = random_prime(50, 200)
q = random_prime(50, 200)

print(f"p = {p}")
print(f"q = {q}")

# 2. Hitung n dan phi
n = p * q
phi = (p - 1) * (q - 1)

print(f"n = {n}")
print(f"phi(n) = {phi}")

# 3. Pilih e yang relatif prima dengan phi
while True:
    e = random.randint(2, phi-1)
    if math.gcd(e, phi) == 1:
        break

print(f"e = {e}")

# 4. Hitung d
d = mod_inverse(e, phi)
print(f"d = {d}")

print("\n=== Kunci RSA ===")
print(f"Public Key  = ({e}, {n})")
print(f"Private Key = ({d}, {n})")

# 5. Input plaintext (teks)
plaintext = input("\nMasukkan plaintext (teks): ")

# 6. Enkripsi per karakter
cipher = []
for ch in plaintext:
    m = ord(ch)              # konversi ke ASCII
    c = pow(m, e, n)         # RSA encrypt
    cipher.append(c)

print("\nCiphertext (angka):")
print(cipher)

# 7. Dekripsi
decrypted_text = ""
for c in cipher:
    m = pow(c, d, n)
    decrypted_text += chr(m)

print("\nHasil Dekripsi:")
print(decrypted_text)