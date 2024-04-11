import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from analise_dados.adicionar_statistica_regressao import adicionar_statistica_regressao

def fazer_plotagem(data_frame_pivotado, diretorio_plots):    
    # Plotar os dados de ocorrência do processo em relação ao tempo para cada processo
    plt.figure(figsize=(10, 5))

    # Iterar sobre as colunas de data_frame_pivotado
    for column in data_frame_pivotado.columns:
        # Obter os dados de ocorrência do processo e tempo para o processo atual
        Y_process = data_frame_pivotado[column].values
        X = data_frame_pivotado.index.values.reshape(-1, 1)
        Y = Y_process

        # Ajustar o modelo de regressão linear
        regression_model = LinearRegression().fit(X, Y)

        # Plotar os pontos de dados das ocorrências do processo em relação ao tempo para o processo atual
        plt.scatter(X, Y, label=f'{column}', alpha=0.5)

        # Plotar a linha de regressão para o processo atual
        plt.plot(X, regression_model.predict(X), label=f'Linha de Regressão - {column}')

    # Adicionar rótulos e título ao gráfico
    plt.xlabel('Tempo (H)')
    plt.ylabel('Ocorrências do Processo')
    plt.title('Ocorrências do Processo em relação ao Tempo com Linha de Regressão para cada Processo')
    plt.legend()
    
    if os.path.exists(f'{diretorio_plots}/fragmentacao'):
        pass
    
    else:
        os.makedirs(f'{diretorio_plots}/fragmentacao/')

    # Salvar a figura como uma imagem
    plt.savefig(f'{diretorio_plots}/fragmentacao/fragmentation.png')
    plt.close()



    # adicionar_statistica_regressao(
    #     modelo=regression_model,
    #     x=X, y=Y,
    #     nome_arquivo='',
    #     diretorio_plots=diretorio_plots
    # )