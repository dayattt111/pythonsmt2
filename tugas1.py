def hitung_harga(kode, jumlah):
    if kode == 'X':
        if jumlah == 20:
            harga = 20000
        elif jumlah == 10:
            harga = 11000
        elif jumlah == 5:
            harga = 6000
        else:
            print("Jumlah pulsa tidak valid untuk XL.")
            return 0, 0
    elif kode == 'T':
        if jumlah == 20:
            harga = 21000
        elif jumlah == 10:
            harga = 11500
        elif jumlah == 5:
            harga = 6500
        else:
            print("Jumlah pulsa tidak valid untuk Telkomsel.")
            return 0, 0
    elif kode == 'I':
        if jumlah == 20:
            harga = 22000
        elif jumlah == 10:
            harga = 12000
        elif jumlah == 5:
            harga = 7000
        else:
            print("Jumlah pulsa tidak valid untuk Indosat.")
            return 0, 0
    else:
        print("Kode operator tidak valid.")
        return 0, 0
    
    ppn = harga * 0.1
    total_harga = harga + ppn
    return harga, total_harga

def main():
    nama_pelanggan = input("Masukkan nama pelanggan: ")
    kode_pulsa = input("Masukkan kode pulsa (X/T/I): ")
    jumlah_pulsa = int(input("Masukkan jumlah pulsa (5/10/20): "))
    
    harga_pulsa, total_harga = hitung_harga(kode_pulsa, jumlah_pulsa)
    
    if harga_pulsa != 0:
        print("\nDetail Pembelian:")
        print("Nama Pelanggan:", nama_pelanggan)
        print("Kode Pulsa:", kode_pulsa)
        print("Jumlah Pulsa:", jumlah_pulsa)
        print("Harga Pulsa:", harga_pulsa)
        print("PPN (10%):", harga_pulsa * 0.1)
        print("Total Harga:", total_harga)

if __name__ == "__main__":
    main()
