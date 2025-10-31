import tkinter as tk
from tkinter import messagebox
import itertools

def atur_buku():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
    except:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk n dan r!")
        return

    buku = [f"B{i+1}" for i in range(n)]
    rak = [f"R{j+1}" for j in range(r)]
    semua_cara = list(itertools.product(rak, repeat=n))

    text_hasil.delete(1.0, tk.END)
    text_hasil.insert(tk.END, f"Total cara menata {n} buku di {r} rak = {len(semua_cara)}\n\n")

    for i, cara in enumerate(semua_cara, 1):
        text_hasil.insert(tk.END, f"{i}. ")
        for b, r in zip(buku, cara):
            text_hasil.insert(tk.END, f"{b}->{r} ")
        text_hasil.insert(tk.END, "\n")

# GUI Setup
root = tk.Tk()
root.title("Pengaturan Buku di Rak - GUI")
root.geometry("600x450")

tk.Label(root, text="Masukkan jumlah buku (n):").pack(pady=5)
entry_n = tk.Entry(root, width=10)
entry_n.pack()

tk.Label(root, text="Masukkan jumlah rak (r):").pack(pady=5)
entry_r = tk.Entry(root, width=10)
entry_r.pack()

tk.Button(root, text="Hitung Semua Cara", bg="lightgreen", command=atur_buku).pack(pady=10)

text_hasil = tk.Text(root, height=20, width=70)
text_hasil.pack()

root.mainloop()
