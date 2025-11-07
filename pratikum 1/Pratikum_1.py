import tkinter as tk
from tkinter import messagebox

def hitung_nilai():
    try:
        # Ambil nilai dari entry
        sikap = float(entry_sikap.get())
        tugas = float(entry_tugas.get())
        uts = float(entry_uts.get())
        uas = float(entry_uas.get())

        # Hitung total nilai akhir berdasarkan bobot
        nilai_akhir = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)

        # Tentukan grade / huruf mutu
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

        # Tentukan keterangan lulus atau tidak
        keterangan = "Lulus" if nilai_akhir >= 56 else "Tidak Lulus"

        # Tampilkan hasil ke label
        hasil_var.set(
            f"Total Nilai Akhir : {nilai_akhir:.2f}\n"
            f"Nilai Huruf       : {grade}\n"
            f"Bobot Nilai       : {bobot}\n"
            f"Keterangan        : {keterangan}"
        )

    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")

def reset_form():
    entry_sikap.delete(0, tk.END)
    entry_tugas.delete(0, tk.END)
    entry_uts.delete(0, tk.END)
    entry_uas.delete(0, tk.END)
    hasil_var.set("")

# Buat jendela utama
root = tk.Tk()
root.title("Form Nilai Akhir Akademik")
root.configure(bg="#f0f8ff")  # background biru muda

# Judul
tk.Label(root, text="FORM PENILAIAN AKADEMIK", font=("Arial", 14, "bold"), bg="#4682b4", fg="white", pady=10).pack(fill="x")

# Frame utama
frame = tk.Frame(root, bg="#add8e6", padx=20, pady=20, bd=2, relief="ridge")
frame.pack(padx=20, pady=20)

# Label dan Entry
tk.Label(frame, text="Nilai Sikap/Kehadiran (0-100):", bg="#add8e6", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
entry_sikap = tk.Entry(frame)
entry_sikap.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Nilai Tugas (0-100):", bg="#add8e6", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
entry_tugas = tk.Entry(frame)
entry_tugas.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Nilai UTS (0-100):", bg="#add8e6", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
entry_uts = tk.Entry(frame)
entry_uts.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Nilai UAS (0-100):", bg="#add8e6", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=5)
entry_uas = tk.Entry(frame)
entry_uas.grid(row=3, column=1, pady=5)

# Tombol
tk.Button(frame, text="Hitung Nilai Akhir", command=hitung_nilai, bg="#4682b4", fg="white", font=("Arial", 10, "bold")).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(frame, text="Reset", command=reset_form, bg="red", fg="white", font=("Arial", 10, "bold")).grid(row=5, column=0, columnspan=2, pady=5)

# Label hasil
hasil_var = tk.StringVar()
tk.Label(root, textvariable=hasil_var, justify="left", font=("Arial", 11), bg="#f0f8ff", fg="black").pack(pady=10)

# Jalankan aplikasi
root.mainloop()
