kelime = input("Bir sözcük girin: ")
sesliler = "aeıioöuü"
sayac = 0

for harf in kelime:
  if harf in sesliler:
    sayac +=1
    
print(sayac)
