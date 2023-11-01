# perulangan for
ulang = 10

for i in range(ulang):
    print(f"Perulangan ke-{i}")
# perulangan menggunakan senarai (list)

item = ['kopi', 'udud', 'nasi', 'teh']
for isi in item:
    print(isi)

# perulangan while
jawab = 'ya'
hitung = 0

while jawab == 'ya':
    hitung += 1
    jawab = input("Ulangi Tidak? ")

print(f"Total Perulangan: {hitung}")
# f untuk memasukan nilai variabel kedalam string
