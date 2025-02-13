import numpy as np

dizi = np.array([1, 2, 3, 4, 5])
print(dizi)

matris = np.array([[1, 2], [3, 4], [5, 6]])
print(matris)

sayilar = np.array([5], dtype=np.uint8)  # 8 bit lik olarak ayarlandı
ikili_temsil = np.unpackbits(sayilar)
print(ikili_temsil)  # 5 sayısının ikili sistemdeki hali: [0 0 0 0 0 1 0 1]
