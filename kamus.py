kamus1 = {'saya':'I', 'kamu':'you','dia': 'he/she', 'kita':'we','kami':'we','mereka':'they'}
kamus2 = {'pergi':'go', 'pulang': 'back', 'tidur':'sleep', 'makan': 'eat', 'main':'play', 'naik':'ride', 'bermain':'play', 'suka':'love', 'setelah':'after', 'sebelum':'before'}
kamus3 = {'di':'at','ke':'to','sekolah':'school','kantor':'office','rumah':'home','resto':'restaurant','sepeda':'bike','bola':'soccer','tennis':'tenis','dari':'from',}

jawab=''
while(True):
    kalimat = input("Apa kegiatan hari ini? : ")
    for kata in kalimat.split(' '):
        if kata in(kamus1):
            jawab += kamus1[kata] + ' '
        elif kata in(kamus2):
            jawab += kamus2[kata] + ' '
        elif kata in(kamus3):
            jawab += kamus3[kata] + ' '
        else:
            jawab += kata + ' '
    print(jawab)
    lagi = input("Masih Mau Translate ? (Y/N)")
    if (lagi == 'n'):
        break
    else:
        jawab=''
print('See You Again!')