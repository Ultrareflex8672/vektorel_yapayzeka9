import cv2
import numpy as np

# aşağıdaki [255, 255, 255] rakamlarını oynayarak ne olduğuna bakın
r1= np.full((720, 1280, 3), [10, 100, 75], dtype=np.uint8) # 720x1280 boyutunda 3 kanallı 10, 100, 75 renkli dizi
# print(r1)

cv2.imshow("Olusan resim", r1) # Oluşan resmi gösterir

cv2.waitKey(0) # Kullanıcı bir tuşa basana kadar bekler
 
cv2.destroyAllWindows() # Pencereleri kapatır
