import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

metals = pd.read_csv('commodity_futures.csv')

prices_filtrado = metals.fillna(0)

prices_metals = prices_filtrado[['Date', 'COPPER', 'ALUMINIUM', 'ZINC', 'NICKEL', 'GOLD', 'SILVER']]
f = prices_metals.loc[:, prices_metals.columns != "Date"]
df = f.sample(axis='columns')

count = float(df.count())
maxV = float(df.max())
minV = float(df.min())
unique = float(df.nunique())
mean = float(df.mean())
median = float(df.median())
perc75 = float(df.apply(lambda x: np.percentile(x, 75)).reset_index()[0])
perc25 = float(df.apply(lambda x: np.percentile(x, 25)).reset_index()[0])
std = float(df.std())

print(df.info())
print(f'Cantidad de valores: {count}')
print(f'Máximo valor: {maxV}')
print(f'Mínimo valor: {minV}')
print(f'Valores únicos: {unique}')
print(f'Media: {mean}')
print(f'Mediana: {median}')
print(f'75vo percentil: {perc75}')
print(f'25vo percentil: {perc25}')
print(f'Desviación estándar: {std}')

boxplot = df.boxplot(grid=False, rot=45, fontsize=15)
hist = df.hist(bins=3)
plt.tight_layout()
plt.show()
