import pandas as pd

# Carregar o dataset
df = pd.read_csv("penguins_size.csv")


# Mostrar informações sobre o dataset
print(df.info())
print(df.shape)  # Retorna (linhas, colunas)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.describe())
print(df["species"].value_counts())
print(df.groupby("species")["body_mass_g"].mean())
adelie = df[df["species"] == "Adelie"]
print(adelie.head())
pesados = df[df["body_mass_g"] > 4000]
pd.set_option("display.max_rows", None)  # Permite mostrar todas as linhas
print(pesados)
df_filtrado = df[["species", "body_mass_g"]]
print(df_filtrado)
