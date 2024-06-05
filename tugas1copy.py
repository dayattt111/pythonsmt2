def input_data():
    print("\n       PUSAT PENDIDIKAN KOMPUTER ")
    print("              INFORMATIKA")
    print("--------------------------------------")
    reg_no = input(" No.Registrasi     : ")
    nama_peserta = input(" Nama Peserta      : ")
    print(" Pilih Bhs.Pemrograman")
    print("1. Basic")
    print("2. Pascal")
    print("3. C++")
    while True:
        kode_bahasa = input("      Input Kode Bahasa [1/2/3]  : ")
        if kode_bahasa in ['1', '2', '3']:
            bahasa = {'1': 'Basic', '2': 'Pascal', '3': 'C++'}[kode_bahasa]
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan kode bahasa yang benar.")

    while True:
        try:
            nilai_ujian = int(input("        Input Nilai Ujian [0..100] : "))
            if 0 <= nilai_ujian <= 100:
                break
            else:
                print("Nilai ujian harus dalam rentang 0 hingga 100.")
        except ValueError:
            print("Masukkan nilai ujian dalam angka.")

    print("--------------------------------------")
    return reg_no, nama_peserta, bahasa, nilai_ujian

def find_max_score(data_peserta):
    max_scores = {'Basic': {'no_reg': '', 'nama_peserta': '', 'nilai': -1},
                  'Pascal': {'no_reg': '', 'nama_peserta': '', 'nilai': -1},
                  'C++': {'no_reg': '', 'nama_peserta': '', 'nilai': -1}}

    for reg_no, nama_peserta, bahasa, nilai in data_peserta:
        if nilai > max_scores[bahasa]['nilai']:
            max_scores[bahasa] = {'no_reg': reg_no, 'nama_peserta': nama_peserta, 'nilai': nilai}

    return max_scores

def display_output(max_scores):
    for bahasa, data in max_scores.items():
        if data['nilai'] != -1:
            print("\n Nilai Tertinggi pada Bahasa", bahasa + ":")
            print("   No.Registrasi : ", data['no_reg'])
            print("   Nama Peserta  : ", data['nama_peserta'])
            print("   Nilai Ujian   : ", data['nilai'])
            print("  -------------------------------------")
        else:
            print(f"\n Tidak ada data yang memenuhi untuk bahasa {bahasa}.")

def main():
    data_peserta = []
    while True:
        reg_no, nama_peserta, bahasa, nilai = input_data()
        data_peserta.append((reg_no, nama_peserta, bahasa, nilai))

        ulangi = input("\n Ada data lain [y/t] : ")
        if ulangi.lower() != 'y':
            break

    max_scores = find_max_score(data_peserta)
    display_output(max_scores)

if __name__ == "__main__":
    main()
