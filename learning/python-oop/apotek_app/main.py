from master import master_obat
from models.obat import Obat
from models.obat_resep import ObatResep
from models.transaksi import Transaksi


"""
o1 = Obat("Paracetamol", 5000, 20)
o2 = ObatResep("Amoxicillin", 2000, 10, "dr.Syifa")

o1.info()
o2.info()

"""

#convert master_obat to object list
list_obat = []
for data in master_obat:
    obj = Obat(
        data["kode"],
        data["nama"],
        data["harga"],
        data["stok"]
    )
    list_obat.append(obj)
    
    
print("=== Daftar Obat ===")
for obat in list_obat:
    obat.info()
    
    
print("===Pencarian Obat===")

def cari_obat(kode):
        for obat in list_obat:
            if obat.kode == kode:
               return obat
        return None
    
hasil = cari_obat("OB003")
if hasil:
    hasil.info()
else:
    print("Obat tidak ditemukan")
    
trx = Transaksi()
trx.beli(cari_obat("OB001"), 2)
trx.beli(cari_obat("OB002"), 5)
trx.beli(cari_obat("OB005"), 4) #test stok tidak cukup
trx.struk()