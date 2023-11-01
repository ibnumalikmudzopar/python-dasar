hobi = []
stop = False
i = 0

while not stop:
    hobi_baru = input("Inputkan hobi yang ke -{}: ".format(i))
    hobi.append(hobi_baru)

    i += 1

    tanya = input("isi lagi(y/t): ")
    if tanya == "t":
        stop = True

# cetak hobby
print("-" * 10)
print("Kamu memiliki {} hobi".format(len(hobi)))

for hb in hobi:
    print("- {}".format(hb))
