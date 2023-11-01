# program bonus atau diskon untuk orang yang belanja
# program ini dalam rangka belajar percangan if
total_belanja = int(input("Berapa Jumlah Total Belanja Anda?: "))

if total_belanja >= 300000:
    print("Kamu Mendapat Diskon Sebesar 5%")

diskon = total_belanja * 5/100
bayar = total_belanja - diskon
print("Total yang harus dibayar: RP{}".format(bayar))
print("Terima Kasih sudah berbelanja\nDatang lagi ya")
