import matplotlib.pyplot as plt
kategoriler = ["1.Sınav","2.Sınav","3.Sınav"]
degerler = [80,70,90]

plt.title('Kategoriye Göre Değerler')
# plt.pie([80,70,90],labels=["1.Sınav","2.Sınav","3.Sınav"])
plt.pie(degerler,labels=kategoriler)
plt.show()