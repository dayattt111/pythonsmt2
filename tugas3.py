class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

class Array2D:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.array = [[None for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

class Student:
    def __init__(self, no_pokok, nama):
        self.no_pokok = no_pokok
        self.nama = nama
        self.kehadiran = Array2D(1, 15)
        self.tugas = Array2D(1, 5)
        self.mid = 0
        self.final = 0
        self.presensi = 0
        self.rerata_tugas = 0
        self.nilai_akhir = 0
        self.nilai_huruf = ''

    def calculate_presensi(self):
        self.presensi = sum(self.kehadiran[0]) / 15 * 100

    def calculate_rerata_tugas(self):
        self.rerata_tugas = sum(self.tugas[0]) / 5

    def calculate_nilai_akhir(self):
        self.nilai_akhir = (0.1 * self.presensi) + (0.2 * self.rerata_tugas) + (0.3 * self.mid) + (0.4 * self.final)

    def calculate_nilai_huruf(self):
        if self.nilai_akhir >= 80:
            self.nilai_huruf = 'A'
        elif 80 > self.nilai_akhir >= 65:
            self.nilai_huruf = 'B'
        elif 65 > self.nilai_akhir >= 50:
            self.nilai_huruf = 'C'
        elif 50 > self.nilai_akhir >= 30:
            self.nilai_huruf = 'D'
        else:
            self.nilai_huruf = 'E'

def main():
    students = Array(10)  # assume 10 students
    for i in range(10):
        no_pokok = input("Enter No. Pokok: ")
        nama = input("Enter Nama: ")
        student = Student(no_pokok, nama)
        for j in range(15):
            kehadiran = int(input(f"Enter Kehadiran {j+1}: "))
            student.kehadiran[0][j] = kehadiran
        for j in range(5):
            tugas = int(input(f"Enter Tugas {j+1}: "))
            student.tugas[0][j] = tugas
        student.mid = int(input("Enter Mid: "))
        student.final = int(input("Enter Final: "))
        student.calculate_presensi()
        student.calculate_rerata_tugas()
        student.calculate_nilai_akhir()
        student.calculate_nilai_huruf()
        students[i] = student

    # print output for each student
    for student in students:
        print(f"No. Pokok: {student.no_pokok}, Nama: {student.nama}")
        print(f"Presensi: {student.presensi:.2f}, Rerata Tugas: {student.rerata_tugas:.2f}")
        print(f"Mid: {student.mid}, Final: {student.final}")
        print(f"Nilai Akhir: {student.nilai_akhir:.2f}, Nilai Huruf: {student.nilai_huruf}")
        print()

    # print output for highest and lowest nilai akhir
    nilai_akhir_max = max(student.nilai_akhir for student in students)
    nilai_akhir_min = min(student.nilai_akhir for student in students)
    print(f"Nilai Akhir Tertinggi: {nilai_akhir_max:.2f}")
    print(f"Nilai Akhir Terendah: {nilai_akhir_min:.2f}")

if __name__ == "__main__":
    main()