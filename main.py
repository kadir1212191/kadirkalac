kelime = input("Bir sözcük girin: ")
endeks = int(input("Bir sayı girin: ")) -1
harf = input("Bir harf girin: ")

sonuc = kelime[:endeks] + harf + kelime[endeks+1:]
print(sonuc)