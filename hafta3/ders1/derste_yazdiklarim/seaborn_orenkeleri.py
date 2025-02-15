import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5]) # Histogramı çizer

plt.show()


sns.distplot([0, 1, 2, 3, 4, 5], hist=False) # Histogramı kaldırır

plt.show()
