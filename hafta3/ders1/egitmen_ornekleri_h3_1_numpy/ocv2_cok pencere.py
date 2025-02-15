import cv2 # OpenCV renk sıralaması B, G, R
import numpy as np

# aşağıdaki [255, 255, 255] rakamlarını oynayarak ne olduğuna bakın
r1= np.full((45, 90, 3), [150, 150, 150], dtype=np.uint8)
r2= np.full((45, 90, 3), [50 , 50, 50], dtype=np.uint8)
print(r1)

cv2.imshow("Olusan resim1", r1)
cv2.imshow("Olusan resim2", r2)

cv2.waitKey(0)
 
cv2.destroyAllWindows()
