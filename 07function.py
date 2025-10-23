#function
def sapa():
    print("Hello, welcome to the function demo!")
sapa()

#function with parameters
def greet(name):
    print("Hello, " + name + "! Nice to meet you.")
greet("Syifa")
greet("Erza")

#function with return value
def tambah(a, b):
    return a + b
hasil = tambah(5, 3)
print("Hasil penjumlahan:", hasil)

#function with default parameter
def perkenalan(nama, umur=18):
    print("Nama saya " + nama + ", umur saya " + str(umur) + " tahun.")
perkenalan("Syifa", 20)
perkenalan("Erza")  

#function with variable-length arguments
def daftar_buah(*buah):
    print("Buah-buahan yang saya suka:")
    for b in buah:
        print("- " + b)
daftar_buah("apel", "pisang", "mangga")
daftar_buah("jeruk", "kiwi")

#function with keyword arguments
def info_orang(**info):
    for key, value in info.items():
        print(key + ": " + str(value))
info_orang(nama="Syifa", umur=20, kota="Jakarta")
info_orang(nama="Erza", pekerjaan="Programmer")

#nested function
def luar(x):
    def dalam(y):
        return y * y
    return dalam(x) + 10
hasil_nested = luar(5)      
print("Hasil dari fungsi nested:", hasil_nested)

#lambda function
kali = lambda a, b: a * b
hasil_lambda = kali(4, 5)
print("Hasil perkalian menggunakan lambda:", hasil_lambda)  

#function sebagai argumen
def operasi(a, b, func):
    return func(a, b)
def kurang(x, y):
    return x - y
hasil_operasi = operasi(10, 4, kurang)
print("Hasil operasi pengurangan:", hasil_operasi)

#rekursif function
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)
hasil_faktorial = faktorial(5)
print("Faktorial dari 5 adalah:", hasil_faktorial) 

#function dengan dokumentasi
def luas_persegi(sisi):
    """Menghitung luas persegi dengan sisi tertentu."""
    return sisi * sisi          
luas = luas_persegi(4)
print("Luas persegi:", luas)
print(luas_persegi.__doc__)

#anonymous function dengan filter dan map
angka = [1, 2, 3, 4, 5, 6]
genap = list(filter(lambda x: x % 2 == 0, angka))
kuadrat = list(map(lambda x: x * x, angka))
print("Angka genap:", genap)
print("Kuadrat dari angka:", kuadrat)

#function dengan dekorator
def dekorator(func):
    def wrapper():
        print("Sebelum menjalankan fungsi.")
        func()
        print("Setelah menjalankan fungsi.")
    return wrapper  
@dekorator
def sapa_dekorasi():
    print("Halo dari fungsi dengan dekorator!")
sapa_dekorasi()

#function dengan exception handling
def bagi(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    else:
        return hasil
    finally:
        print("Operasi pembagian selesai.")
print(bagi(10, 2))
print(bagi(10, 0))  

#function dengan tipe data kompleks
def proses_data(data):      
    if isinstance(data, list):
        return [x * 2 for x in data]
    elif isinstance(data, dict):
        return {k: v * 2 for k, v in data.items()}
    else:
        return "Tipe data tidak didukung."
hasil_list = proses_data([1, 2, 3])
hasil_dict = proses_data({"a": 1, "b": 2})
print("Hasil proses list:", hasil_list)
print("Hasil proses dictionary:", hasil_dict) 

#function dengan anotasi tipe
def tambah_angka(a: int, b: int) -> int:
    return a + b
hasil_tambah = tambah_angka(7, 3)
print("Hasil penjumlahan dengan anotasi tipe:", hasil_tambah)   
print(tambah_angka.__annotations__)

#function dengan closure
def pembuat_pengali(faktor):
    def pengali(x):
        return x * faktor
    return pengali
kali_3 = pembuat_pengali(3)
hasil_closure = kali_3(10)
print("Hasil pengalian dengan closure:", hasil_closure) 

#function dengan coroutine
def penghitung():
    total = 0
    while True:
        nilai = yield total
        if nilai is None:
            break
        total += nilai
counter = penghitung()
next(counter)  

print("Total setelah menambahkan 5:", counter.send(5))
print("Total setelah menambahkan 10:", counter.send(10))

try:
    counter.send(None)
except StopIteration:
    print("Coroutine selesai.")



