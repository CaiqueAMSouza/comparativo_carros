import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o dataset
df = pd.read_csv("penguins_size.csv")


adelie = df[df["species"] == "Adelie"]
print(adelie.head())
pesados = df[df["body_mass_g"] > 4000]
pd.set_option("display.max_rows", None)  # Permite mostrar todas as linhas
print(pesados)
df_filtrado = df[["species", "body_mass_g"]]
print(df_filtrado)
df["massa_kg"] = df["body_mass_g"] / 1000
df["massa_kg"] = df["body_mass_g"] / 1000
print(df)
df["sex"] = df["sex"].fillna(df["sex"].mode().iloc[0])
df.dropna(inplace=True)
df["sex"] = df["sex"].replace({".": df["sex"].mode().iloc[0]})
df_sorted = df.sort_values(by="flipper_length_mm", ascending=False)
print(df_sorted)
print(df.groupby("island")["body_mass_g"].mean())
print(df.groupby("sex").size())
plt.figure(figsize=(8, 5))
sns.boxplot(x="culmen_length_mm", y="culmen_depth_mm", data=df)
plt.title("Relação entre Espécie e Tamanho da Nadadeira")
plt.show()