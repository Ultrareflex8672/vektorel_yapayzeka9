import random, cv2, numpy as np
resim = []
satirdizisi = []
for satir in range(2):
    for sutun in range(5):
        a = random.randint(0,255)
        b = random.randint(0,255) 
        c = random.randint(0,255)
        renk = [a,b,c]
        satirdizisi.append(renk)
        print(renk)
    resim.append(satirdizisi)
# print(satirdizisi)
print(resim)


# r1= np.full((200, 300, 3), [a, b, c], dtype=np.uint8)
r1 = np.array(resim)
cv2.imshow("Resim", r1)
# print(f"Mavi:{a}, Yeşil:{b}, Kırmızı:{c}")
cv2.waitKey(0)
        
cv2.destroyAllWindows()