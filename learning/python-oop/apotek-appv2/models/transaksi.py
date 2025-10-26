class Transaksi:
    def __init__(self):
        self.data_beli = []

    def beli(self, obat, qty):
        if obat.jual(qty):
            self.data_beli.append((obat, qty))

    def total(self):
        return sum(o.harga * qty for o, qty in self.data_beli)

    def struk(self):
        print("\n=== STRUK PEMBELIAN ===")
        for o, qty in self.data_beli:
            print(f"{o.nama} x {qty} = Rp{o.harga * qty:,}")
        print("-----------------------")
        print(f"TOTAL: Rp{self.total():,}")
