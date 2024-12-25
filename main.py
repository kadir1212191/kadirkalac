hesap_bakiyesi = float(input("Başlangıç bakiyesini girin: "))
islem = input("İşlem türünü girin (Para Yatırma / Para Çekme): ")
tutar = float(input("İşlem tutarını girin: "))
if islem == "Para Yatırma":
  hesap_bakiyesi += tutar
if islem == "Para Çekme":
  hesap_bakiyesi -= tutar
else:
 print("Geçersiz İşlem")
 
  