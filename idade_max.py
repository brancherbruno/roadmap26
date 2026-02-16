import pandas as pd

df = pd.read_csv("funcionarios.csv")
df["ordem_sexo"] = df["sexo"].map({"F": 0, "M": 1})
df_ordenado = df.sort_values(["ordem_sexo", "idade"], ascending=[True, True])

print(df_ordenado)
