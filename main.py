import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

uro = [219, 400, 360, 295, 320, 357]
rok = [2015, 2016, 2017, 2018, 2019, 2020]

s = pd.Series(uro, rok)


df = pd.DataFrame(s)
df['Urodzeń'] = df.rolling(window=100).mean()
df.plot()
plt.show()

#Zad1



