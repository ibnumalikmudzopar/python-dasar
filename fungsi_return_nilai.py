""""Fungsi Yang mengembalikan nilai"""


def luas_persegi(sisi):
    luas = sisi * sisi
    return luas


print("Luas Persegi adalah: %d" % luas_persegi(6))


def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume


print("Volume Persegi adalah: %d" % volume_persegi(5))

"""Variabel Global dan Lokal"""

# contoh


# ini adalah variabel global
nama = "Jim Jirdann"
umur = 17
citacita = "Programmer"


def helpp():
    #  ini variabel lokal
    nama2 = "ibnu malik"
    umur2 = 18
    citacita2 = "developer"

    # mengakses variabel lokal
    print("Nama: %s " % nama2)
    print("umur: %d " % umur2)
    print("Cita - Cita: %s " % citacita2)


#  Mengakses variabel global
print("Nama: %s " % nama)
print("umur: %s " % umur)
print("Cita - Cita: %s " % citacita)

helpp()
