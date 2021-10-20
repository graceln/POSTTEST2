# Judul program
print("Program konversi rupiah ke mata uang asing")

# Fungsi konversi_uang
def konversi_uang():
    print("Pilih mata uang yang akan dikonversi")
    print("1. IDR - USD")
    print("2. IDR - SGD")
    print("3. IDR - EUR")
    print("4. IDR - JPY")
    print("5. Keluar")
print("")

# kondisi awal variabel
rupiah=0
konversi=0

# kondisi while
while True:
    konversi_uang()
    operator = input("Pilih kategori: ")
    operator = str(operator)
    print("")
    
    if operator=='1':
         print("IDR - USD")
         rupiah=input("Nominal Rupiah: ")
         rupiah=int(rupiah)
         konversi = rupiah/(float(14.014))
         print (f"hasilnya adalah = {float(konversi)} USD")
         print("")

    if operator=='2':
         print("IDR - SGD")
         rupiah=input("Nominal Rupiah: ")
         rupiah=int(rupiah)
         konversi = rupiah/(float(10.482))
         print (f"hasilnya adalah = {float(konversi)} SGD")
         print("")

    if operator=='3':
         print("IDR - EUR")
         rupiah=input("Nominal Rupiah: ")
         rupiah=int(rupiah)
         konversi = rupiah/(float(16.412))
         print (f"hasilnya adalah = {float(konversi)} EUR")
         print("")

    if  operator=='4':
         print("IDR - JPY")
         rupiah=input("Nominal Rupiah: ")
         rupiah=int(rupiah)
         konversi = rupiah/(float(123.30))
         print (f"hasilnya adalah = {float(konversi)} JPY")
         print("")

    if operator=='5':
        print("Program selesai")
        break    



