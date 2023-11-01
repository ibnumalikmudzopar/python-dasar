"""Ini adalah contoh penggunaan di dunia nyata yiaut"""


def rata_rata(*data):
    banyak_data = len(data)
    jumlah_data = sum(data)
    nilai_rata_rata = float(jumlah_data) / float(banyak_data)
    return nilai_rata_rata


print(rata_rata(2, 4, 1, 2, 4, 1, 2, 3, 4, 5, 1, 8, 2))

""""kuncinya di penamaan *nama *umur *usia dan digunakan pada parameter didalam fungsi"""
""""*args jadi tuple sedangkan **kwargs jadi dictionary"""


def panggil_nama_args(*nama):
    print("Daftar Orang Yang Dipangil: ")
    for orang in nama:
        print(orang)


def panggil_nama_kwargs(**isi):
    print(isi)


def panggil(nama):
    print("Daftar Orang Yang Dipangil: ")
    for orang in nama:
        print(orang)


#  pemanggilan fungsi
panggil_nama_args("Jimi", "Ibnu", "Malik")
panggil_nama_kwargs(tujuan=123, pesan="hai")
# panggil("Iben", "Jirdan")  #  akan error ketika menggunakan 2 paramater
