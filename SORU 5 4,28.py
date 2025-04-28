girdi = raw_input("Lütfen sayıları virgülle ayırarak girin: ")
my_list = [int(sayi.strip()) for sayi in girdi.split(",")]
en_buyuk = my_list[0]

for sayi in my_list[1:]:
    if sayi > en_buyuk:
        en_buyuk = sayi
print "En büyük sayı:", en_buyuk
