class Transaksi:
    def __init__(self):
        self.daftar_beli = []
    
    def beli(self, obat, qty):
        obat.jual(qty)
        self.daftar_beli.append((obat.nama, qty, obat.harga))
        
    
    def total_harga(self):
        return sum(qty * harga for _, qty, harga in self.daftar_beli )
    
    def struk(self):
        print("=== Struk Pembelian ===")
        for nama, qty, harga in self.daftar_beli:
            print(f"{nama} x {qty} - Rp{harga * qty,}")
            print(f"Total Harga: Rp {self.total_harga()}")
    