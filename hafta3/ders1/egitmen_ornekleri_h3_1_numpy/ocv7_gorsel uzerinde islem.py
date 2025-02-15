# restgele renklerden oluşan resim..
import cv2, random, numpy as np

r1= np.full((200, 300, 3), [0, 0, 0], dtype=np.uint8)
# cv2.imshow("Resim", r1)
# cv2.waitKey(0)

# r1[x,y]=[m1, y1, k1]
y = random.randint(0,300)
x = random.randint(0,200)
r1[x,y]=[255,255,255]
r1[x,y+1]=[255,255,255]
r1[x,y+2]=[255,255,255]
   
cv2.imshow("Resim", r1)
cv2.waitKey(0)
 
cv2.destroyAllWindows()