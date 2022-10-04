import pandas as pd

df=pd.read_csv("/BS.csv")

df.head(5)

df=df.dropna()

price=df['Price']

import matplotlib.pyplot as plt

plt.hist(price)

print(df['Price'].mean())
print(df['Price'].median())
print(df['Price'].mode())
print(df['Price'].std())

print(subrub_count)

rooms_type=df['Type'].value_counts()
rooms_type=dict(rooms_type)

print(rooms_type)

t=rooms_type.keys()

print(t)

c=rooms_type.values()

print(c)

plt.bar(x=t,height=c)
plt.title("Room type")
plt.show()

print(df['SellerG'].unique())

from IPython.core.pylabtools import figsize
fig=plt.figure(figsize=(10,10))
plt.pie(x=c, labels=t, explode=[0.0,0.2,0.0])
plt.legend()
plt.title("House type")
plt.show()

from pandas.core.algorithms import value_counts
dist=(df['Distance'].value_counts())
dist=dict(dist)
print(dist)

dist=df['Distance']

price=df['Price']

plt.plot(dist,price)
plt.title("Distance Vs Price")
plt.xlabel('Distance')
plt.ylabel('Price')
plt.show()



plt.scatter(dist,price)
plt.title("Distance Vs Price")
plt.xlabel('Distance')
plt.ylabel('Price')
plt.show()
