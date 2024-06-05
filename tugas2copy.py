harga_pulsa = {
    'T': {'20': 22000, '10': 12000, '5': 7000},
    'X': {'20': 21000, '10': 12000, '5': 7000},
    'I': {'20': 20000, '10': 11000, '5': 6000}
}

kode_operator = input("Masukkan kode operator (T/X/I): ")
jenis_pulsa = input("Masukkan jenis pulsa (20/10/5): ")
jumlah_uang = int(input("Masukkan jumlah uang: "))

if kode_operator in harga_pulsa.keys() and jenis_pulsa in harga_pulsa[kode_operator].keys():
    if kode_operator == 'T':
        nama_operator = "Telkomsel"
    elif kode_operator == "X":
        nama_operator = "XL"
    elif kode_operator == "I":
        nama_operator = "Indosat"

    harga = harga_pulsa[kode_operator][jenis_pulsa]

    ppn = harga * 0.1
    total_harga = harga + ppn
    kembalian = jumlah_uang - total_harga

    print("\n COUNTER PULSA MAJU MUNDUR ")
    print("-------------------------------")
    print("Masukkan kode operator : ", kode_operator)
    print("        Nama Operator  : ", nama_operator)
    print("Masukkan jenis pulsa   : ", jenis_pulsa)
    print("     Harga Pulsa Rp.   : ", harga)
    print("      ppn 10% Rp.      : ", ppn)
    print("     total harga Rp.   : ", total_harga)
    print("Masukkan Jumlah Uang   : ", jumlah_uang)
    print("        Kembalian Rp.  : ", kembalian)

else:
    print("Kode operator atau jenis pulsa tidak valid.")
