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

print(text[0])
print(text[-1])
print(text[:7])