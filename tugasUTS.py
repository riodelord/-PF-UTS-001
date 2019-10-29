nama = []
hasil_kotor = []
zakat = []
hitung_asasi = []
bersih = []
def show_data():
    print("No  Nama\tPenghasilan Kotor\tPenghasilan Bersih")
    if len(nama) <= 0:
        print ('Belum ada data')
    else:
        for i in range(len(nama)):
            print(i+1, nama[i],"Rp." + str(hasil_kotor[i]), "Rp. " + str(bersih[i]))

def insert_data():
    nama_tambah = input("Masukan Nama Yang diinginkan : ")
    nama.append(nama_tambah)
    kotor = int(input("Masukan Hasil Kotor : "))
    hasil_kotor.append(kotor)
    asasi = int(input("Pengeluaran Asasi : "))
    hitung_asasi.append(asasi)
    bersihhasil = kotor-asasi
    bersih.append(bersihhasil)


def edit_data():
    show_data()
    i = int(input("Inputkan Key :"))
    if (i > len(nama)):
        print ("ID tidak ada")
    else:
        nama_baru = input("Nama Baru : ")
        nama[i-1] = nama_baru

def delete_data():
    show_data()
    i = int(input("Inputkan Key :"))
    if (i > len(nama)):
        print("ID tidak ada")
    else:
        del (nama[i - 1])

def perhitungan_bersih():
    show_data()
    i = int(input("Inputkan Key :"))
    if (i > len(nama)):
        print("ID tidak ada")
    else:
        print("  Penghasilan Kotor\tAsasi\tPenghasilan Bersih")
        print("Rp.", hasil_kotor[i-1], " - ", "Rp.", hitung_asasi[i-1], " = ", "Rp.", bersih[i-1])

def hitung_zakat():
    print("test11")


def show_menu():
    print("\n")
    print("+++++++++MENU+++++++++++++")
    print("[1] Show data")
    print("[2] Insert data")
    print("[3] Edit data")
    print("[4] Delete data")
    print("[5] Perhitungan bersih")
    print("[6] Exit")

    menu = int(input("Masukan Menu > "))
    print("\n")
    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        perhitungan_bersih()
    elif menu == 6:
        hitung_zakat()
    elif menu == 7:
        quit()
    else :
        print("Inputan Salah!")

if __name__ == "__main__":
    while (True):
        show_menu()