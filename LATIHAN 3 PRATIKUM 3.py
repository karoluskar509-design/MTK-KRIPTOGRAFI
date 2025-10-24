import tkinter as tk
from tkinter import messagebox

def konversi_hexa():
    hexa = entry_hexa.get()
    try:
        desimal = int(hexa, 16)
        biner = bin(desimal)[2:]
        oktal = oct(desimal)[2:]
        label_desimal.config(text=f"Desimal: {desimal}")
        label_biner.config(text=f"Biner: {biner}")
        label_oktal.config(text=f"Oktal: {oktal}")
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid! Gunakan angka 0-9 atau huruf A-F.")

def clear():
    entry_hexa.delete(0, tk.END)
    label_desimal.config(text="Desimal: ")
    label_biner.config(text="Biner: ")
    label_oktal.config(text="Oktal: ")

root = tk.Tk()
root.title("Konversi Hexadesimal ke Desimal, Biner & Oktal")
root.geometry("430x280")
root.config(bg="#f0f0f0")

tk.Label(root, text="KONVERSI HEXA", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(root, text="Masukkan Bilangan Hexadesimal:", bg="#f0f0f0").pack()
entry_hexa = tk.Entry(root, font=("Consolas", 12), width=25, justify="center")
entry_hexa.pack(pady=5)

tk.Button(root, text="Konversi", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), command=konversi_hexa).pack(pady=5)
tk.Button(root, text="Clear", bg="#f44336", fg="white", font=("Arial", 11, "bold"), command=clear).pack()

label_desimal = tk.Label(root, text="Desimal: ", bg="#f0f0f0", font=("Arial", 12))
label_desimal.pack(pady=10)
label_biner = tk.Label(root, text="Biner: ", bg="#f0f0f0", font=("Arial", 12))
label_biner.pack()
label_oktal = tk.Label(root, text="Oktal: ", bg="#f0f0f0", font=("Arial", 12))
label_oktal.pack()

root.mainloop()
