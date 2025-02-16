import numpy as np

# CSV dosyası okuma
dizi1 = np.genfromtxt("hafta3/ders2/derste_yazdiklarim/ornekCSVdosyasi.csv",delimiter=",", names=True)
print(dizi1)


# CSV dosyası yazma
import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])
np.save("hafta3/ders2/derste_yazdiklarim/numpy_dosya_islemleri",arr1)
