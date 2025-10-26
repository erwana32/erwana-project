from master.loader import load_master, save_master
from models.obat import Obat
from models.transaksi import Transaksi

#load JSON -> Dictionary
data = load_master()

#Dictionary -> Object
list_obat = [Obat(o["kode"], o["nama"], o["harga"], o["stok"]) for o in data]


def cari_obat(kode):
    for obat in list_obat:
        if obat.kode == kode:
            return obat
    return None




print("💊 Sistem Apotek Erza")

trx = Transaksi()
trx.beli(cari_obat("OB001"), 2)
trx.beli(cari_obat("OB003"), 1)

trx.struk()

# Save new stock to JSON
save_master([o.to_dict() for o in list_obat])


#info obat

for obat in list_obat:
    obat.info()
