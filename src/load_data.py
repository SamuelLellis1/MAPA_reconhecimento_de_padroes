import pandas as pd
import glob

def load_data(file_path = "./data/retail_max.csv"):
    file_paths = glob.glob(file_path)
    if not file_paths:
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    lista_dataframes = [pd.read_csv(file) for file in file_paths]
    return pd.concat(lista_dataframes, ignore_index=True)