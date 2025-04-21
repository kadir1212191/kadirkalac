metin = input("Bir metin girin: ")
harf = input("Silmek istediğiniz harfleri girin: ")

for karakter in harf:
  metin= metin.replace(karakter, "")
  
print(metin)