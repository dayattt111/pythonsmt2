def buatArray(A, n):
    for i in range(n):
        A.append(0)
    # A = [0] * n

def isiArray(A, n):
    for i in range(n):
        A[i] = int(input("ISI : "))

def bacaArray(A):
    r = input("0 - 1-suku data : ")
    r = int(r)
    if r < 1:
        print(A)
    else:
        x = int(input("Posisi : "))
        print(A[x - 1])

def cariArray(x, A):
    ketemu = False
    for i in range(len(A)):
        if x == A[i]:
            print("ketemu di Posisi", i + 1, '\n')
            ketemu = True
    if not ketemu:
        print(x, ' Tidak ada dalam Array')

def hapus(x, A):
    ketemu = False
    for i in range(len(A)):
        if x == A[i]:
            print("Ketemu di posisi", i + 1, '\n')
            ketemu = True
            A[i] = ''
    if not ketemu:
        print(x, ' Tidak ada dalam Array \n')

A = []
buatArray(A, 5)
print(A)

isiArray(A, 5)
print("Array setelah pengisian:", A)

bacaArray(A)

cariArray(3, A)

hapus(3, A)
print("Array setelah penghapusan:", A)

