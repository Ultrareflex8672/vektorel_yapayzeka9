# Normal vs Binomial distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal') # loc=ortalama, scale=standart sapma
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial') # n=deneme sayısı, p=başarı olasılığı

plt.legend() # etiketleri gösterir
plt.show() # grafiği gösterir