import random
print("Hello World!!!")
print("Selamat Datang Di Program Python")
print("Saya Belajar Python dengan Pycharm")
print("Salam Kenal JimJirdann")
print("saat ini tanggal 27 oktober 2023")
print("-------------------")
print("String & Case Style")
judul = 'Belajar Python Sampai Bisa'
Judul = '''Belajar Python Sampai Bisa'''
penulis = "jimjirdann"
Penulis = """jimjirdann"""
print("Case Yang disarankan")
print("1. Snake Case digunakan pada: module_name, package_name, method_name, function_name, , global_var_name, "
      "instance_var_name, function_parameter_name, local_var_name. \n2. CamelCase digunakan Pada:ClassName, "
      "ExceptionName \n3. ALL CAPS digunakan Pada:GLOBAL_CONSTANT_NAME")
print("-------------------")
print("blok program python")
username = 'jimjirdann'
# Blok Percabangan if
if username == 'jimjirdann':
    """if expression ini digunakan untuk contoh penulisan blok saja"""
    print("Selamat Datang Admin")
    print("Silahkan Ambil Tempat Duduk")
# Blok Percabangan for
for i in range(4):
    print(i)
print("--------------------")
print('Variable')
variabel_ku = "ini isi variable"
variabel2 = 20
_variable3 = 2
variableKu = 5
VariableKu = 1
print(variabel_ku)
print(variabel2)
print(VariableKu)
print(variableKu)
# del(_variable3)
print(_variable3)
print('----------------')
print("Tipe Data")
nama_ku = "jimjirdann"
jenis_kelamin = 'L'  # tipe data char
umur = 23
tinggi = 171.234
alamat = "Majalengka"
menikah = 0  # 0=false boolean
jarak = 3e3
print("Nama : ", nama_ku)
if menikah:
    print("Status: Menikah")
else:
    print("Status: Belum Menikah")
tipe = type(jenis_kelamin)
print(tipe)
print('------------------')
print('Konversi Tipe Data')
a = 10
b = 3
c = float(a) / float(b)
""""int() long,bool,chr,str,bin,hex,oct"""
print(c)
print('--------------------')
print("INPUT DAN OUTPUT dari keyboard")
nama = input("Siapa nama kamu: ")
umur = input("berapa umur kamu: ")
angka = input("Pilih angka 1-9: ")
print("Hello", nama, "umur kamu adalah %s" % umur)  # %s %d %f string decimal float
print("angka yang kamu pilih adalah: {}".format(angka))
print('------------------')
print("Operator")
"""+ - * / %(hasil sisa bagi) **(pangkat)"""
a = int(input("Inputkan Nilai a: "))  # Mengubah input menjadi bilangan bulat
b = int(input("Inputkan Nilai b: "))  # Mengubah input menjadi bilangan bulat
d = int(input("Inputkan nilai d: "))
tipe = type(d)
c = a + b
print("Hasil %d + %d = %d" % (a, b, c))  # Memperbaiki pemformatan string
print("tipe data nilai d adalah: ", tipe)
print('----------------')
print("Operator Penugasan")
a = int(input("Masukan Nilai a: "))
print("Nilai a = %d" % a)
a += 2
a -= 2
a *= 2
a /= 2
a **= 2
print("Nilai a = %d " % a)
print('--------------------')
print("Operator Pembanding")
a = int(input("Masukan Nilai a: "))
b = int(input("Masukan Nilai b: "))
c = a == b
print("Apakah %d == %d: %r" % (a, b, c))
"""== < > <= >= !="""
print('----------------------')
print("Operator Logika")
a = True
b = False
c = a and b
print("%r and %r = %r" % (a, b, c))
c = a or b
print("%r or %r = %r" % (a, b, c))
c = not a
print("not %r = %r" % (a, c))
print('----------------')
print("Operator Bitwise")  # melakukan operasi berdasarkan biner/bit
"""and& or| xor^ negative~ leftshift<< rightshift>>"""
a = int(input("Masukan angka a: "))
b = int(input("Masukan angka b: "))
# operasi and
c = a & b
print("operasi and a & b = %s" % c)
# operasi or
c = a | b
print("operasi or   a | b = %s" % c)
c = a ^ b
print("operasi XOR  a ^ b = %s" % c)
c = ~a
print("operasi not  a = %s" % c)
c = a << b
print("operasi shiftleft a << b = %s" % c)
c = a >> b
print("operasi rightleft a >> b = %s" % c)
print('--------------')
print("Game tebak angka random")
number = random.randint(1, 10)

guess = int(input("tebak angka 1 - 10= "))

if guess == number:
    print("You Won!")
else:
    print("You Lose!")
    print("Number yang benar adalah: {}".format(number))

print("----------------------------------------------------")
print('Opeartor Ternary(Kondisi)')
umur = int(input("Berapa Umur Kamu? "))
aku = "bocah" if umur < 10 else "Dewasa"
print(aku)
# cara lain menggunakan operasi ternary menggunakan tuple dan list
jomblo = True
status = ("Menikah", "Single")[jomblo]
print(status)
print('---------------------')
print('percabangan')
lulus = input("Apakah Kamu lulus? [ya/tidak]: ")
if lulus == "tidak":
    print("Kamu harus ikut ujian")
