# Resim açma
import cv2
img = cv2.imread('hafta3/ders2/derste_yazdiklarim/sincap.png')
print(img)  # None döner
cv2.imshow('Deneme',img)

# Resim açma, gritonlu
img1 = cv2.imread('hafta3/ders2/derste_yazdiklarim/sincap.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Deneme1',img1)  

# Resim açma, siyah beyaz
img2 = cv2.imread('hafta3/ders2/derste_yazdiklarim/sincap.png', 0) # IMREAD_GRAYSCALE
cv2.imshow('Deneme2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows() 
