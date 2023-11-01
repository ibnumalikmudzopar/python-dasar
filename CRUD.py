# program crud perpustakaan


buku = []


def show_data():
    if len(buku) <= 0:
        print("Data Buku Kosong")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))


def insert_data():
    data_baru = input("Masukan Data Buku = ")
    buku.append(data_baru)


def edit_data():
    show_data()
    indeks = int(input("Masukan ID buku: "))
    if indeks > len(buku):
        print("ID salah")
    else:
        judul_baru = input("Masukan Judul Baru: ")
        buku[indeks] = judul_baru


def delete_data():
    show_data()
    indeks = int(input("Masukan ID Buku: "))
    if indeks > len(buku):
        print("ID Salah!")
    else:
        buku.remove(buku[indeks])
        print("Data Buku %s telah dihapus" % indeks)


# menampilkan menu
def show_menu():
    print("\n")
    print("-------------MENU------------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")

    menu = int(input("PILIH MENU> "))
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
        exit()
    else:
        print("Salah Pilih!!!")


# menjalankan show_menu() ketika file CRUD.py ini dijalankan
# tidak dipakai ketika file CRUD.py ini hanya menjadi modul
if __name__ == "__main__":

    while True:
        show_menu()
