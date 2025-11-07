# latihan2_calculator_if.py
# Kalkulator sederhana menggunakan if/elif/else

def main():
    print("=== Latihan 2: Kalkulator Sederhana (menggunakan if) ===")

    try:
        a = float(input("Masukkan nilai a: ").strip())
        b = float(input("Masukkan nilai b: ").strip())
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return

    op = input("Masukkan operator (+, -, *, /, %, **): ").strip()

    # Menggunakan if/elif untuk menentukan operasi
    if op == '+':
        hasil = a + b
    elif op == '-':
        hasil = a - b
    elif op == '*':
        hasil = a * b
    elif op == '/':
        if b == 0:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
            return
        hasil = a / b
    elif op == '%':
        if b == 0:
            print("Error: Modulus dengan nol tidak diperbolehkan.")
            return
        hasil = a % b
    elif op == '**':
        hasil = a ** b
    else:
        print("Operator tidak valid. Gunakan salah satu dari (+, -, *, /, %, **).")
        return

    print(f"Hasil dari {a} {op} {b} = {hasil}")

# Perbaikan di sini: gunakan __name__ bukan _name_
if __name__ == "__main__":
    main()
