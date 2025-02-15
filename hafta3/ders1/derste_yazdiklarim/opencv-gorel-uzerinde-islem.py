import cv2
import random
import numpy as np

r1= np.full((720, 1280, 3), [0,0,0], dtype=np.uint8) # 720x1280 boyutunda 3 kanallı 0,0,0 renkli dizi

rastgele_satir = random.randint(0,719) # 0'dan 719'a kadar rastgele bir satır seçer
rastgele_sutun = random.randint(0,1279) # 0'dan 1279'a kadar rastgele bir sütun seçer

r1[rastgele_satir,rastgele_sutun]=[255,255,255] # 360, 640 koordinatındaki pikseli beyaz yapar

ranging = 50 # 10 birimlik bir aralık belirler
if ranging != 0: # 0 değilse
    for i in range(0,720,ranging): # 0'dan 720'ye kadar 10'ar 10'ar artarak
        for j in range(0,1280,ranging): # 0'dan 1280'e kadar 10'ar 10'ar artarak
            r1[i,j]=[255,255,255] # 720x1280 boyutunda 3 kanallı r1 dizisine beyaz renkler atar

ranging_pixel = 0 # 10 birimlik bir aralık belirler
count = 0
if ranging_pixel != 0: # 0 değilse
    for i in range(ranging_pixel): # 0'dan ranging_pixel değerine kadar 1'er 1'er artarak
        count += 1
        r1[rastgele_satir+count,rastgele_sutun+count]=[255,255,255] 

cv2.imshow("Olusan resim", r1) # Oluşan resmi gösterir
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler
cv2.destroyAllWindows() # Pencereleri kapatır