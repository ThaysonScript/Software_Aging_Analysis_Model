import pandas as pd


def ler_csv(caminho_arquivo):
    """
    Read CSV file and return DataFrame.
    """
    try:
        return pd.read_csv(caminho_arquivo, delimiter=";", header=0)

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as e:
        print("An error occurred:", str(e))
        return None
