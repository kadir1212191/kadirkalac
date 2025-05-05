yumurta_sayisi = int(input("Bugün kaç tane yumurta toplandı?:"))
kutu12 = yumurta_sayisi // 12
print("12lik kutulardan", kutu12, "tane gerekiyor.")
kalan = yumurta_sayisi % 12
if kalan >= 6:
    print("Ek olarak 1 adet 6'lık kutuya da ihtiyaç var.")
    kalan = kalan - 6
else:
    print("6'lık kutuya ihtiyaç yok.")
print("kahvaltı için", kalan,"yumurta kaldı.")