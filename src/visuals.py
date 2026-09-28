import matplotlib.pyplot as plt
from matplotlib import ticker
import pandas as pd
from matplotlib.lines import Line2D

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

COLOR = '#2E5C8A'
PALETTE = ['#2E5C8A', '#5B9BD5', '#8FBF7F', '#E8A33D', '#D9635E',
           '#9B7FC7', '#5FA8A0', '#C97BB0', '#7A9E5E', '#C4A05B']

def grafico_silhouette(results):
    plt.figure(figsize=(10, 6))
    plt.plot(results["k"], results["silhouette score"], marker='o')
    plt.title("Silhouette Score vs Numero de clusters (K)")
    plt.xlabel("Numero de Clusters (K)")
    plt.ylabel("silhouette score")
    plt.xticks(results["k"])
    plt.grid()
    plt.savefig("src/charts/silhouette_score.png", dpi=150)
    plt.show()

# Grafico canal por faixa etaria

def grafico_canais_idade(df):
    fig, ax = plt.subplots(figsize=(8, 5.5))
    ct = pd.crosstab(df["Faixa Etaria"], df["Canal"])
    ct = ct.reindex(["Jovem", "Adulto", "Idoso"])
    ct.plot(kind="bar", stacked= False, ax=ax, color= PALETTE[:3])
    ax.set_title("Canal de Compra Preferido por Faixa Etária", fontsize= 14, fontweight="bold", pad= 12)
    ax.set_xlabel("Faixa Etária")
    ax.set_ylabel("Número de Compras")
    plt.xticks(rotation= 0)
    ax.legend(title = "Canal")
    plt.tight_layout()
    plt.savefig("src/charts/canal_faixa_etaria.png", dpi= 150)
    plt.close()

# Grafico volume de compras por regiao

def grafico_volume_regiao(df):
    fig, ax = plt.subplots(figsize=(9, 5.5))
    estados = df["Estado"].value_counts().sort_values(ascending=False)
    ax.bar(estados.index, estados.values, color= COLOR)
    ax.set_title("Volume de compras por região", fontsize= 14, fontweight="bold", pad= 12)
    ax.set_xlabel('Estado (UF)')
    ax.set_ylabel('Volume de compras')
    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.xticks(rotation= 45, ha='right')
    plt.tight_layout()
    plt.savefig("src/charts/volume_por_estado.png", dpi= 150)
    plt.close()

# Grafico distribuicao por categoria de produto

def grafico_distribuicao_categoria(df):
    fig, ax = plt.subplots(figsize=(9, 5.5))
    cat_counts = df["Categoria Produto"].value_counts()
    ax.pie(cat_counts.values, labels=cat_counts.index, autopct='%1.0f%%', colors= PALETTE,
           startangle=90, pctdistance=0.8, wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})
    ax.set_title("Distribuição de Compras por Categoria de Produto", fontsize= 14, fontweight="bold", pad= 12)
    plt.tight_layout()
    plt.savefig("src/charts/distribuicao_categoria.png", dpi= 150)
    plt.close()

# Grafico Compras por Turno do Dia

def grafico_compras_por_turno(df):
    fig, ax = plt.subplots(figsize=(9, 5.5))
    turno_counts = df["Turno"].value_counts().reindex(["Manhã", "Tarde", "Noite"])
    ax.bar(turno_counts.index, turno_counts.values, color= ['#E8A33D', '#5B9BD5', '#2E5C8A'])
    ax.set_title("Distribuição de Compras por Turno do Dia", fontsize= 14, fontweight="bold", pad= 12)
    ax.set_xlabel("Turno")
    ax.set_ylabel("Número de Compras")
    plt.tight_layout()
    plt.savefig("src/charts/compras_por_turno.png", dpi= 150)
    plt.close()

# Grafico dispersao de idade por valor da compra

def grafico_dispersao_idade_valor(df):
    fig, ax = plt.subplots(figsize=(9, 5.5))
    color_gender = df["Gênero"].map({"M": "#2E5C8A", "F": "#D9635E"})
    ax.scatter(df["Idade"], df["Valor (R$)"], c=color_gender, alpha=0.6, s = 50, edgecolors='w', linewidth=0.5)
    ax.set_title("Dispersão de Idade por Valor da Compra", fontsize= 14, fontweight="bold", pad= 12)
    ax.set_xlabel("Idade")
    ax.set_ylabel("Valor da Compra (R$)")
    legend_elems = [Line2D([0], [0], marker='o', color='w', label='Masculino', markerfacecolor='#2E5C8A', markersize=10),
                    Line2D([0], [0], marker='o', color='w', label='Feminino', markerfacecolor='#D9635E', markersize=10)]
    ax.legend(handles=legend_elems, title="Gênero")
    plt.tight_layout()
    plt.savefig("src/charts/dispersao_idade_valor.png", dpi= 150)
    plt.close()