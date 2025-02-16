# pip install opencv-python
# https://www.tamindir.com/indir/paintnet/
# Resim açma
import cv2
# img = cv2.imread('resimler/squirrel1.jpg')
img = cv2.imread('resimler/bayrak2.jpg')
print(img)
# cv2.imshow('Deneme',img)
cv2.waitKey(3000) # 3 saniye bekle
cv2.destroyAllWindows() # pencereleri kapa