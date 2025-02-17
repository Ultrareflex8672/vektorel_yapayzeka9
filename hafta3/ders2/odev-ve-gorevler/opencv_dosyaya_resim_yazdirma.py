import cv2
import random
import numpy as np

r1= np.full((720, 1280, 3), [0,0,0], dtype=np.uint8) # 720x1280 boyutunda 3 kanallı 0,0,0 renkli dizi

for satir in range(720):
    for sutun in range(1280):
        a = random.randint(0,255)
        b = random.randint(0,255)
        c = random.randint(0,255) 
        r1[satir,sutun]=[a,b,c] # 720x1280 boyutunda 3 kanallı r1 dizisine rastgele renkler atar

rastgele_satir = random.randint(0,719) # 0'dan 719'a kadar rastgele bir satır seçer
rastgele_sutun = random.randint(0,1279) # 0'dan 1279'a kadar rastgele bir sütun seçer

r1[rastgele_satir,rastgele_sutun]=[255,255,255] # 360, 640 koordinatındaki pikseli beyaz yapar

ranging_pixel = 360 # 10 birimlik bir aralık belirler
count = 0
if ranging_pixel != 0: # 0 değilse
    for i in range(ranging_pixel): # 0'dan ranging_pixel değerine kadar 1'er 1'er artarak
        count += 1
        r1[rastgele_satir+count,rastgele_sutun+count]=[255,255,255] 

cv2.imwrite('hafta3/ders2/derste_yazdiklarim/rastgele.jpg',r1) # Oluşan resmi rastgele.jpg adında renkli kaydeder
img = cv2.imread('hafta3/ders2/derste_yazdiklarim/rastgele.jpg',0)  # Oluşan resmi siyah beayaz olarak okur
cv2.imwrite('hafta3/ders2/derste_yazdiklarim/rastgele.jpg',img) # Siyah beyaz olarak okunan dosyayı siyah beyaz resm rastgele.jpg adında kaydeder

print(r1) # Oluşan resmi ekrana yazdırır
print("r1 dizisinin boyutu: ", r1.shape) # Oluşan resmin boyutunu ekrana yazdırır
print("---------------------------------------------------")
print(img) # Siyah beyaz olarak okunan resmi ekrana yazdırır
print("img dizisinin boyutu: ", img.shape) # Siyah beyaz olarak okunan resmin boyutunu ekrana yazdırır

cv2.imshow("Olusan resim", r1) # Oluşan resmi gösterir
cv2.imshow("Olusan resim - Siyah Beyaz", img)   # Siyah beyaz olarak okunan resmi gösterir
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler
cv2.destroyAllWindows() # Pencereleri kapatır

# Görselin boyutlarını al
height, width, _ = r1.shape

# Sarı renkte 5 piksel kalınlığında çerçeve ekle
cv2.rectangle(r1, (0, 0), (width-1, height-1), (0, 255, 255), 5)

# Çerçeveli resmi kaydet
cv2.imwrite('hafta3/ders2/derste_yazdiklarim/rastgele_cerceveli.jpg', r1)

# Çerçeveli resmi göster
cv2.imshow("Olusan resim - Cerceveli", r1)
cv2.waitKey(0)
cv2.destroyAllWindows()

