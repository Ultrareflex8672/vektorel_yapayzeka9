import pandas as pd
print(pd.__version__)

# arac_satis_verileri = {
#     "arabalar":["bmw","ferrari","togg"],
#     "satis_rakamlari":[200,10,150]    
# }
veriler = pd.read_csv("ornekveri.csv")

pandas_ile_olusan_dizi = pd.DataFrame(veriler)
print(pandas_ile_olusan_dizi)
