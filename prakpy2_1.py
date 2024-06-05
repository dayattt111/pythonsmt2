from array import array
bil = array('i', [])
jum = tot = 0
while True:
    nilai = int(input('Masukkan Bilangan [0:selesai] :'))
    if nilai == 0:
        break
    bil.append(nilai)
    tot += bil[jum]
    jum += 1

print('\nBilangan yang di input : ', end='')
for x in range(jum):
    print(bil[x], end='')
print('nJumlah Bilangan yang di input :  ', len(bil))
print('Total Jumlahan : ', tot)

tot = 0
print('\n\nBilanngan Ganjil adalah : ', end='')
for x in range(jum):
    if bil[x] % 2 == 1:
        print (bil[x], end='')
        tot += bil[x]
print('\nTotal JUmlah bilangan ganjil : ', tot)
tot = 0
print('\nBilangan Genap adalah : ', end='')
for x in range(jum):
    if bil[x] % 2 == 0:
        print(bil[x], end='')
        tot += bil[x]
print('\nTotal Jumlahan Bilangan Genap : ', tot)
maks = 0 
mins = 9999999999
for x in range(jum):
    if maks < bil[x]:
        maks = bil[x]
    if mins > bil[x]:
        mins = bil[x]
print('\nNilai terbesar adalah : ', maks)
print('\nNilai terkecil adalah : ', mins)

for i in range (0, len(bil) -1):
    for j in range(len(bil)-1, i, -1):
        if bil[j] < bil[j-1]:
            bil [j] < bil[j-1] = bil[j-1], bil[j]
print('\nBilangan Setelah di urutkan : ', end='')
for x in range(jum):
    print(bil[x], end='')