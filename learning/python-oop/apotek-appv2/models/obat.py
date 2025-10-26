class Obat:
    def __init__(self, kode, nama, harga, stok):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok
        
    def info(self):
        print(f"Kode: {self.kode} - Nama: {self.nama} - Harga: {self.harga} - Stok: {self.stok}")

    def jual(self, qty):
        if qty > self.stok:
            print(f"❌ Stok {self.nama} tidak cukup!")
            return False
        self.stok -= qty
        print(f"✅ Terjual {qty} strip {self.nama}")
        return True

    def to_dict(self):
        return {
            "kode": self.kode,
            "nama": self.nama,
            "harga": self.harga,
            "stok": self.stok
        }
