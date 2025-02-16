# Resim açma, gri tonlu
import cv2
img1 = cv2.imread('resimler/beyazresim.png')
img2 = cv2.imread('resimler/beyazresim.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('Deneme',img1)
# cv2.imshow('Deneme2',img2)
cv2.waitKey(0)# herhangi bir tuşa basılana kadar bekle
cv2.destroyAllWindows()
print(img2)
print("------------")
print(img1)
