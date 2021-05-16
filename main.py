import numpy as np
import pandas as pd
from matplotlib import pyplot as plt



#Zad1
'''uro = [219, 400, 360, 295, 320, 357]
rok = [2015, 2016, 2017, 2018, 2019, 2020]

s = pd.Series(uro, rok)
df = pd.DataFrame(s)

print(df)
df.plot()
plt.title("Wykres urodzeń w poszczególnych latach")
plt.xlabel("rok")
plt.ylabel("urodzeń")
plt.legend()
plt.show()'''

#Zad2
'''
dzieci = {'Płeć': ['Chłopcy', 'Dziewczynki', 'Chłopcy', 'Dziewczynki'],
          'Populacja': [560, 490, 362, 413]}
df = pd.DataFrame(dzieci)
print(df)
grupa = df.groupby(['Płeć']).agg({'Populacja': ['sum']})
wykres = grupa.plot.bar()
wykres.set_xlabel('Płeć')
wykres.set_ylabel('Urodzeń')
plt.legend()
plt.title('Wykres słupkowy urodzeń z podziałem na płeć')
plt.xticks(rotation = 0)
plt.show()
'''
#Zad3
'''
data = {'Płeć': ['Chłopiec', 'Dziewczynka', 'Chłopiec', 'Chłopiec', 'Dziewczynka', 'Dziewczynka', 'Chłopiec', 'Dziewczynka', 'Dziewczynka', 'Chłopiec'],
        'Urodzeń': [322, 422, 345, 374, 358, 386, 364, 381, 363, 367],
        'Rok': [2016, 2016, 2017, 2017, 2018, 2018, 2019, 2019, 2020, 2020]}

df = pd.DataFrame(data)
print(df)
grupa = df.groupby(['Płeć']).agg({'Urodzeń':['sum']})
wykres = grupa.plot.pie(subplots=True, autopct='%.2f%%', fontsize=20, figsize=(6, 6), legend=(0, 0))
plt.show()
'''

#Zad4
'''
df = pd.read_csv('dane.csv', header = 0, sep = ';', decimal = '.')
print(df)
grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia':['count']})
wykres = grupa.plot.bar()
plt.legend()
plt.xticks(rotation=0)
wykres.set_ylabel('Ilość zamówień')
plt.show()
'''
