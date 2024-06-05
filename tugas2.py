def input_nilai():
    reg = input("No.Registrasi     : ")
    nama = input("Nama Peserta      : ")
    
    while True:
        print("Pilih Bhs.Pemrograman")
        print("1. Basic")
        print("2. Pascal")
        print("3. C++")
        kode = input("Input Kode Bahasa [1/2/3]  : ")
        if kode in ['1', '2', '3']:
            break
        else:
            print("Kode Bahasa Pemrograman tidak valid.")
            
    if kode == '1':
        bahasa = "Basic"
    elif kode == '2':
        bahasa = "Pascal"
    else:
        bahasa = "C++"
    
    while True:
        nilai = input("Input Nilai Ujian [0..100] : ")
        if nilai.isdigit() and 0 <= int(nilai) <= 100:
            nilai = int(nilai)
            break
        else:
            print("Nilai Ujian tidak valid.")
    return reg, nama, bahasa, nilai

def main():
    nilai_tertinggi = {"Basic": {"no_reg": "", "nama": "", "nilai": 0},
                       "Pascal": {"no_reg": "", "nama": "", "nilai": 0},
                       "C++": {"no_reg": "", "nama": "", "nilai": 0}}
    
    lanjut = 'y'  # Inisialisasi agar masuk ke loop pertama
    
    while lanjut.lower() == 'y':
        print("PUSAT PENDIDIKAN KOMPUTER")
        print("INFORMATIKA")
        print("--------------------------------------")
        
        reg, nama, bahasa, nilai = input_nilai()
        
        if nilai > nilai_tertinggi[bahasa]["nilai"]:
            nilai_tertinggi[bahasa]["no_reg"] = reg
            nilai_tertinggi[bahasa]["nama"] = nama
            nilai_tertinggi[bahasa]["nilai"] = nilai
        
        print("--------------------------------------")
        
        while True:
            lanjut = input("Ada data lain [y/t] : ")
            if lanjut.lower() in ['y', 't']:
                break
            else:
                print("Masukkan y untuk ya atau t untuk tidak.")
    
    print("\nNilai Tertinggi pada Bahasa Basic:")
    print("  No.Registrasi :", nilai_tertinggi["Basic"]["no_reg"])
    print("  Nama Peserta  :", nilai_tertinggi["Basic"]["nama"])
    print("  Nilai Ujian   :", nilai_tertinggi["Basic"]["nilai"])
    print("-------------------------------------")
    print("Nilai Tertinggi pada Bahasa Pascal:")
    print("  No.Registrasi :", nilai_tertinggi["Pascal"]["no_reg"])
    print("  Nama Peserta  :", nilai_tertinggi["Pascal"]["nama"])
    print("  Nilai Ujian   :", nilai_tertinggi["Pascal"]["nilai"])
    print("-------------------------------------")
    print("Nilai Tertinggi pada Bahasa C++:")
    print("  No.Registrasi :", nilai_tertinggi["C++"]["no_reg"])
    print("  Nama Peserta  :", nilai_tertinggi["C++"]["nama"])
    print("  Nilai Ujian   :", nilai_tertinggi["C++"]["nilai"])
    print("-------------------------------------")

if __name__ == "__main__":
    main()
