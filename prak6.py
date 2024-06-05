from modulepy6 import *
def main():
    Q = ArrayQueue()
    Q.enqueue(5)
    Q.enqueue(3)
    Q.enqueue(4)
    Q.enqueue(2)
    Q.enqueue(7)
    n = len(Q)
    print("ada %d data dalam Queue" % n)
    print("Data Pertama : %d" % Q.first())
    print("Melayani isi Antrian : ")
    for i in range(n):
        x = Q.dequeue()
        print("Mengambil %d " % x)

    print("Apakah Antrian Sudah Kosong")
    if (Q.is_empty()):
        print("Antrian Sudah Kosong")

main()