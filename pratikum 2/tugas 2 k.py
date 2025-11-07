import tkinter as tk
from tkinter import messagebox

def kalkulasi():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        op = operator_var.get()

        if op == '+':
            hasil = a + b
        elif op == '-':
            hasil = a - b
        elif op == '*':
            hasil = a * b
        elif op == '/':
            if b == 0:
                messagebox.showerror("Error", "Pembagian dengan nol tidak diperbolehkan.")
                return
            hasil = a / b
        elif op == '%':
            if b == 0:
                messagebox.showerror("Error", "Modulus dengan nol tidak diperbolehkan.")
                return
            hasil = a % b
        elif op == '**':
            hasil = a ** b
        else:
            messagebox.showerror("Error", "Operator tidak dikenali.")
            return

        label_hasil.config(text=f"Hasil: {a} {op} {b} = {hasil}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk A dan B.")

def keluar():
    root.destroy()

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator GUI (Latihan 1)")
root.geometry("350x300")
root.resizable(False, False)

# Label dan Entry
tk.Label(root, text="Masukkan nilai A:").pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Masukkan nilai B:").pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack()

# Pilihan operator
tk.Label(root, text="Pilih Operator:").pack(pady=5)
operator_var = tk.StringVar(value='+')
ops = ['+', '-', '*', '/', '%', '**']
for op in ops:
    tk.Radiobutton(root, text=op, variable=operator_var, value=op).pack(anchor='w', padx=100)

# Tombol hitung dan keluar
tk.Button(root, text="Hitung", command=kalkulasi, bg="#4CAF50", fg="white", width=15).pack(pady=10)
tk.Button(root, text="Keluar", command=keluar, bg="#f44336", fg="white", width=15).pack()

# Label hasil
label_hasil = tk.Label(root, text="Hasil: ", font=("Arial", 11, "bold"))
label_hasil.pack(pady=10)

root.mainloop()
