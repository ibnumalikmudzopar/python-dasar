laci = ["nasgor", 20, True, 34.12]
laci[0] = "nasi"  # mengganti isi laci
print(laci[0])

print("contoh program memakai list")

my_friends = ["anda", "saya", "kamu", "kami", "kau"]
print("isi my_friend index ke - 3 adalah {} ".format(my_friends[3]))
print("semua teman: ada {} orang".format(len(my_friends)))
for friend in my_friends:
    print(friend)

# mengganti nilai list
# append = menambahkan

buah = ["apel", "mangga", "jeruk", "kedongdong"]
print("Sebelum menggunakan append", buah)
buah.append("duren")
print("setelah menggunakan append", buah)
# buah.prepend("anggur")
# print("setelah menggunakan prepend=", buah)
buah.insert(2, "bonteng")
print("Setelah menggunakan insert", buah)
# memotong list
print("memotong list", buah[1:5])
# menghapus item dari list
del buah[3]
print("setelah menggunakan fungsi del pada index 3", buah)
