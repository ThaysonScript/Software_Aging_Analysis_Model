import os
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm


def configurar_regressao(data_frame, diretorio_plots):
    """ CONFIGURAR A LINHA DE REGRESSAO DOS DADOS A SEREM MONITORADOS
        
        Argumentos:
            data_frame: DataFrame contendo os dados a serem analisados
    """
    
    # Extração das variáveis independentes (TEMPO PASSADO) e dependentes (VALOR DEPENDENTE)
    X = data_frame.index.values.reshape(-1, 1)  # TEMPO PASSADO
    Y = data_frame.iloc[:, 0].values            # VALOR DEPENDENTE

    # Imprimindo os valores de X e Y (apenas para verificação)
    print(f'X: {X}')
    print(f'Y: {Y}')

    # Construindo o modelo de regressão linear com a biblioteca scikit-learn
    regression_model = LinearRegression().fit(X, Y)

    # Calculando o coeficiente de determinação (R-squared) para avaliar o ajuste do modelo
    r_squared = regression_model.score(X, Y)

    # Adicionando uma constante ao conjunto de variáveis independentes para a análise com statsmodels
    x_with_const = sm.add_constant(X)

    # Criando e ajustando o modelo de regressão linear com statsmodels
    regression_model_sm = sm.OLS(Y, x_with_const).fit()

    # Obtendo um resumo estatístico do modelo ajustado
    regression_summary = regression_model_sm.summary()

    # Imprimindo o resumo estatístico (incluindo coeficientes, erro padrão, valor p, etc.)
    print(regression_summary)
    
    file_directory = f'{diretorio_plots}/fragmentacao'
    file_path = f'{file_directory}/resumo_estatistico_regressao_fragmentacao.txt'
        
    # Verificar se o diretório existe, se não, criar
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)

    # Criar o arquivo vazio
    with open(file_path, 'w') as f:
        f.write(regression_summary.as_text())
