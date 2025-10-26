from models.obat import Obat

class ObatResep(Obat):
    def __init__(self, nama, harga, stok, dokter):
        super().__init__(nama, harga, stok)
        self.dokter = dokter
    