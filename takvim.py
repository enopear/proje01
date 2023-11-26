from datetime import date


def Takvim():
    today = date.today() 

    print("Yıl:", today.year)
    print("Ay :", today.month)
    print("Gün:", today.day)
