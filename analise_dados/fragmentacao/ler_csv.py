import pandas as pd


def ler_csv(caminho_arquivo):
    """
    Read CSV file and return DataFrame.
    """
    try:
        return pd.read_csv(caminho_arquivo, delimiter=";", header=0)

    except FileNotFoundError:
        print("Seu arquivo não existe, verifique os caminhos, nome, etc do arquivo a ser analisado")
        return None

    except Exception as e:
        print("Um erro foi ocorrido em:", str(e))
        return None
