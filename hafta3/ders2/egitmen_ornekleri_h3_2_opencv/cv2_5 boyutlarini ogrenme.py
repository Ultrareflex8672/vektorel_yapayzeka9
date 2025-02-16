import cv2

# Örnek bir resim yükleyelim
img2 = cv2.imread('resimler/bayrak2.jpg')

# Resmin boyutlarını öğrenelim
height, width, channels = img2.shape

print(f'Height: {height}, Width: {width}, Channels: {channels}')
