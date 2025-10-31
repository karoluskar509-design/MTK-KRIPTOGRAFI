import tkinter as tk
from tkinter import ttk, messagebox
import itertools

def permutasi_menyeluruh(data):
    return list(itertools.permutations(data))

def permutasi_sebagian(data, k):
    return list(itertools.permutations(data, k))

def permutasi_keliling(data):
    if len(data) == 1:
        return [data]
    pertama = data[0]
    sisa = list(itertools.permutations(data[1:]))
    return [[pertama] + list(perm) for perm in sisa]

def permutasi_berkelompok(grup):
    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru
    return hasil

def hitung_permutasi():
    jenis = combo.get()
    data = entry_data.get().split()
    hasil.delete(1.0, tk.END)

    if not data:
        messagebox.showwarning("Peringatan", "Masukkan elemen terlebih dahulu!")
        return

    if jenis == "Permutasi Menyeluruh":
        res = permutasi_menyeluruh(data)

    elif jenis == "Permutasi Sebagian":
        try:
            k = int(entry_k.get())
        except:
            messagebox.showerror("Error", "Masukkan nilai k yang valid!")
            return
        res = permutasi_sebagian(data, k)

    elif jenis == "Permutasi Keliling":
        res = permutasi_keliling(data)

    elif jenis == "Permutasi Berkelompok":
        grup_text = entry_data.get().split(";")
        grup = [g.split() for g in grup_text]
        res = permutasi_berkelompok(grup)

    else:
        messagebox.showerror("Error", "Jenis permutasi tidak dikenal!")
        return

    for i, r in enumerate(res, 1):
        hasil.insert(tk.END, f"{i}. {r}\n")

# GUI Setup
root = tk.Tk()
root.title("Program Permutasi - GUI")
root.geometry("550x450")

tk.Label(root, text="Pilih Jenis Permutasi:").pack(pady=5)
combo = ttk.Combobox(root, values=[
    "Permutasi Menyeluruh",
    "Permutasi Sebagian",
    "Permutasi Keliling",
    "Permutasi Berkelompok"
])
combo.current(0)
combo.pack()

tk.Label(root, text="Masukkan Elemen (pisahkan spasi / untuk berkelompok pisahkan dengan ;)").pack(pady=5)
entry_data = tk.Entry(root, width=50)
entry_data.pack()

tk.Label(root, text="Masukkan k (jika diperlukan)").pack(pady=5)
entry_k = tk.Entry(root, width=10)
entry_k.pack()

tk.Button(root, text="Hitung Permutasi", command=hitung_permutasi, bg="lightblue").pack(pady=10)

hasil = tk.Text(root, height=15, width=60)
hasil.pack()

root.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
import itertools

def permutasi_menyeluruh(data):
    return list(itertools.permutations(data))

def permutasi_sebagian(data, k):
    return list(itertools.permutations(data, k))

def permutasi_keliling(data):
    if len(data) == 1:
        return [data]
    pertama = data[0]
    sisa = list(itertools.permutations(data[1:]))
    return [[pertama] + list(perm) for perm in sisa]

def permutasi_berkelompok(grup):
    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru
    return hasil

def hitung_permutasi():
    jenis = combo.get()
    data = entry_data.get().split()
    hasil.delete(1.0, tk.END)

    if not data:
        messagebox.showwarning("Peringatan", "Masukkan elemen terlebih dahulu!")
        return

    if jenis == "Permutasi Menyeluruh":
        res = permutasi_menyeluruh(data)

    elif jenis == "Permutasi Sebagian":
        try:
            k = int(entry_k.get())
        except:
            messagebox.showerror("Error", "Masukkan nilai k yang valid!")
            return
        res = permutasi_sebagian(data, k)

    elif jenis == "Permutasi Keliling":
        res = permutasi_keliling(data)

    elif jenis == "Permutasi Berkelompok":
        grup_text = entry_data.get().split(";")
        grup = [g.split() for g in grup_text]
        res = permutasi_berkelompok(grup)

    else:
        messagebox.showerror("Error", "Jenis permutasi tidak dikenal!")
        return

    for i, r in enumerate(res, 1):
        hasil.insert(tk.END, f"{i}. {r}\n")

# GUI Setup
root = tk.Tk()
root.title("Program Permutasi - GUI")
root.geometry("550x450")

tk.Label(root, text="Pilih Jenis Permutasi:").pack(pady=5)
combo = ttk.Combobox(root, values=[
    "Permutasi Menyeluruh",
    "Permutasi Sebagian",
    "Permutasi Keliling",
    "Permutasi Berkelompok"
])
combo.current(0)
combo.pack()

tk.Label(root, text="Masukkan Elemen (pisahkan spasi / untuk berkelompok pisahkan dengan ;)").pack(pady=5)
entry_data = tk.Entry(root, width=50)
entry_data.pack()

tk.Label(root, text="Masukkan k (jika diperlukan)").pack(pady=5)
entry_k = tk.Entry(root, width=10)
entry_k.pack()

tk.Button(root, text="Hitung Permutasi", command=hitung_permutasi, bg="lightblue").pack(pady=10)

hasil = tk.Text(root, height=15, width=60)
hasil.pack()

root.mainloop()
