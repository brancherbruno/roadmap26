import pandas as pd

def filter_employee_25_30_by_gender(path: str):
    df = pd.read_csv(path)
    df["ordem_sexo"] = df["sexo"].map({"F": 0, "M": 1})
    filtro_idade = (df["idade"] >= 25) & (df["idade"] <= 40)
    df_filtrado = df.loc[filtro_idade]
    df_ordenado = df_filtrado.sort_values(["ordem_sexo", "idade"],ascending=[True, True])
    return df_ordenado

if __name__ == "__main__":
    df_filtered = filter_employee_25_30_by_gender("funcionarios.csv")
    print(df_filtered.head(15))


def sort_employee_by_gender_age(path: str):
    df = pd.read_csv(path)
    df["ordem_sexo"] = df["sexo"].map({"F": 0, "M": 1})
    df_ordenado = df.sort_values(["ordem_sexo", "idade"], ascending=[True, True])
    return df_ordenado
if __name__ == "__main__":
    df_sorted = sort_employee_by_gender_age("funcionarios.csv")
    print(df_sorted.head(15))
