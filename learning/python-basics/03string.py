nama = "Erwana"
pesan = 'Selamat datang di Apotek Erza!'
multi = """Ini contoh
string dengan
banyak baris."""

print(nama)
print(pesan)
print(multi)


#string methods
text = "Apotek Erza menyediakan berbagai macam obat-obatan."

print(text.upper())
print(text.lower())
print(len(text))
print(text.replace("Apotek", "Toko Obat"))
print(text.split(" "))
print("Erza" in text)
print("Obat" not in text)

#Indexing
print(text[0])
print(text[-1])
print(text[:12])

#Slicing
print(text[0:6])
print(text[8:12])
print(text[::2])    


path = "C:\\Users\\Erwana\\Documents\\obat.txt"
name = "Name:\tErwana\n"
umur = "Age:\t25\n"
print(path)
print(name)
print(umur)

harga_obat = 15000
quantity = 3

print(f" Harga Obat: Rp {harga_obat}\n Jumlah: {quantity}\n Total: Rp.{harga_obat * quantity}")