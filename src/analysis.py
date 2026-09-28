import pandas as pd

def analise (data):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame.")

    analysis_results = {
        "Valores nulos": data.isnull().sum().to_dict(),
        "Valores duplicados": data.duplicated().sum(),
        "Tipos de dados": data.dtypes.to_dict(),
        "Estatísticas descritivas": data.describe().to_dict()
    }
    return analysis_results

def analise_clusters(df):
    perfil = df.groupby("Cluster").agg(
       Clientes = ("Cliente", "count"),
       Idade_media = ("Idade", "mean"),
       Valor_medio = ("Valor (R$)", "mean")
    )
    return perfil

def analise_categorias(df):
    categorias = (
        df.groupby("Cluster")["Categoria Produto"]
        .value_counts()
        .groupby(level=0, group_keys=False)
        .head(1)
    )
    return categorias

def analise_canais(df):
    canais = (
        df.groupby("Cluster")["Canal"]
        .value_counts()
        .groupby(level=0, group_keys=False)
        .head(1)
    )
    return canais

def faixa_etaria(df):
        bins = [0, 29, 50, 150]
        labels = ["Jovem", "Adulto", "Idoso"]
        df["Faixa Etaria"] = pd.cut(df["Idade"], bins=bins, labels=labels, right=False)
        return df

def turno (hora_str):
    h = int(hora_str.split(":")[0])
    if 6 <= h < 12:
        return "Manhã"
    elif 12 <= h < 18:
        return "Tarde"
    else:
        return "Noite"


# Reconhecimento de padroes

def padroes(df):
    print("\n Categoria por Genero")
    print(pd.crosstab(df["Categoria Produto"], df["Gênero"]))

    print("\n Categoria mais comprada")
    print(df["Categoria Produto"].value_counts())

    print("\n Canal por Turno")
    print(pd.crosstab(df["Turno"], df["Canal"]))

    print("\n Valor medio por Genero")
    print(df.groupby("Gênero")["Valor (R$)"].agg(["count", "mean", "sum"]))

    print("\n Valor medio por Categoria")
    print(df.groupby("Categoria Produto")["Valor (R$)"].agg(["count", "mean"]).sort_values(by="mean", ascending=False))
