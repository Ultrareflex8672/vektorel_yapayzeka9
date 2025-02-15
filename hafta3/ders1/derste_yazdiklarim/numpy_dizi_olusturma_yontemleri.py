import numpy as np

birlerdizisi = np.ones((3, 3)) # 3x3 boyutunda 1'lerden oluşan dizi
sifirlardizisi = np.zeros((3, 3)) # 3x3 boyutunda 0'lardan oluşan dizi
birimmatris = np.eye(5) # 5x5 boyutunda birim matris
araliklidizi = np.arange(50, 100, 5) # 50'den 100'e kadar 5'er artan dizi
tersaraliklidizi = np.arange(100, 50, -5) # 100'den 50'ye kadar 5'er azalan dizi

print(birlerdizisi)
print(sifirlardizisi)
print(birimmatris)
print(araliklidizi)
print(tersaraliklidizi)

tersaraliklidizi = araliklidizi[::-1] # Diziyi tersine çevirmek
print(tersaraliklidizi) # 95, 90, 85, 80, 75, 70, 65, 60, 55, 50

boyutdegistirme = araliklidizi.reshape(2, 5) # Dizinin boyutunu değiştirmek
print(boyutdegistirme)

tekboyutludizi = np.array([19, 2, 5, 9, 8, 7]) # Tek boyutlu dizi
ikiboyutludizi = np.array([[19, 2, 5], [9, 8, 7]]) # İki boyutlu dizi
ucboyutludizi = np.array([[[19, 2, 5], [9, 8, 7]], [[19, 2, 5], [9, 8, 7]]]) # Üç boyutlu dizi
print(tekboyutludizi)
print(ikiboyutludizi)
print(ucboyutludizi)