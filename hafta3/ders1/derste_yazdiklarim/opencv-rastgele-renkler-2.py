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


cv2.imshow("Olusan resim", r1) # Oluşan resmi gösterir
cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler
cv2.destroyAllWindows() # Pencereleri kapatır