from src.load_data import load_data
from src.analysis import (analise, analise_clusters, analise_categorias, analise_canais, faixa_etaria, turno, padroes)
from src.kmeans import prepare_model, find_best_k, apply_kmeans
from src.visuals import (grafico_silhouette, grafico_canais_idade, grafico_volume_regiao, grafico_distribuicao_categoria, grafico_compras_por_turno, grafico_dispersao_idade_valor)

def main():
# Carregando os dados
    df_raw = load_data("./data/retail_max.csv")

    analise_df = analise(df_raw)

    for titulo, conteudo in analise_df.items():
        print(f"\n{titulo}:")

    from pprint import pprint

    pprint(conteudo, sort_dicts=False)

    df_raw = faixa_etaria(df_raw)
    df_raw["Turno"] = df_raw["Hora Compra"].apply(turno)

# Preparando os dados para o modelo KMeans
    data_scaled, feature_names = prepare_model(df_raw)
    resultado_k = find_best_k(data_scaled)
    best_k = int(resultado_k.loc[resultado_k["silhouette score"].idxmax(), "k"])
    df_clustered, modelo = apply_kmeans(df_raw, data_scaled, best_k)

    perfil_clusters = analise_clusters(df_clustered)
    categorias_top = analise_categorias(df_clustered)
    canais_top = analise_canais(df_clustered)

    print(perfil_clusters)
    print(categorias_top)
    print(canais_top)

# Reconhecimento de padroes
    print("\n Padrões encontrados:")

    padroes(df_clustered)


# Graficos
    grafico_silhouette(resultado_k)
    grafico_canais_idade(df_clustered)
    grafico_volume_regiao(df_clustered)
    grafico_distribuicao_categoria(df_clustered)
    grafico_compras_por_turno(df_clustered)
    grafico_dispersao_idade_valor(df_clustered)

if __name__ == '__main__':
    main()