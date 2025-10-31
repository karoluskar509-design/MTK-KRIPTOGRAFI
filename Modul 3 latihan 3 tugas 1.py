import tkinter as tk
from tkinter import messagebox
import itertools

# --- Fungsi faktorial ---
def faktorial(x):
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

# --- Fungsi kombinasi (nilai matematis) ---
def kombinasi(n, r):
    if r > n:
        return 0
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

# --- Fungsi untuk menampilkan kombinasi huruf ---
def tampilkan_kombinasi():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        if n <= 0 or r <= 0:
            messagebox.showwarning("Peringatan", "n dan r harus lebih dari 0!")
            return
        if r > n:
            messagebox.showerror("Error", "r tidak boleh lebih besar dari n!")
            return
    except:
        messagebox.showerror("Error", "Masukkan nilai n dan r yang valid!")
        return

    # Hitung nilai kombinasi
    hasil_nilai = kombinasi(n, r)

    # Buat daftar huruf inisial (A, B, C, D, ...)
    huruf = [chr(65 + i) for i in range(n)]

    # Buat semua kombinasi menggunakan itertools
    semua_kombinasi = list(itertools.combinations(huruf, r))

    # Tampilkan hasil
    text_hasil.delete(1.0, tk.END)
    text_hasil.insert(tk.END, f"Jumlah kombinasi C({n}, {r}) = {hasil_nilai}\n\n")
    text_hasil.insert(tk.END, "Daftar Kombinasi:\n")
    for i, komb in enumerate(semua_kombinasi, 1):
        text_hasil.insert(tk.END, f"{i}. {komb}\n")

# --- GUI Setup ---
root = tk.Tk()
root.title("Program Kombinasi - GUI")
root.geometry("500x500")

tk.Label(root, text="=== PERHITUNGAN KOMBINASI ===", font=("Arial", 12, "bold")).pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=5)

tk.Label(frame_input, text="Masukkan jumlah total objek (n):").grid(row=0, column=0, padx=5, pady=5)
entry_n = tk.Entry(frame_input, width=10)
entry_n.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Masukkan jumlah objek yang dipilih (r):").grid(row=1, column=0, padx=5, pady=5)
entry_r = tk.Entry(frame_input, width=10)
entry_r.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Hitung Kombinasi", command=tampilkan_kombinasi, bg="lightblue").pack(pady=10)

text_hasil = tk.Text(root, height=20, width=60)
text_hasil.pack()

root.mainloop()
