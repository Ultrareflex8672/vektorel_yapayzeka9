# ör-1: Kameraya erişme (tuşa bastıkça)
import cv2

kaynak = cv2.VideoCapture(0) 
# 1, 2 diğer kameralar

while True:
    ret, frame = kaynak.read()
    # ret= görüntü var/yok
    # frame= okunan görüntü 
    cv2.imshow('frame',frame)
    print(frame)
    tus = cv2.waitKey(10)
    # waitKey (bekleme süresi). 0 tuşa basana kadar
    if tus == ord('q'): break

kaynak.release()
cv2.destroyAllWindows()