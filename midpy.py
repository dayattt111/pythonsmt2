class Pelanggan:
    def __init__(self, no_rek, nama, golongan, meter_awal, meter_akhir, tgl_bayar):
        self.no_rek = no_rek
        self.nama = nama
        self.golongan = golongan
        self.meter_awal = meter_awal
        self.meter_akhir = meter_akhir
        self.tgl_bayar = tgl_bayar
        self.jumlah_pemakaian = self.hitung_jumlah_pemakaian()
        self.biaya_pemakaian = self.hitung_biaya_pemakaian()
        self.denda = self.hitung_denda()
        self.total_pembayaran = self.hitung_total_pembayaran()

    def hitung_jumlah_pemakaian(self):
        return self.meter_akhir - self.meter_awal

    def hitung_biaya_pemakaian(self):
        tarif = {"RT1": 3900, "RT2": 5700, "RT3": 9500}[self.golongan]
        return self.jumlah_pemakaian * tarif

    def hitung_denda(self):
        rentang_bayar = {"RT1": (1, 10), "RT2": (11, 20), "RT3": (21, 31)}[self.golongan]
        denda = {"RT1": 17000, "RT2": 26000, "RT3": 35000}[self.golongan]
        if not (rentang_bayar[0] <= self.tgl_bayar <= rentang_bayar[1]):
            return denda
        return 0

    def hitung_total_pembayaran(self):
        biaya_beban = {"RT1": 50000, "RT2": 75000, "RT3": 100000}[self.golongan]
        return biaya_beban + self.biaya_pemakaian + self.denda

# Contoh data pelanggan
pelanggan_list = [
    Pelanggan("001", "Andi", "RT1", 1000, 1200, 15),
    Pelanggan("002", "Budi", "RT2", 1500, 1700, 12),
    Pelanggan("003", "Citra", "RT3", 2000, 2250, 25)
]

# Output data per pelanggan
for pelanggan in pelanggan_list:
    print(f"No. Rekening: {pelanggan.no_rek}")
    print(f"Nama Pelanggan: {pelanggan.nama}")
    print(f"Golongan Meter: {pelanggan.golongan}")
    print(f"Jumlah Pemakaian: {pelanggan.jumlah_pemakaian} kWh")
    print(f"Biaya Pemakaian: Rp. {pelanggan.biaya_pemakaian}")
    print(f"Total Pembayaran: Rp. {pelanggan.total_pembayaran}")
    print("")

# Output agregat
jumlah_pelanggan_rt1 = sum(1 for p in pelanggan_list if p.golongan == "RT1")
jumlah_pelanggan_rt2 = sum(1 for p in pelanggan_list if p.golongan == "RT2")
jumlah_pelanggan_rt3 = sum(1 for p in pelanggan_list if p.golongan == "RT3")

total_denda = sum(p.denda for p in pelanggan_list)
total_pemasukan = sum(p.total_pembayaran for p in pelanggan_list)
total_pemasukan_setelah_operasional = total_pemasukan * 0.9

print(f"Jumlah Pelanggan RT1: {jumlah_pelanggan_rt1}")
print(f"Jumlah Pelanggan RT2: {jumlah_pelanggan_rt2}")
print(f"Jumlah Pelanggan RT3: {jumlah_pelanggan_rt3}")
print(f"Total Jumlah Denda: Rp. {total_denda}")
print(f"Total Pemasukan: Rp. {total_pemasukan}")
print(f"Total Pemasukan Setelah Biaya Operasional 10%: Rp. {total_pemasukan_setelah_operasional}")
