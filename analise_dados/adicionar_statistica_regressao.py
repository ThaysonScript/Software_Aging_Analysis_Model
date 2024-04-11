import os
import statsmodels.api as sm


def adicionar_statistica_regressao(modelo, x, y, nome_arquivo='', col='', diretorio_plots='erro_diretorio'):

    # Calculando o coeficiente de determinação (R-squared) para avaliar o ajuste do modelo
    r_squared = modelo.score(x, y)

    # Adicionando uma constante ao conjunto de variáveis independentes para a análise com statsmodels
    x_with_const = sm.add_constant(x)

    # Criando e ajustando o modelo de regressão linear com statsmodels
    modelo_sm = sm.OLS(y, x_with_const).fit()

    # Obtendo um resumo estatístico do modelo ajustado
    regression_summary = modelo_sm.summary()

    # Imprimindo o resumo estatístico (incluindo coeficientes, erro padrão, valor p, etc.)
    print(regression_summary)
    
    
    if col != '':
        file_directory = f'{diretorio_plots}/{nome_arquivo}/'
        file_path = f'{diretorio_plots}/{nome_arquivo}/{nome_arquivo}_{col}.txt'
        
    else:
        file_directory = f'{diretorio_plots}/fragmentacao'
        file_path = f'{file_directory}/resumo_estatistico_regressao_fragmentacao.txt'
        
    # Verificar se o diretório existe, se não, criar
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)

    # Criar o arquivo vazio
    with open(file_path, 'w') as f:
        f.write(regression_summary.as_text())
