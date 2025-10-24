import tkinter as tk
from tkinter import messagebox

def konversi_biner():
    biner = entry_biner.get()
    try:
        desimal = int(biner, 2)
        hexa = hex(desimal)[2:].upper()
        label_desimal.config(text=f"Desimal: {desimal}")
        label_hexa.config(text=f"Hexadesimal: {hexa}")
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid! Masukkan hanya angka 0 dan 1.")

def clear():
    entry_biner.delete(0, tk.END)
    label_desimal.config(text="Desimal: ")
    label_hexa.config(text="Hexadesimal: ")

# GUI setup
root = tk.Tk()
root.title("Konversi Biner ke Desimal & Hexadesimal")
root.geometry("400x250")
root.config(bg="#f0f0f0")

tk.Label(root, text="KONVERSI BINER", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(root, text="Masukkan Bilangan Biner:", bg="#f0f0f0").pack()
entry_biner = tk.Entry(root, font=("Consolas", 12), width=25, justify="center")
entry_biner.pack(pady=5)

tk.Button(root, text="Konversi", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), command=konversi_biner).pack(pady=5)
tk.Button(root, text="Clear", bg="#f44336", fg="white", font=("Arial", 11, "bold"), command=clear).pack()

label_desimal = tk.Label(root, text="Desimal: ", bg="#f0f0f0", font=("Arial", 12))
label_desimal.pack(pady=10)
label_hexa = tk.Label(root, text="Hexadesimal: ", bg="#f0f0f0", font=("Arial", 12))
label_hexa.pack()

root.mainloop()
