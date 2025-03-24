import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Carregar o dataset
df = pd.read_csv("car_prices.csv")
print(df.info())
print(df.shape) 
print(df.columns)
print(df.isnull().sum())
print(df.describe())
print(df["make"].value_counts().to_string())
suv = df[df["body"] == "SUV"]
print(suv)
antigos = df[df["sellingprice"] > 150000]
print(antigos)
df_filtrado = df[df["sellingprice"] > 150000][["make","sellingprice"]]
print(df_filtrado)
df["kilometragem KM"] = df["odometer"] / 0.6214
print(df)
df["transmission"] = df["transmission"].fillna(df["transmission"].mode()[0])
df_sorted = df.sort_values(by="year", ascending=False)
print(df_sorted)
df.fillna(df.mode().iloc[0], inplace=True)
media_precos = df.groupby("make")["sellingprice"].mean()
print(media_precos.to_string())
marcas = df.groupby("make").size()
marcas_ordem = marcas.sort_values(ascending=False)
print(marcas_ordem.to_string())
