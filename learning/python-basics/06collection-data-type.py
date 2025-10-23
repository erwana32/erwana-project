#list
buah = ["apel", "jeruk", "pisang"]
buah.append("mangga")
buah[1] = "pepaya"
buah.remove("apel")
print(buah)

#tuple
warna = ("merah", "hijau", "biru")
print(warna[0]) 
#warna[1] = "kuning"  # ini akan error karena tuple tidak bisa diubah
print(warna)

#set    
obat = {"Paracetamol", "Amoxicillin", "Ibuprofen"}
obat.add("Cetirizine")
obat.remove("Ibuprofen")
print(obat)

#dictionary
stok_obat = {
    "Paracetamol": 20,
    "Amoxicillin": 15,
    "Ibuprofen": 0
}
stok_obat["Cetirizine"] = 10
stok_obat["Paracetamol"] = 25
del stok_obat["Ibuprofen"]
print(stok_obat)

