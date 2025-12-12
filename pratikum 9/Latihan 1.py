# Latihan 1: RSA p, q, e tetap

# Diketahui
p = 17
q = 11
e = 7

print("=== RSA LATIHAN 1 (p, q, e tetap) ===")
print(f"p = {p}, q = {q}, e = {e}")

# 1. Hitung n
n = p * q
print(f"n = p * q = {n}")

# 2. Hitung phi(n)
phi = (p - 1) * (q - 1)
print(f"phi(n) = (p-1)*(q-1) = {phi}")

# 3. Cari d (modular inverse)
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

d = mod_inverse(e, phi)
print(f"d = {d}")

# 4. Enkripsi & Dekripsi
plaintext = int(input("Masukkan plaintext (angka): "))
cipher = pow(plaintext, e, n)
decrypted = pow(cipher, d, n)

print(f"Ciphertext = {cipher}")
print(f"Hasil Dekripsi = {decrypted}")