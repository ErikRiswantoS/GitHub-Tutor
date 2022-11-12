# perulangan bersama saya erik riswanto saputra
usia = int(input("masukan usia: "))
tinggi = int(input("masukan tinggi: "))

if usia < 2:
    print("dilarang masuk")
elif usia < 4:
    if (tinggi <= 70):
        print("untuk usia",usia,"tahun dengan tinggi",tinggi,"cm dengan harga tiket rp. 30.000")
    else: 
        print("untuk usia",usia,"tahun dengan tinggi",tinggi,"cm dengan harga tiket rp.",30000 + 10000)
elif usia < 7:
    if (tinggi <=120):
        print("untuk usia",usia,"tahun dengan tinggi",tinggi,"cm dengan harga tiket rp. 40.000")
    else:
        print("untuk usia",usia,"tahun dengan tinggi",tinggi,"cm dengan harga tiket rp.",40000 + 15000)
elif usia < 10:
    if (tinggi <= 150):
        print("untuk usia",usia,"tahun dengan tinggi",tinggi,"cm dengan harga tiket rp. 50.000")
    else:
        print("untuk usia",usia,"tahun dengan tinggi",tinggi,"cm dengan harga tiket rp.",50000 + 20000)
else:
    if (usia >= 10):
        print("untuk usia",usia,"tahun dengan tinggi",tinggi,"cm dengan harga tiket rp. 80.000")