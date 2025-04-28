girdi = raw_input("Lütfen sayıları virgülle ayırarak girin: ")
my_list = [int(sayi.strip()) for sayi in girdi.split(",")]
cift_sayilar = [sayi for sayi in my_list if sayi % 2 == 0]

print "Çift sayılar:", cift_sayilar
