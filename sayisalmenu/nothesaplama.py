def nothesaplamayıbaslat():
  x = int(input("Kaç yazılı notunuz var  "))
  yazilitoplam = 0
  for i in range(x):
      y = int(input(f"{i+1}. Yazılı notunu giriniz  "))
      yazilitoplam += y
  ortlama = yazilitoplam/x
  print(f"Ortalama Notunuz {ortlama}")