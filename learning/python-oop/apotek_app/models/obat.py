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
            print(f"Stok {self.nama} - Tidak Cukup Sisa Stok: {self.stok}")
        else:
            self.stok -= qty
            print(f"{self.nama} - Terjual {qty} - Sisa Stok: {self.stok}")
    
   
