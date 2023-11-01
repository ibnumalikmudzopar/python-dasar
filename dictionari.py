# dalam pemrogramman PHP dictionari dikenal sebagai asosiatif array

aku = {
    "nama": "Ibnu Malik Mudzopar",
    "umur": 23,
    "hobi": ["membaca", "sepak bola", "badminton"],
    "menikah": False,
    "sosmed": {
        "instagram": "jimjirdan",
        "facebook": "ibnumalikmudzopar"
    }
}
nama_dict = {
    "key": "value"
}

# cara lain penggunaan dictionary

warna_buah = dict(jeruk="kuning", apel="merah", kedongdong="hijau")

# saat nya mengakses isi dari dictionary

print("Nama saya {}".format(aku["nama"]))
print("umur saya %d " % aku["umur"])
print("Username instagram saya : %s " % aku["sosmed"]["instagram"])
print(aku.get("menikah"))
for key in aku:
    print(aku[key])
for key, val in aku.items():
    print("%s : %s " % (key, val))

# mengubah val dari umur didalam aku

aku["umur"] = 17
print(aku.get("umur"))
aku["hobi"] = "makan", "minum"
print(aku.get("hobi"))

# menghapus
print(aku.get("umur"))
aku.pop("umur")  # menghapus key umur didalam dict aku
print(aku.get("umur"))
aku.update({"umur": 23})  # menambahkan
print(aku.get("umur"))
del aku["umur"]  # menghapus umur didalam dict aku

if aku.get("umur"):
    print(aku.get("umur"))
else:
    aku.update({"umur": 16})
    print(aku.get("umur"))

print("Total hobi saya sejumlah: %d " % len(aku["hobi"]))
print("yaitu:")
print(aku.get("hobi"))
