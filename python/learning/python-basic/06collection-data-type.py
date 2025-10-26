#list
print("=== List ===")
buah = ["apel", "jeruk", "pisang"]
print(buah)
buah.append("mangga")
print(buah)
buah[1] = "pepaya"
print(buah)
buah.remove("apel")
print(buah)
buah.pop()
print(buah)

#tampilkan semua buah di setiap index
for b in range(len(buah)):
    print("- " + buah[b])
    
#check isi list
if "mangga" in buah:
    print("Mangga ada dalam daftar buah")
else:
    print("Mangga tidak ada dalam daftar buah")

#-----------------------------------------------
#tuple
print("\n=== Tuple ===")
warna = ("merah", "hijau", "biru")
print(warna[0]) 
#warna[1] = "kuning"  # ini akan error karena tuple tidak bisa diubah
print(warna)





#-----------------------------------------------
#set
print("\n=== Set ===")    
obat = {"Paracetamol", "Amoxicillin", "Ibuprofen"}
obat.add("Cetirizine")
obat.remove("Ibuprofen")
print(obat)

for e in obat:
    print("- " + e)

#-----------------------------------------------
#dictionary
print("\n=== Dictionary ===")
stok_obat = {
    "Paracetamol": 20,
    "Amoxicillin": 15,
    "Ibuprofen": 0
}
for key, value in stok_obat.items():
    print(key + ": " + str(value))

stok_obat["Cetirizine"] = 10
print("\n")
for key, value in stok_obat.items():
    print(key + ": " + str(value))

stok_obat["Paracetamol"] = 25
print("\n")
for key, value in stok_obat.items():
    print(key + ": " + str(value))

del stok_obat["Ibuprofen"]
print(stok_obat)
print("\n")
for key, value in stok_obat.items():
    print(key + ": " + str(value))

