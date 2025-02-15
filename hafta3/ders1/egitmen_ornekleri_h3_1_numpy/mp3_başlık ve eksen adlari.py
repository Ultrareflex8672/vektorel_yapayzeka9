import matplotlib.pyplot as plt

plt.title('Öğrencilerin sınav başarıları')
# X ve Y eksenlerine etiketler ekleme
plt.xlabel('Sınavlar')
plt.ylabel('Puanlar')

plt.bar(["1.Sınav","2.Sınav","3.Sınav"], [80,70,90])
plt.show()
