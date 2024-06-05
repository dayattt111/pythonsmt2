def input_data_pelanggan():
    no_rek = input("Masukkan No. Rekening: ")
    nama = input("Masukkan Nama Pelanggan: ")
    golongan = input("Masukkan Golongan Meter (RT1/RT2/RT3): ")
    meter_awal = int(input("Masukkan Penunjukan Meter Awal: "))
    meter_akhir = int(input("Masukkan Penunjukan Meter Akhir: "))
    tgl_bayar = int(input("Masukkan Tanggal Pembayaran: "))
    return (no_rek, nama, golongan, meter_awal, meter_akhir, tgl_bayar)

def hitung_jumlah_pemakaian(meter_awal, meter_akhir):
    return meter_akhir - meter_awal

def hitung_biaya_pemakaian(jumlah_pemakaian, golongan, tarif_per_kwh):
    return jumlah_pemakaian * tarif_per_kwh[golongan]

def hitung_denda(tgl_bayar, golongan, rentang_bayar, denda_per_golongan):
    if not (rentang_bayar[golongan][0] <= tgl_bayar <= rentang_bayar[golongan][1]):
        return denda_per_golongan[golongan]
    return 0

def hitung_total_pembayaran(biaya_beban, biaya_pemakaian, denda):
    return biaya_beban + biaya_pemakaian + denda

def main():
    # Tarif dan biaya beban per golongan
    tarif_per_kwh = {"RT1": 3900, "RT2": 5700, "RT3": 9500}
    biaya_beban = {"RT1": 50000, "RT2": 75000, "RT3": 100000}
    rentang_bayar = {"RT1": (1, 10), "RT2": (11, 20), "RT3": (21, 31)}
    denda_per_golongan = {"RT1": 17000, "RT2": 26000, "RT3": 35000}
    
    pelanggan_list = []
    jumlah_pelanggan = int(input("Masukkan jumlah pelanggan: "))
    
    for _ in range(jumlah_pelanggan):
        pelanggan = input_data_pelanggan()
        pelanggan_list.append(pelanggan)
    
    # Output data per pelanggan
    for pelanggan in pelanggan_list:
        no_rek, nama, golongan, meter_awal, meter_akhir, tgl_bayar = pelanggan
        jumlah_pemakaian = hitung_jumlah_pemakaian(meter_awal, meter_akhir)
        biaya_pemakaian = hitung_biaya_pemakaian(jumlah_pemakaian, golongan, tarif_per_kwh)
        denda = hitung_denda(tgl_bayar, golongan, rentang_bayar, denda_per_golongan)
        total_pembayaran = hitung_total_pembayaran(biaya_beban[golongan], biaya_pemakaian, denda)
        
        print("\nData Pelanggan:")
        print(f"No. Rekening: {no_rek}")
        print(f"Nama Pelanggan: {nama}")
        print(f"Golongan Meter: {golongan}")
        print(f"Jumlah Pemakaian: {jumlah_pemakaian} kWh")
        print(f"Biaya Pemakaian: Rp. {biaya_pemakaian}")
        print(f"Denda: Rp. {denda}")
        print(f"Total Pembayaran: Rp. {total_pembayaran}")
        print("")
    
    # Output agregat
    jumlah_pelanggan_per_golongan = {"RT1": 0, "RT2": 0, "RT3": 0}
    total_denda = 0
    total_pemasukan = 0
    
    for pelanggan in pelanggan_list:
        golongan = pelanggan[2]
        jumlah_pelanggan_per_golongan[golongan] += 1
        jumlah_pemakaian = hitung_jumlah_pemakaian(pelanggan[3], pelanggan[4])
        biaya_pemakaian = hitung_biaya_pemakaian(jumlah_pemakaian, golongan, tarif_per_kwh)
        denda = hitung_denda(pelanggan[5], golongan, rentang_bayar, denda_per_golongan)
        total_pembayaran = hitung_total_pembayaran(biaya_beban[golongan], biaya_pemakaian, denda)
        
        total_denda += denda
        total_pemasukan += total_pembayaran
    
    total_pemasukan_setelah_operasional = total_pemasukan * 0.9
    
    print("Laporan Agregat:")
    print(f"Jumlah Pelanggan RT1: {jumlah_pelanggan_per_golongan['RT1']}")
    print(f"Jumlah Pelanggan RT2: {jumlah_pelanggan_per_golongan['RT2']}")
    print(f"Jumlah Pelanggan RT3: {jumlah_pelanggan_per_golongan['RT3']}")
    print(f"Total Jumlah Denda: Rp. {total_denda}")
    print(f"Total Pemasukan: Rp. {total_pemasukan}")
    print(f"Total Pemasukan Setelah Biaya Operasional 10%: Rp. {total_pemasukan_setelah_operasional}")

if __name__ == "__main__":
    main()
