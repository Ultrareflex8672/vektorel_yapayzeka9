# Resim kaydetme
import cv2
# img = cv2.imread('resimler/squirrel1.jpg')
img = cv2.imread('resimler/bayrak2.jpg')
img2 = cv2.imread('resimler/bayrak2.jpg', cv2.IMREAD_GRAYSCALE)
# print(img2)
cv2.imshow('Deneme',img2)
cv2.imwrite('resimler/bayrak2sb.jpg',img2)
cv2.waitKey(3000) # 3 saniye bekle
cv2.destroyAllWindows() # pencereleri kapa

import cv2

# Örnek bir resim yükleyelim

# Resmin boyutlarını öğrenelim
height, width = img2.shape

print(f'Height: {height}, Width: {width}, Channels: {channels}')