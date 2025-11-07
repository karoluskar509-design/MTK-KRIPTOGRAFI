import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memproses ekspresi
def proses_ekspresi():
    ekspresi = entry_input.get()
    try:
        # Gunakan eval untuk menghitung ekspresi
        hasil = eval(ekspresi)
        label_hasil.config(text=f"Hasil: {hasil}")
    except Exception as e:
        messagebox.showerror("Error", f"Ekspresi tidak valid!\n{e}")

# Fungsi untuk membersihkan input dan output
def clear():
    entry_input.delete(0, tk.END)
    label_hasil.config(text="Hasil: ")

# Membuat window utama
root = tk.Tk()
root.title("Kalkulator Hybrid")
root.geometry("400x250")
root.configure(bg="#f2f2f2")

# Judul
label_judul = tk.Label(root, text="Tugas Praktikum 2\nKalkulator Hybrid", 
                       font=("Arial", 14, "bold"), bg="#f2f2f2")
label_judul.pack(pady=10)

# Label input
label_input = tk.Label(root, text="Input (Ekspresi):", font=("Arial", 11), bg="#f2f2f2")
label_input.pack()

# Kolom input
entry_input = tk.Entry(root, font=("Consolas", 12), width=30, justify="center")
entry_input.pack(pady=5)

# Tombol proses dan clear
frame_tombol = tk.Frame(root, bg="#f2f2f2")
frame_tombol.pack(pady=10)

btn_proses = tk.Button(frame_tombol, text="Proses", font=("Arial", 11, "bold"), 
                       bg="#4CAF50", fg="white", width=10, command=proses_ekspresi)
btn_proses.grid(row=0, column=0, padx=5)

btn_clear = tk.Button(frame_tombol, text="Clear", font=("Arial", 11, "bold"), 
                      bg="#f44336", fg="white", width=10, command=clear)
btn_clear.grid(row=0, column=1, padx=5)

# Label hasil
label_hasil = tk.Label(root, text="Hasil: ", font=("Arial", 12, "bold"), bg="#f2f2f2", fg="blue")
label_hasil.pack(pady=15)

# Jalankan GUI
root.mainloop()
