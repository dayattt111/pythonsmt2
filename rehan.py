def hitung_pendapatan(data_penjualan):
    total_pendapatan = 0
    for buah, jumlah_terjual, harga_satuan in data_penjualan:
        pendapatan_buah = jumlah_terjual * harga_satuan