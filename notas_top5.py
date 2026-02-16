import pandas as pd

df = pd.read_csv("notas.csv")
df_ordenado = df.sort_values("valor", ascending=False)
print(df_ordenado.head(5))
