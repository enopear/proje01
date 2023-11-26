import random
def yazi_turaoyunu(): 
    yazi_tura  = random.randint(1, 2)
    tahmin = input("Yazı mı Tura mı  ")

 
    if yazi_tura == 1:
        sonuc = "Yazı"

        if tahmin == sonuc:
            print("Doğru bildin...")
        else: print("Bilemedin...")
    else:
        sonuc = "Tura"
        if tahmin == sonuc:
            print("Doğru bildin...")
        else: print("Bilemedin...")




