import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


# Preparando os dados

pd.set_option('display.width', 150)
pd.set_option('display.max_columns', 20)

df = pd.read_csv(r'C:\Users\samue\PycharmProjects\RetailMax\data\retail_max.csv')

def prepare_model(df):
    data = df[["Idade", "Valor (R$)","Gênero", "Canal"]].copy()
    data = pd.get_dummies(data, columns=["Gênero", "Canal"], drop_first=True)
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    return data_scaled, data.columns.tolist()

# Encontrando o melhor número de clusters

def find_best_k(data_scaled, k_min = 2, k_max = 10):
    results = []
    for k in range(k_min, k_max + 1):
        kmeans = KMeans(n_clusters=k, random_state=0, n_init= 10)
        clusters = kmeans.fit_predict(data_scaled)
        inertia = kmeans.inertia_
        silhouette = silhouette_score(data_scaled, clusters)
        results.append([k, inertia, silhouette])
    results_df = pd.DataFrame(results, columns = ["k", "inertia", "silhouette score"])
    return results_df

# Aplicando o modelo KMeans com o melhor número de clusters

def apply_kmeans(df, data_scaled, best_k):
    kmeans = KMeans(n_clusters=best_k, random_state=0, n_init= 10)
    df = df.copy()
    df["Cluster"] = kmeans.fit_predict(data_scaled)
    return df, kmeans

# Execucao do fluxo completo

data_scaled, kmeans = prepare_model(df)
print(data_scaled.shape)

resultado_k = find_best_k(data_scaled)
print(resultado_k)

# Grafico elbow + silhouette

fig, axes = plt.subplots(1, 2, figsize=(11, 5))
axes [0].plot(resultado_k["k"], resultado_k["inertia"], marker='o', color = "#2E5C8A")
axes [0].set_title("Metodo do cotovelo (Elbow)", fontweight="bold")
axes [0].set_xlabel("Numero de Clusters (k)")
axes [0].set_ylabel("Inertia")

axes [1].plot(resultado_k["k"], resultado_k["silhouette score"], marker='o', color = "#D9635E")
axes [1].set_title("Silhouette Score por K", fontweight="bold")
axes [1].set_xlabel("Numero de Clusters (k)")
axes [1].set_ylabel("Silhouette Score")

plt.tight_layout()
plt.savefig("src/charts/elbow_silhouette.png", dpi= 150)
plt.close()


