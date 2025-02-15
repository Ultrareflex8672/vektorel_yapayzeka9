#01 3 sınavdan aldığımız puanlar
import matplotlib.pyplot as plt
plt.plot([1,2,3], [80,70,90])
plt.show()

#02 Kategori adları
import matplotlib.pyplot as plt
plt.plot(["1.Sınav","2.Sınav","3.Sınav"], [80,70,90])
plt.show()

#03 Sütun grafiği
import matplotlib.pyplot as plt
plt.bar(["1.Sınav","2.Sınav","3.Sınav"], [80,70,90])
plt.show()

#04 verileri ayırma
import matplotlib.pyplot as plt
kategoriler = ["1.Sınav","2.Sınav","3.Sınav"]
degerler = [80,70,90]
plt.bar(kategoriler, degerler)
plt.show()

#05 Başlık ve etiket ve değer ekleme
import matplotlib.pyplot as plt
kategoriler = ["1.Sınav","2.Sınav","3.Sınav"]
degerler = [80,70,90]

plt.title('Kategoriye Göre Değerler')
# X ve Y eksenlerine etiketler ekleme
plt.xlabel('Kategoriler')
plt.ylabel('Değerler')

plt.plot(kategoriler, degerler)
plt.show()

#06 Pasta dilimi
import matplotlib.pyplot as plt
kategoriler = ["1.Sınav","2.Sınav","3.Sınav"]
degerler = [80,70,90]

plt.title('Kategoriye Göre Değerler')
plt.pie(degerler,labels=kategoriler)
plt.show()

#06 Veri etiketleri
import matplotlib.pyplot as plt

# Kategoriler ve değerler
kategoriler = ["1.Sınav", "2.Sınav", "3.Sınav"]
degerler = [80, 70, 90]
# Sütun grafiği oluşturma

plt.title('Kategoriye Göre Değerler')
plt.xlabel('Kategoriler')
plt.ylabel('Değerler')

plt.bar(kategoriler, degerler)
plt.bar_label(plt.bar(kategoriler, degerler))

plt.show() # Grafiği gösterme

