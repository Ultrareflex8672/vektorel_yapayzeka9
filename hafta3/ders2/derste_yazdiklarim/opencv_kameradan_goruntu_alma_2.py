import cv2

vid = cv2.VideoCapture(0) 
# 1, 2 diğer kameralar

while True:
    ret, frame = vid.read()
    cv2.imshow('frame',frame)
    tus = cv2.waitKey(1000)
    # bir saniye bekle
    if tus == ord('q'): break

vid.release()
cv2.destroyAllWindows()

# waitKey(1) == ord('q') # çalışmazsa
# waitKey(1) & 0xFF == ord('q') # kullan
# Bu platform ile ilgili bir konu
