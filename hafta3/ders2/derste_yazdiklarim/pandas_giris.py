import pandas as pd

mydataset = {   # dictionary
  'Arabalar': ["BMW", "Volvo", "Ford"],
  'Satışlar': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset) # pandas.DataFrame() fonksiyonu ile dictionary'den DataFrame oluşturuldu.

print(myvar) # DataFrame ekrana yazdırıldı.

