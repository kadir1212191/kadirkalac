girdi = raw_input("Sayıları virgülle ayırarak girin: ")
my_list = [int(i) for i in girdi.split(",")]
toplam = 0
for sayi in my_list:
    toplam += sayi

print toplam
