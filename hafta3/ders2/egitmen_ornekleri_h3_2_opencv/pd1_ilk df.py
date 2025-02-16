import pandas as pd
print(pd.__version__)

arac_satis_verileri = {
    "arabalar":["bmw","ferrari","togg"],
    "satis_rakamlari":[200,10,150]    
}

pandas_ile_olusan_dizi = pd.DataFrame(arac_satis_verileri)
print(pandas_ile_olusan_dizi)