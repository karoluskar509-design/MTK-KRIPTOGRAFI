import tkinter as tk
from tkinter import messagebox

def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext

def proses_enkripsi():
    plaintext = entry_plaintext.get().upper()
    aturan_input = entry_aturan.get().upper()
    
    try:
        aturan_pairs = [pair.strip() for pair in aturan_input.split(',')]
        aturan = {}
        for pair in aturan_pairs:
            k, v = pair.split(':')
            aturan[k.strip()] = v.strip()
    except:
        messagebox.showerror("Error", "Format aturan salah! Gunakan format seperti: A:B, B:C, C:D")
        return
    
    ciphertext = substitusi_cipher(plaintext, aturan)
    entry_ciphertext.delete(0, tk.END)
    entry_ciphertext.insert(0, ciphertext)

# GUI Window
root = tk.Tk()
root.title("Program Substitusi Cipher")
root.geometry("450x300")
root.resizable(False, False)

# Label dan Entry
tk.Label(root, text="Substitusi Cipher", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Masukkan Plaintext:").grid(row=0, column=0, sticky="w", pady=5)
entry_plaintext = tk.Entry(frame, width=40)
entry_plaintext.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Masukkan Aturan (format A:B, B:C, ...):").grid(row=1, column=0, sticky="w", pady=5)
entry_aturan = tk.Entry(frame, width=40)
entry_aturan.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Hasil Ciphertext:").grid(row=2, column=0, sticky="w", pady=5)
entry_ciphertext = tk.Entry(frame, width=40)
entry_ciphertext.grid(row=2, column=1, pady=5)

# Tombol
btn_enkripsi = tk.Button(root, text="Enkripsi", width=15, command=proses_enkripsi)
btn_enkripsi.pack(pady=10)

root.mainloop()
