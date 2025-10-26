umur = 20
if umur > 18:
    print("Anda sudah dewasa")
else:
    print("Anda masih di bawah umur")

nilai = 85
if nilai >= 90:
    print("Nilai Anda A")
elif nilai >= 80:
    print("Nilai Anda B")
elif nilai >= 70:
    print("Nilai Anda C")
else:
    print("Nilai Anda D")


angka = int(input("Masukkan sebuah angka: "))
if angka % 2 == 0:
    print(f"{angka} adalah angka genap.")
else:
    print(f"{angka} adalah angka ganjil.")

#match-case statement
hari = input("Masukkan nama hari: ").lower()
match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("Hari kerja")
    case "sabtu" | "minggu":
        print("Hari libur")
    case _:
        print("Hari tidak valid")
        
#ternary operator
angka = int(input("Masukkan sebuah angka:"))
hasil = "Genap" if angka % 2 == 0 else "Ganjil"
print(f"Angka {angka} adalah {hasil}.")

