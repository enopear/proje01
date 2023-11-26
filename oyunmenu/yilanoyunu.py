import pygame
import time
import random
def baslat():
    pygame.init()

        # Ekran boyutları
    genislik = 800
    yukseklik = 600

        # Renkler
    siyah = (0, 0, 0)
    beyaz = (255, 255, 255)
    kirmizi = (255, 0, 0)

        # Yılan özellikleri
    yilan_bas = [100, 50]
    yilan_govde = [[100, 50], [90, 50], [80, 50]]
    yilan_hareket = [10, 0]
    yilan_uzunluk = 3

        # Yem özellikleri
    yem_pozisyon = [random.randrange(1, (genislik//10)) * 10, random.randrange(1, (yukseklik//10)) * 10]
    yem_var = True

        # Ekran oluşturma
    ekran = pygame.display.set_mode((genislik, yukseklik))
    pygame.display.set_caption('Yılan Oyunu')

        # Yılan hızı
    fps = pygame.time.Clock()
    oyun_hizi = 15

    def yilan_cek(yilan_govde):
            for segment in yilan_govde:
                pygame.draw.rect(ekran, beyaz, pygame.Rect(segment[0], segment[1], 10, 10))

    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                keys = pygame.key.get_pressed()
                for key in keys:
                    if keys[pygame.K_LEFT]:
                        yilan_hareket = [-10, 0]
                    elif keys[pygame.K_RIGHT]:
                        yilan_hareket = [10, 0]
                    elif keys[pygame.K_UP]:
                        yilan_hareket = [0, -10]
                    elif keys[pygame.K_DOWN]:
                        yilan_hareket = [0, 10]

            # Yılanın hareketi
            yilan_bas[0] += yilan_hareket[0]
            yilan_bas[1] += yilan_hareket[1]

            # Yılanın sınırlarını kontrol etme
            if yilan_bas[0] < 0 or yilan_bas[0] >= genislik or yilan_bas[1] < 0 or yilan_bas[1] >= yukseklik:
                pygame.quit()
                quit()

            # Yılanın kendisine çarpma kontrolü
            for segment in yilan_govde[1:]:
                if yilan_bas == segment:
                    pygame.quit()
                    quit()

            # Yılanın uzunluğunu kontrol etme
            yilan_govde.insert(0, list(yilan_bas))
            if yilan_bas[0] == yem_pozisyon[0] and yilan_bas[1] == yem_pozisyon[1]:
                yem_var = False
            else:
                if len(yilan_govde) > yilan_uzunluk:
                    yilan_govde.pop()

            # Yeni yem oluşturma
            if not yem_var:
                yem_pozisyon = [random.randrange(1, (genislik//10)) * 10, random.randrange(1, (yukseklik//10)) * 10]
                yem_var = True

            # Ekran temizleme
            ekran.fill(siyah)

            # Yılanı çizme
            yilan_cek(yilan_govde)

            # Yemi çizme
            pygame.draw.rect(ekran, kirmizi, pygame.Rect(yem_pozisyon[0], yem_pozisyon[1], 10, 10))

            pygame.display.flip()

            fps.tick(oyun_hizi)

