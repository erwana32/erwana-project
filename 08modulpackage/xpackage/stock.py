def cek_stok(nama, jumlah):
    if jumlah == 0:
        return f"Stok {nama} habis! Segera restock!"
    elif jumlah < 10:
        return f"Stok {nama} menipis, tersisa {jumlah} strip."
    else:
        return f"Stok {nama} cukup, tersisa {jumlah} strip."
    
    