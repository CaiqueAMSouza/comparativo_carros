import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import openpyxl

df = pd.read_csv("car_prices.csv") #codigo para ler o arquivo importado

df.info() # codigo mostrando cada coluna e o tipo da variavel

print(df.shape) # mostra quantidade de linhas e colunas

print(df.columns) # nome de cada coluna

print(df.isnull().sum()) #quantidade de termos nulos  em cada coluna

print(df.describe()) #uma media geral do arquivo

df_teste=df

df_teste["saledate"] = pd.to_datetime(df_teste["saledate"], errors="coerce", utc=True) # linhas de codigo para mudar a formatação das datas

df_teste["saledate"] = df_teste["saledate"].dt.strftime("%d/%m/%Y") 

df_teste.info() #antes de retirar os termos nulos:558837 entradas

df_teste=df_teste.dropna() # linhas para retirar os temos nulos/nan

df_teste.info()#depois de retirar os termos nulos:472325 entradas

vendas_datas=df_teste.groupby(["saledate", "make"])["make"].size() # linhas para mostrar a data de venda e quantos/quais carros foram vendidos naquela data

print(vendas_datas)

df_teste["saledate"] = pd.to_datetime(df_teste["saledate"], errors="coerce", utc=True) # linhas para mostrar a data de venda e quantos/quais carros foram vendidos naquela data

vendas_datas = df_teste.groupby([df_teste["saledate"].dt.date, "make"]).size().reset_index(name="quantidade_vendas")

vendas_datas = vendas_datas.sort_values(by="saledate")

(vendas_datas)

make_df=df["make"].value_counts().to_string() #aqui mostra a fabricante e a quantidade de carros feitos respectivamente

print(make_df)

make_counts = df["make"].value_counts() #grafico para mostra a fabricante e a quantidade de carros feitos respectivamente

plt.figure(figsize=(19, 7))
make_counts.plot(kind="bar", color="royalblue")

plt.title("Quantidade de Carros Vendidos por Fabricante", fontsize=14)
plt.xlabel("Fabricante", fontsize=12)
plt.ylabel("Quantidade de Carros", fontsize=12)
plt.xticks(rotation=90)  

plt.show()

suv = df[df["body"] == "SUV"] #aqui é uma tabela mostrando todos os SUV da lista 
suv=suv.dropna()
(suv)

luxo = df[df["sellingprice"] > 150000] # mostra os carros que foram vendidos por mais de 150mil
luxo=luxo.dropna()
(luxo)

df_filtrado = df[df["sellingprice"] > 150000][["make","sellingprice"]] #codigo para mostras de forma detalhada os carros que foram vendidos por mais de 150mil e sua marca

(df_filtrado)

df["kilometragem KM"] = df["odometer"] / 0.6214 #linha para criar nova coluna chamada Kilometragem KM

df[["kilometragem KM", "odometer", "make"]] 

df["transmission"] = df["transmission"].fillna(df["transmission"].mode()[0]) #linhas para mostrar o ano, marca, modelo e tipo de transmissão

df_sorted = df.sort_values(by="year", ascending=False) # linha para ordenar eles pelo ano do carro
df_sorted=df_sorted.dropna()

df_sorted[["year", "make", "model", "transmission"]]

df.fillna(df.mode().iloc[0], inplace=True) #media geral de preços dos carros de cada marca 

media_precos = df.groupby("make")["sellingprice"].mean()

print(media_precos.to_string())


plt.figure(figsize=(19, 7)) # grafico mostrando a media de preço x marca
media_precos.sort_values(ascending=False).plot(kind="bar", color="royalblue")

# Adicionar título e rótulos
plt.title("Média de Preços dos Carros por Marca", fontsize=14)
plt.xlabel("Marca", fontsize=12)
plt.ylabel("Preço Médio (USD)", fontsize=12)
plt.xticks(rotation=90)  


plt.show()

media_precos_df = media_precos.reset_index() #exportando para o excel os dados do preço medio por marca
media_precos_df.columns = ["Marca", "Preço Médio"]

media_precos_df.to_excel("media_precos_marcas.xlsx", index=False)

marcas = df.groupby("make").size() #linhas para mostrar quantos carros foram vendidos por marca

marcas_ordem = marcas.sort_values(ascending=False)

print(marcas_ordem.to_string())

df["saledate"] = pd.to_datetime(df["saledate"], errors="coerce") #linhas para procurar a quantidade de carros vendidos por estado e por periodo de data

inicio = pd.Timestamp("2014-01-01")
fim = pd.Timestamp("2015-07-25")

df["state"] = df["state"].str.strip().str.upper()

estado_desejado = "PA" 
df_modific = df[(df["saledate"] >= inicio) & 
                (df["saledate"] < fim) & 
                (df["state"] == estado_desejado)]

tempo_estado = df_modific.groupby("saledate").size()

pd.set_option("display.max_rows", None)

pd.set_option("display.max_columns", None) 

pd.set_option("display.expand_frame_repr", False) 

print(tempo_estado)


plt.figure(figsize=(12, 6))
plt.plot(tempo_estado.index, tempo_estado.values, marker="o", linestyle="-", color="b")
plt.xlabel("Data de Venda")
plt.ylabel("Quantidade de Carros Vendidos")
plt.title(f"Vendas de Carros no Estado {estado_desejado} ({inicio.date()} a {fim.date()})")
plt.xticks(rotation=45)
plt.grid(True)

# Mostrar o gráfico
plt.show()

tempo_estado_df = tempo_estado.reset_index(name='Quantidade de Carros Vendidos') #exportando para o excel os dados do venda de carros por mes em estado XX
tempo_estado_df.columns = ["saledate","quantidade ce carros vendidos"]
tempo_estado_df.to_excel("venda de carros do estado XX.xlsx", index=False)

df["year_month"] = df["saledate"].dt.to_period("M")

vendas_por_mes = df.groupby("year_month").size()
vendas_por_marca = df.groupby(["year_month", "make"]).size()
faturamento_mensal = df.groupby("year_month")["sellingprice"].sum()


vendas_por_mes = df.groupby("year_month").size()

marca_mais_vendida = vendas_por_marca.groupby(level=0).idxmax()
quantidade_mais_vendida = vendas_por_marca.groupby(level=0).max()
media_vendas = vendas_por_marca.groupby(level=0).mean()

resultado = pd.DataFrame({
    "Faturamento Mensal": faturamento_mensal,
    "Vendas Totais": vendas_por_mes,
    "Média de Vendas": media_vendas,
    "Marca Mais Vendida": [m[1] for m in marca_mais_vendida],
    "Quantidade Marca Mais Vendida": quantidade_mais_vendida
})

print(resultado)


fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(resultado.index.astype(str), resultado["Vendas Totais"], color="skyblue", label="Vendas Totais")

for i, txt in enumerate(resultado["Marca Mais Vendida"]):
    ax.text(i, resultado["Vendas Totais"].iloc[i] + 50, txt, ha="center", fontsize=10, color="red")

plt.xticks(rotation=45)
plt.xlabel("Ano-Mês")
plt.ylabel("Quantidade de Vendas")
plt.title("Vendas de Carros por Mês e Marca Mais Vendida")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()

vendas_por_mes = vendas_por_mes.reset_index()
vendas_por_mes = vendas_por_mes.rename(columns={'index': 'Mes', 'saledate': 'Quantidade de Carros Vendidos'})

df.to_excel("dados_completos_carros.xlsx", index=False, engine='openpyxl')


resultado_df = resultado.reset_index() #exportando para o excel os dados do preço medio por marca
resultado_df.columns = ["year_month", "Faturamento Mensal","Vendas Totais","Média de Vendas","Marca Mais Vendida","Quantidade Marca Mais Vendida"]

resultado_df.to_excel("resultado.xlsx", index=False)