#06 Pasta dilimi
import matplotlib.pyplot as plt 
kategoriler = ["1.Sınav","2.Sınav","3.Sınav"] # kategorileri belirler
degerler = [80,70,90] # değerleri belirler


plt.title('Kategoriye Göre Değerler') # başlık belirler
plt.pie(degerler,labels=kategoriler) # pasta dilimi grafiğini çizer
plt.show() # grafiği gösterir