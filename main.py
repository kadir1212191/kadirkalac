x = ("Bir sözcük giriniz :")
y= int(input("Bir sayı girin :"))
if y<len(x):
  x1 = x[:y]
  x2 = x[y:]
  x=x1+"-"+x2
  print(x)
