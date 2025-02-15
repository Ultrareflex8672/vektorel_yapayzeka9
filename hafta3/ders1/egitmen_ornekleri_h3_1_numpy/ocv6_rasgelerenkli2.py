# restgele renklerden oluşan resim..
import cv2, random, numpy as np

r1= np.full((200, 300, 3), [0, 0, 0], dtype=np.uint8)
cv2.imshow("Resim", r1)
cv2.waitKey(0)

for x in range(200):
   for y in range(300):
        m1=random.randint(0,255)
        y1=random.randint(0,255) 
        k1=random.randint(0,255)
        r1[x,y]=[m1, y1, k1]
   
cv2.imshow("Resim", r1)
cv2.waitKey(0)
 
cv2.destroyAllWindows()