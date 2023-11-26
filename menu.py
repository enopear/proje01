import sayisalmenu
import takvim
import oyunmenu
import os
import time
import random
from datetime import date
import turtle
import pygame
def anamenu():
  print("╔══════════════════════╗")
  print("║  PYTHON ÇALIŞMALARI  ║") 
  print("║ 1-Hesap makinesi     ║")
  print("║ 2-Not hesapla        ║")
  print("║ 3-Sayı tahmin oyunu  ║")
  print("║ 4-Fibonacci serisi   ║")
  print("║ 5-XOX oyunu          ║")
  print("║ 6-Yılan oyunu        ║")
  print("║ 7-Sıcaklık dönüşümü  ║")
  print("║ 8-Yazı tura oyunu    ║")
  print("║ 9-Takvim             ║")
  print("║ 10-Çıkış             ║")
  print("║    Seçimiz nedir?    ║")
  print("╚══════════════════════╝")
  secim = int(input())
  if secim == 1:
    x =  int(input("İlk sayıyı girin"))
    y =  int(input("2. sayıyı girin"))
    islem = input("Dört işlemden birini işlemini yazarak seçin")
    sayisalmenu.hesapmakinesi.hesapla(x,y,islem)
    anamenu()
    
  elif secim ==2:
    sayisalmenu.nothesaplama.nothesaplamayıbaslat()
    anamenu()
    
  elif secim== 3:
    oyunmenu.sayitahmin.sayibaslat()
    anamenu()
    
  elif secim == 4:
    a = int(input("Dizi kaçıncı aşamasına kadar devam etsin: "))
    sayisalmenu.fibonacci.fibonaccibasla(a)
    anamenu()
    
  elif secim == 5:
    oyunmenu.xoxoyunu.xoxbaslat()
    anamenu()
  elif secim== 6:
    oyunmenu.yilanoyunu.baslat()
    anamenu()
  elif secim==7:
    sıcaklıksecim = int(input("Selsiyustan Fahrenheit için 1'e Fahrenheitten selsiyus için 2'ye basınız: "))
    if sıcaklıksecim==1:
      celsius = int(input("Selsiyus değerini giriniz: "))
      sayisalmenu.sıcaklıkdönüşümü.celsius_to_fahrenheit(celsius)
    elif sıcaklıksecim==2:
      fahrenheit = int(input("Fahrenheit değerini giriniz: "))
      sayisalmenu.sıcaklıkdönüşümü.fahrenheit_to_celsius(fahrenheit)
    else: 
      print("1 veya 2'ye basınız")
    anamenu()
  elif secim==8:
    oyunmenu.yazitura.yazi_turaoyunu()
    anamenu()
  elif secim==9:
    takvim.Takvim()
    anamenu()
  elif secim==10:
    print("Çıkış yapılıyor...")
    
  else:
    print("Lütfen belirtilen işlemlerden birini seçiniz")
    anamenu()
anamenu()

