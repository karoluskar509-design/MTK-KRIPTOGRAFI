import tkinter as tk
from tkinter import messagebox

# === LATIHAN 1 : Kalkulator dengan input operator ===
def form1():
    def hitung():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            op = entry_op.get()
            if op == '+':
                hasil = a + b
            elif op == '-':
                hasil = a - b
            elif op == '*':
                hasil = a * b
            elif op == '/':
                if b == 0:
                    hasil = "Error: Pembagian nol!"
                else:
                    hasil = a / b
            else:
                hasil = "Operator tidak valid"
            label_hasil.config(text=f"Hasil: {hasil}")
        except ValueError:
            messagebox.showerror("Error", "Input harus angka!")

    win = tk.Toplevel(root)
    win.title("Latihan 1 - Kalkulator Operator")

    tk.Label(win, text="Angka 1:").grid(row=0, column=0)
    entry_a = tk.Entry(win)
    entry_a.grid(row=0, column=1)

    tk.Label(win, text="Angka 2:").grid(row=1, column=0)
    entry_b = tk.Entry(win)
    entry_b.grid(row=1, column=1)

    tk.Label(win, text="Operator (+, -, *, /):").grid(row=2, column=0)
    entry_op = tk.Entry(win)
    entry_op.grid(row=2, column=1)

    tk.Button(win, text="Hitung", command=hitung).grid(row=3, column=0, columnspan=2, pady=5)
    label_hasil = tk.Label(win, text="Hasil: ")
    label_hasil.grid(row=4, column=0, columnspan=2)


# === LATIHAN 2 : Kalkulator semua operasi langsung ===
def form2():
    def hitung_semua():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            hasil = (
                f"Penjumlahan : {a+b}\n"
                f"Pengurangan : {a-b}\n"
                f"Perkalian   : {a*b}\n"
                f"Pembagian   : {a/b if b != 0 else 'Error: nol!'}"
            )
            label_hasil.config(text=hasil)
        except ValueError:
            messagebox.showerror("Error", "Input harus angka!")

    win = tk.Toplevel(root)
    win.title("Latihan 2 - Kalkulator Semua Operasi")

    tk.Label(win, text="Angka 1:").grid(row=0, column=0)
    entry_a = tk.Entry(win)
    entry_a.grid(row=0, column=1)

    tk.Label(win, text="Angka 2:").grid(row=1, column=0)
    entry_b = tk.Entry(win)
    entry_b.grid(row=1, column=1)

    tk.Button(win, text="Hitung Semua", command=hitung_semua).grid(row=2, column=0, columnspan=2, pady=5)
    label_hasil = tk.Label(win, text="", justify="left")
    label_hasil.grid(row=3, column=0, columnspan=2)


# === LATIHAN 3 : Form Nilai Akademik ===
def form3():
    def hitung_nilai():
        try:
            sikap = float(entry_sikap.get())
            tugas = float(entry_tugas.get())
            uts = float(entry_uts.get())
            uas = float(entry_uas.get())

            nilai_akhir = (sikap*0.10) + (tugas*0.30) + (uts*0.25) + (uas*0.35)

            if 81 <= nilai_akhir <= 100:
                grade, bobot = "A", 4
            elif 76 <= nilai_akhir <= 80:
                grade, bobot = "B+", 3.5
            elif 71 <= nilai_akhir <= 75:
                grade, bobot = "B", 3
            elif 66 <= nilai_akhir <= 70:
                grade, bobot = "C+", 2.5
            elif 56 <= nilai_akhir <= 65:
                grade, bobot = "C", 2
            elif 46 <= nilai_akhir <= 55:
                grade, bobot = "D", 1
            else:
                grade, bobot = "E", 0

            ket = "Lulus" if nilai_akhir >= 56 else "Tidak Lulus"

            hasil_var.set(
                f"Total Nilai Akhir : {nilai_akhir:.2f}\n"
                f"Nilai Huruf       : {grade}\n"
                f"Bobot Nilai       : {bobot}\n"
                f"Keterangan        : {ket}"
            )
        except ValueError:
            messagebox.showerror("Error", "Input harus berupa angka!")

    def reset_form():
        entry_sikap.delete(0, tk.END)
        entry_tugas.delete(0, tk.END)
        entry_uts.delete(0, tk.END)
        entry_uas.delete(0, tk.END)
        hasil_var.set("")

    win = tk.Toplevel(root)
    win.title("Latihan 3 - Form Nilai Akademik")
    win.configure(bg="#f0f8ff")

    tk.Label(win, text="FORM PENILAIAN AKADEMIK", font=("Arial", 14, "bold"), bg="#4682b4", fg="white", pady=10).pack(fill="x")

    frame = tk.Frame(win, bg="#add8e6", padx=20, pady=20, bd=2, relief="ridge")
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="Nilai Sikap/Kehadiran (0-100):", bg="#add8e6").grid(row=0, column=0, sticky="w")
    entry_sikap = tk.Entry(frame); entry_sikap.grid(row=0, column=1)

    tk.Label(frame, text="Nilai Tugas (0-100):", bg="#add8e6").grid(row=1, column=0, sticky="w")
    entry_tugas = tk.Entry(frame); entry_tugas.grid(row=1, column=1)

    tk.Label(frame, text="Nilai UTS (0-100):", bg="#add8e6").grid(row=2, column=0, sticky="w")
    entry_uts = tk.Entry(frame); entry_uts.grid(row=2, column=1)

    tk.Label(frame, text="Nilai UAS (0-100):", bg="#add8e6").grid(row=3, column=0, sticky="w")
    entry_uas = tk.Entry(frame); entry_uas.grid(row=3, column=1)

    tk.Button(frame, text="Hitung Nilai Akhir", command=hitung_nilai, bg="#4682b4", fg="white").grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(frame, text="Reset", command=reset_form, bg="red", fg="white").grid(row=5, column=0, columnspan=2, pady=5)

    hasil_var = tk.StringVar()
    tk.Label(win, textvariable=hasil_var, justify="left", font=("Arial", 11), bg="#f0f8ff").pack(pady=10)


# === MENU UTAMA ===
root = tk.Tk()
root.title("Program Latihan")

tk.Label(root, text="Pilih Latihan", font=("Arial", 14, "bold"), pady=10).pack()

tk.Button(root, text="Form 1 - Kalkulator Operator", width=30, command=form1, bg="#4682b4", fg="white").pack(pady=5)
tk.Button(root, text="Form 2 - Kalkulator Semua Operasi", width=30, command=form2, bg="#4682b4", fg="white").pack(pady=5)
tk.Button(root, text="Form 3 - Penilaian Akademik", width=30, command=form3, bg="#4682b4", fg="white").pack(pady=5)

root.mainloop()
