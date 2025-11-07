import tkinter as tk
from tkinter import messagebox, scrolledtext

# ==============================
# FUNGSI UTAMA VIGENERE
# ==============================

def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

# === Enkripsi ===
def encrypt(text, key):
    hasil = []
    key = generate_key(text, key)
    proses = "\n=== PROSES ENKRIPSI ===\n"
    proses += f"Teks Asli : {text}\nKunci     : {key}\n\n"

    for i in range(len(text)):
        if text[i].isalpha():
            x = (ord(text[i].upper()) + ord(key[i].upper())) % 26
            x += ord('A')
            encrypted_char = chr(x)
            hasil.append(encrypted_char)

            proses += (f"[{i+1}] {text[i]} + {key[i]} → "
                       f"({ord(text[i].upper()) - 65} + {ord(key[i].upper()) - 65}) % 26 "
                       f"= {x - 65} → {encrypted_char}\n")
        else:
            hasil.append(text[i])
            proses += f"[{i+1}] {text[i]} (non-huruf, tidak berubah)\n"

    cipher_result = "".join(hasil)
    proses += f"\nHasil Enkripsi: {cipher_result}\n"
    return cipher_result, proses

# === Dekripsi ===
def decrypt(cipher_text, key):
    hasil = []
    key = generate_key(cipher_text, key)
    proses = "\n=== PROSES DEKRIPSI ===\n"
    proses += f"Teks Enkripsi : {cipher_text}\nKunci          : {key}\n\n"

    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            x = (ord(cipher_text[i].upper()) - ord(key[i].upper()) + 26) % 26
            x += ord('A')
            decrypted_char = chr(x)
            hasil.append(decrypted_char)

            proses += (f"[{i+1}] {cipher_text[i]} - {key[i]} → "
                       f"({ord(cipher_text[i].upper()) - 65} - {ord(key[i].upper()) - 65} + 26) % 26 "
                       f"= {x - 65} → {decrypted_char}\n")
        else:
            hasil.append(cipher_text[i])
            proses += f"[{i+1}] {cipher_text[i]} (non-huruf, tidak berubah)\n"

    plain_result = "".join(hasil)
    proses += f"\nHasil Dekripsi: {plain_result}\n"
    return plain_result, proses

# ==============================
# BAGIAN GUI (Tkinter)
# ==============================

def proses_enkripsi():
    text = entry_text.get().upper()
    key = entry_key.get().upper()
    if not text or not key:
        messagebox.showwarning("Peringatan", "Masukkan teks dan kunci terlebih dahulu!")
        return
    hasil, proses = encrypt(text, key)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, proses)

def proses_dekripsi():
    text = entry_text.get().upper()
    key = entry_key.get().upper()
    if not text or not key:
        messagebox.showwarning("Peringatan", "Masukkan teks dan kunci terlebih dahulu!")
        return
    hasil, proses = decrypt(text, key)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, proses)

# ==============================
# DESAIN GUI
# ==============================

root = tk.Tk()
root.title("🔐 Vigenere Cipher (GUI dengan Proses)")
root.geometry("700x600")
root.resizable(False, False)

lbl_title = tk.Label(root, text="🔐 PROGRAM VIGENERE CIPHER", font=("Arial", 14, "bold"))
lbl_title.pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

lbl_text = tk.Label(frame_input, text="Masukkan Teks:")
lbl_text.grid(row=0, column=0, padx=5, sticky="w")
entry_text = tk.Entry(frame_input, width=50)
entry_text.grid(row=0, column=1, padx=5)

lbl_key = tk.Label(frame_input, text="Masukkan Kunci:")
lbl_key.grid(row=1, column=0, padx=5, sticky="w")
entry_key = tk.Entry(frame_input, width=50)
entry_key.grid(row=1, column=1, padx=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_encrypt = tk.Button(frame_buttons, text="🔒 Enkripsi", width=15, bg="#4CAF50", fg="white", command=proses_enkripsi)
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(frame_buttons, text="🔓 Dekripsi", width=15, bg="#2196F3", fg="white", command=proses_dekripsi)
btn_decrypt.grid(row=0, column=1, padx=10)

lbl_output = tk.Label(root, text="Proses dan Hasil:")
lbl_output.pack()

output_box = scrolledtext.ScrolledText(root, width=80, height=25, wrap=tk.WORD)
output_box.pack(pady=5)

btn_exit = tk.Button(root, text="Keluar", width=10, bg="#f44336", fg="white", command=root.destroy)
btn_exit.pack(pady=10)

root.mainloop()
