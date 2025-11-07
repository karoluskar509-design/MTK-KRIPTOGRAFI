import tkinter as tk
from tkinter import messagebox, ttk

# ==========================================================
# FUNGSI KALKULATOR BERULANG
# ==========================================================
def kalkulasi(a, b, op):
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                return "Error: Pembagian dengan nol."
            return a / b
        elif op == '%':
            if b == 0:
                return "Error: Modulus dengan nol."
            return a % b
        elif op == '**':
            return a ** b
        else:
            return "Operator tidak dikenali."
    except Exception as e:
        return f"Terjadi error: {e}"

# ==========================================================
# FUNGSI UNTUK MENU 1: KALKULATOR BERULANG
# ==========================================================
def tampil_kalkulator_berulang():
    clear_frame()
    tk.Label(frame_main, text="KALKULATOR BERULANG (Y/T)", font=("Arial", 14, "bold")).pack(pady=10)

    entry_a = tk.Entry(frame_main, width=10)
    entry_b = tk.Entry(frame_main, width=10)
    entry_op = tk.Entry(frame_main, width=10)
    label_hasil = tk.Label(frame_main, text="Hasil: ", font=("Arial", 12))

    tk.Label(frame_main, text="Nilai A:").pack()
    entry_a.pack()
    tk.Label(frame_main, text="Nilai B:").pack()
    entry_b.pack()
    tk.Label(frame_main, text="Operator (+, -, *, /, %, **):").pack()
    entry_op.pack()

    def hitung():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            op = entry_op.get()
            hasil = kalkulasi(a, b, op)
            label_hasil.config(text=f"Hasil: {a} {op} {b} = {hasil}")
        except ValueError:
            messagebox.showerror("Kesalahan Input", "Masukkan angka yang valid!")

    tk.Button(frame_main, text="Hitung", bg="#00796b", fg="white", command=hitung).pack(pady=5)
    label_hasil.pack(pady=10)

# ==========================================================
# FUNGSI UNTUK MENU 2: KALKULATOR IF/ELIF
# ==========================================================
def tampil_kalkulator_if():
    clear_frame()
    tk.Label(frame_main, text="KALKULATOR IF/ELIF", font=("Arial", 14, "bold")).pack(pady=10)

    entry_a = tk.Entry(frame_main, width=10)
    entry_b = tk.Entry(frame_main, width=10)
    combo_op = ttk.Combobox(frame_main, values=["+", "-", "*", "/", "%", "**"], width=8)
    label_hasil = tk.Label(frame_main, text="Hasil: ", font=("Arial", 12))

    tk.Label(frame_main, text="Nilai A:").pack()
    entry_a.pack()
    tk.Label(frame_main, text="Nilai B:").pack()
    entry_b.pack()
    tk.Label(frame_main, text="Pilih Operator:").pack()
    combo_op.pack()

    def hitung_if():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            op = combo_op.get()

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
                messagebox.showerror("Error", "Operator tidak valid.")
                return

            label_hasil.config(text=f"Hasil: {a} {op} {b} = {hasil}")
        except ValueError:
            messagebox.showerror("Kesalahan Input", "Masukkan angka yang valid!")

    tk.Button(frame_main, text="Hitung", bg="#0288d1", fg="white", command=hitung_if).pack(pady=5)
    label_hasil.pack(pady=10)

# ==========================================================
# FUNGSI UNTUK MENU 3: PEMERIKSA NILAI X, Y, Z
# ==========================================================
def tampil_pemeriksa_xyz():
    clear_frame()
    tk.Label(frame_main, text="PEMERIKSA NILAI X, Y, Z", font=("Arial", 14, "bold")).pack(pady=10)

    entry_x = tk.Entry(frame_main, width=10)
    entry_y = tk.Entry(frame_main, width=10)
    entry_z = tk.Entry(frame_main, width=10)
    text_hasil = tk.Text(frame_main, height=10, width=45)

    tk.Label(frame_main, text="Masukkan nilai X:").pack()
    entry_x.pack()
    tk.Label(frame_main, text="Masukkan nilai Y:").pack()
    entry_y.pack()
    tk.Label(frame_main, text="Masukkan nilai Z:").pack()
    entry_z.pack()

    def periksa():
        text_hasil.delete("1.0", tk.END)
        try:
            x = int(entry_x.get())
            y = int(entry_y.get())
            z = int(entry_z.get())

            if x >= 18 and x <= 30:
                text_hasil.insert(tk.END, "x berada di antara 18 dan 30\n")
            else:
                text_hasil.insert(tk.END, "x tidak berada di antara 18 dan 30\n")

            if y < 10 or y > 20:
                text_hasil.insert(tk.END, "y berada di luar rentang 10 hingga 20\n")
            else:
                text_hasil.insert(tk.END, "y berada di dalam rentang 10 hingga 20\n")

            if z == 5:
                text_hasil.insert(tk.END, "z sama dengan 5\n")
            else:
                text_hasil.insert(tk.END, "z tidak sama dengan 5\n")

            if x != y:
                text_hasil.insert(tk.END, "x tidak sama dengan y\n")
            else:
                text_hasil.insert(tk.END, "x sama dengan y\n")

            if x > y:
                text_hasil.insert(tk.END, "x lebih besar dari y\n")
            else:
                text_hasil.insert(tk.END, "x tidak lebih besar dari y\n")

            if z < y:
                text_hasil.insert(tk.END, "z lebih kecil dari y\n")
            else:
                text_hasil.insert(tk.END, "z tidak lebih kecil dari y\n")

            if y >= 15 and z <= 5:
                text_hasil.insert(tk.END, "y >= 15 dan z <= 5\n")
        except ValueError:
            messagebox.showerror("Kesalahan Input", "Masukkan nilai numerik (bilangan bulat)!")

    tk.Button(frame_main, text="Periksa", bg="#00796b", fg="white", command=periksa).pack(pady=5)
    text_hasil.pack(pady=10)

# ==========================================================
# FUNGSI UNTUK MEMBERSIHKAN FRAME
# ==========================================================
def clear_frame():
    for widget in frame_main.winfo_children():
        widget.destroy()

# ==========================================================
# FRAME UTAMA PROGRAM
# ==========================================================
window = tk.Tk()
window.title("Program Gabungan Kalkulator dan Pemeriksa Nilai")
window.geometry("500x550")
window.config(bg="#e0f7fa")

# Judul Utama
judul = tk.Label(window, text="PROGRAM LATIHAN GABUNGAN", font=("Arial", 16, "bold"), bg="#006064", fg="white", pady=10)
judul.pack(fill=tk.X)

# Frame tombol menu
frame_menu = tk.Frame(window, bg="#b2ebf2")
frame_menu.pack(pady=10)

tk.Button(frame_menu, text="Kalkulator Berulang", width=18, command=tampil_kalkulator_berulang).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_menu, text="Kalkulator If/Elif", width=18, command=tampil_kalkulator_if).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_menu, text="Pemeriksa X, Y, Z", width=18, command=tampil_pemeriksa_xyz).grid(row=0, column=2, padx=5, pady=5)

# Frame utama konten
frame_main = tk.Frame(window, bg="#e0f7fa")
frame_main.pack(pady=20)

# Tombol keluar
tk.Button(window, text="Keluar", bg="#d32f2f", fg="white", width=15, command=window.destroy).pack(pady=15)

# Jalankan program
window.mainloop()
