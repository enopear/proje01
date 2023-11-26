import turtle
def kare():
    kenar1 = int(input("Karenin kenarı kaç pixel olsun "))
    for i in range(4):
        turtle.forward(kenar1)
        turtle.right(90)
def ucgen():
    kenar2 = int(input("Üçgenin kenarı kaç pixel olsun "))
    for i in range(3):
        turtle.forward(kenar2)
        turtle.right(120)
def besgen():
    kenar3 = int(input("Beşgenin kenarı kaç pixel olsun "))
    for i in range(5):
        turtle.forward(kenar3)
        turtle.right(72)
def altigen():
    kenar4 = int(input("Atlıgenin kenarı kaç pixel olsun "))
    for i in range(6):
        turtle.forward(kenar4)
        turtle.right(60)
def resimmenu():
  turtle.speed(10)
  secmek = input("Kenar rengi kırmızı mı mavi mi ")
  if secmek =="kırmızı":
      turtle.color("red")
  elif secmek == "mavi":
      turtle.color("blue")
  else:
      print("Başka renk seçeneği yoktur")

  print("╔═════════════════════╗")
  print("║ RESİM MENÜSÜ        ║")
  print("║                     ║")
  print("║  1-KARE ÇİZME       ║")
  print("║  2-ÜÇGEN ÇİZME      ║")
  print("║  3-BEŞGEN ÇİZME     ║")
  print("║  4-ALTIGEN ÇİZME    ║")
  print("║  5-Çıkış            ║")
  print("║   Seçiminiz:        ║")
  print("╚═════════════════════╝")
  
while True:
  resimmenu()
  secim = int(input(""))

  if secim == 1:
      kare()
    
  elif secim == 2:
      ucgen()
      
  elif secim ==3:
    besgen()
    
  elif secim == 4:
    altigen()
    
  elif secim ==5:
    print("Çıkış yapıldı")
    break
  else:
    print("Lütfen belirliten işlemlerden birini seçiniz")
