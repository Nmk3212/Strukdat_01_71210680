print("KALKULATOR")

while True:
    print("1. TAMBAH")
    print("2. KURANG")
    print("3. KALI")
    print("4. BAGI")

    menu = input("Masukan Pilihan: ")
    bil1 = int(input("Masukan Bilangan 1: "))
    bil2 = int(input("Masukan Bilangan 2: ")) 

    if menu == "1":
        hasil = bil1 + bil2
        print("hasil: ",hasil)
    elif menu == "2":
        hasil = bil1 - bil2
        print("hasil: ",hasil)
    elif menu == "3":
        hasil = bil1 * bil2
        print("hasil: ",hasil)   
    elif menu == "4":
        hasil = bil1 / bil2
        print("hasil: ",hasil)
    
    pilihan = input("Apakah ingin melanjutkan atau tidak jika ya ketik L jika tidak ketik Q: ")
    if pilihan == "Q":
        break