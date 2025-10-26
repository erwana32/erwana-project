# Looping menggunakan for
for i in range(5):
    print("iteration ke-", i)


# Looping menggunakan while
x = 0
while x < 5:
    print("nilai x=", x)
    x +=1

# Looping dengan break
for i in range(10):
    if i == 5:
        break
    print("Looping dengan break, i =", i)

# Looping dengan continue
for i in range(10):
    if i % 2 == 0:
        continue
    print("Looping dengan continue, i =", i)
# Nested loop
for i in range(3):
    for j in range(2):
        print("i =", i, ", j =", j) 

# Loop dengan else
for i in range(3):
    print("Looping dengan else, i =", i)
else:
    print("Loop selesai")   

# Looping melalui list
fruits = ["apel", "pisang", "cherry"]
for fruit in fruits:
    print("Buah:", fruit)   

# Looping melalui string
word = "Python"
for letter in word:
    print("Huruf:", letter)   

# Looping melalui dictionary
person = {"nama": "Erza", "umur": 25, "kota": "Jakarta"}
for key, value in person.items():
    print(key + ":", value)   

# Looping dengan enumerate
colors = ["merah", "hijau", "biru"]
for index, color in enumerate(colors):
    print("Index", index, "warna:", color)   

#case
stock_obat = {
    "Paracetamol": 15,
    "Amoxicillin": 8,
    "Ibuprofen": 0,
    "Cetirizine": 1
}
for name, stock in stock_obat.items():
    if stock < 0:
        print(f"{name} X Habis - segera restock!")
    elif stock < 10:
        print(f"{name} ! Stok menipis, tersisa {stock} strip ")
    else:
        print(f"{name} V Stok cukup, tersisa {stock} strip ")
    
# Tebak angka "using break"

angka_rahasia = 7

while True:
    tebakan = int(input("Tebak angka 1 - 10:"))
    if tebakan == angka_rahasia:
        print("Selamat! Tebakan Anda benar.")
        break
    else:
        print("Tebakan salah. Coba lagi!")
        
#Cetak angka ganjil "using continue"
for i in range (10):
    if i % 2 == 0:
        continue
    print("Angka ganjil:", i)
    

#Mencari password yang benar dengan batas percobaan
password_benar = "Python123"
max_percobaan = 3
percobaan = 0

while percobaan < max_percobaan:
    password = input("Masukkan password:")
    percobaan += 1
    
    if password == password_benar:
        print("Akses diterima.")
        break
    else:
        print(f"Password salah. Anda memiliki {max_percobaan - percobaan} percobaan lagi.")
else:
    print("Akses ditolak. Terlalu banyak percobaan salah.")

#Table perkalian lengakap
print("Table Perkalian 5:\n")
for i in range(1, 6):
    for j in range(1, 6):
        hasil = i * j
        print(i, "x", j, "=", hasil)
    print("=====")