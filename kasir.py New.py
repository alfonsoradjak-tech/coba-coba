# Program Kasir sederhana Toko raja Buah 

def garis():
    print("=" * 60)

while True:
    garis()
    print("                        TOKO RAJA BUAH           ")
    garis()
    print("                SELAMAT DATANG DI TOKO RAJA BUAH")
    print("                =======RAJANYA BUAH SEGAR=======")
    garis()
    print("DAFTAR BUAH")
    print("1. Apel   - Rp 20,000/kg")
    print("2. Jeruk  - Rp 15,000/kg")
    print("3. Mangga - Rp 25,000/kg")
    garis()

    # Input data pelanggan
    nama = input("Masukkan nama pelanggan: ")
    pilihan = int(input("Pilih buah (masukkan nomor 1/2/3): "))

    if pilihan == 1:
        buah = "Apel"
        harga = 20000
    elif pilihan == 2:
        buah = "Jeruk"
        harga = 15000
    elif pilihan == 3:
        buah = "Mangga"
        harga = 25000
    else:
        print("Pilihan tidak valid!")
        continue

    jumlah = float(input(f"Masukkan jumlah {buah} (kg): "))
    total = harga * jumlah

    garis()
    print("=====STRUK PEMBELIAN=====")
    print(f"Nama Pelanggan : {nama}")
    print(f"Buah Dipilih   : {buah}")
    print(f"Jumlah         : {jumlah} kg")
    garis()
    print(f"Total Bayar    : Rp {total:,.1f}")
    garis()
    print("Terima kasih atas pembelian Anda!")
    garis()

    ulang = input("Ingin membeli buah lagi? (ya/tidak): ").lower()
    if ulang != "ya":
        garis()
        print("         Terima kasih telah berbelanja di toko kami")
        print("                         Sampai jumpa              ")
        garis()
        break