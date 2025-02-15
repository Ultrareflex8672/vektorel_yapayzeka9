import cv2
import numpy as np
for a in range(255):
    for b in range(255):
        for c in range(255):
            r1= np.full((720, 1280, 3), [a, b, c], dtype=np.uint8) # 720x1280 boyutunda 3 kanallı 10, 100, 75 renkli dizi
            cv2.imshow("Olusan resim", r1) # Oluşan resmi gösterir
            cv2.waitKey(30) # Kullanıcı bir tuşa basana kadar bekler

cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler
cv2.destroyAllWindows() # Pencereleri kapatır