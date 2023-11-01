# operasi pada list menjumlahkan (+) dan mengkalikan (*) isi list

list_lagu = [
    "No Women, No Cry",
    "Dear God"
]

playlist_favorit = [
    "Break Out",
    "Now Loading!!!"
]

ulangi = 2

# mari kita gabungkna keduanya
semua_lagu = list_lagu + playlist_favorit

# operasi perkalian
semua_lagu2 = list_lagu * ulangi
print(semua_lagu)
print(semua_lagu2)

# catatan
# kelemahan list tidak bisa mengakses isi menggunakan kata kunci artinya hanya bisa diakses menggunanakan index
