# Program Menghitung Nilai Akhir Akademik

# Input nilai dari pengguna
sikap = float(input("Masukkan nilai Sikap/Kehadiran (0-100): "))
tugas = float(input("Masukkan nilai Tugas (0-100): "))
uts = float(input("Masukkan nilai UTS (0-100): "))
uas = float(input("Masukkan nilai UAS (0-100): "))

# Hitung total nilai akhir berdasarkan bobot
nilai_akhir = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)

# Tentukan grade / huruf mutu
if 81 <= nilai_akhir <= 100:
    grade = "A"
    bobot = 4
elif 76 <= nilai_akhir <= 80:
    grade = "B+"
    bobot = 3.5
elif 71 <= nilai_akhir <= 75:
    grade = "B"
    bobot = 3
elif 66 <= nilai_akhir <= 70:
    grade = "C+"
    bobot = 2.5
elif 56 <= nilai_akhir <= 65:
    grade = "C"
    bobot = 2
elif 46 <= nilai_akhir <= 55:
    grade = "D"
    bobot = 1
else:
    grade = "E"
    bobot = 0

# Tentukan keterangan lulus atau tidak
if nilai_akhir >= 56:
    keterangan = "Lulus"
else:
    keterangan = "Tidak Lulus"

# Tampilkan hasil
print("\n=== HASIL PERHITUNGAN NILAI AKADEMIK ===")
print(f"Total Nilai Akhir : {nilai_akhir:.2f}")
print(f"Nilai Huruf       : {grade}")
print(f"Bobot Nilai       : {bobot}")
print(f"Keterangan        : {keterangan}")
