# perulangan while if
jawab = 'ya'
hitung = 0

while True:
    hitung += 1
    jawab = input("Ulangi lagi tidak? ")
    if jawab == 'tidak':
        break

print(f"total Perulangan: {hitung}")
