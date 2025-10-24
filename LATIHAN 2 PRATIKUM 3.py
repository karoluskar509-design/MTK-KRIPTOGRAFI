import tkinter as tk
from tkinter import messagebox

def konversi_oktal():
    oktal = entry_oktal.get()
    try:
        desimal = int(oktal, 8)
        biner = bin(desimal)[2:]
        hexa = hex(desimal)[2:].upper()
        label_desimal.config(text=f"Desimal: {desimal}")
        label_biner.config(text=f"Biner: {biner}")
        label_hexa.config(text=f"Hexadesimal: {hexa}")
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid! Masukkan hanya angka 0-7.")

def clear():
    entry_oktal.delete(0, tk.END)
    label_desimal.config(text="Desimal: ")
    label_biner.config(text="Biner: ")
    label_hexa.config(text="Hexadesimal: ")

root = tk.Tk()
root.title("Konversi Oktal ke Desimal, Biner & Hexadesimal")
root.geometry("420x280")
root.config(bg="#f0f0f0")

tk.Label(root, text="KONVERSI OKTAL", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(root, text="Masukkan Bilangan Oktal:", bg="#f0f0f0").pack()
entry_oktal = tk.Entry(root, font=("Consolas", 12), width=25, justify="center")
entry_oktal.pack(pady=5)

tk.Button(root, text="Konversi", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), command=konversi_oktal).pack(pady=5)
tk.Button(root, text="Clear", bg="#f44336", fg="white", font=("Arial", 11, "bold"), command=clear).pack()

label_desimal = tk.Label(root, text="Desimal: ", bg="#f0f0f0", font=("Arial", 12))
label_desimal.pack(pady=10)
label_biner = tk.Label(root, text="Biner: ", bg="#f0f0f0", font=("Arial", 12))
label_biner.pack()
label_hexa = tk.Label(root, text="Hexadesimal: ", bg="#f0f0f0", font=("Arial", 12))
label_hexa.pack()

root.mainloop()
