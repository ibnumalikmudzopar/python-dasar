# tuple adalah list yang tidak bisa diubah isinya atau immutable
tuple1 = 1234, 567, 'Hello'
tuple2 = (8910, 111213, 'World!')
tuple3 = ([4, 5, 6], {'nama': 'jim', 'umur': 23}, True)
tuple4 = ([1, 2, 3], {'nama': 'Petanikode', 'rank': 123}, True)

# tuple kosong
kosong = ()

# membuat singleton
u = ('singleton',)  # kalo tidak pake koma akan dianggap string
v = 'singleton'  # ini string

print(tuple1[0])
print(tuple2[1:3])
print("Jumlah isi t %d" % len(tuple1))
print(tuple1, tuple2)  # nested tuple

# sequency unpacking
# Menggunakan sequence unpacking dengan list
my_list = [1, 2, 3]
a, b, c = my_list
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Menggunakan sequence unpacking dengan tuple
my_tuple = ('x', 'y', 'z')
d, e, f = my_tuple
print(d)  # Output: 'x'
print(e)  # Output: 'y'
print(f)  # Output: 'z'

# mencoba sequence sendiri
tuple_buah = ('apel', 'kedongdong', 'tomat')
g, h, i = tuple_buah
print(g)
print(h)
print(i)

# sequence dari petani kode
web = (123, "Petani Kode", "https://www.petanikode.com")
id_web, nama_web, url_web = web

print(id_web)
print(nama_web)
print(url_web)
