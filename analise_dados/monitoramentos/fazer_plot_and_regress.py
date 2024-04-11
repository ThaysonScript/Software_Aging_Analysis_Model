import os
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels.api as sm
from analise_dados.adicionar_statistica_regressao import adicionar_statistica_regressao

def fazer_plot_regressao(data_frame, nome_arquivo, diretorio_plots):  
  incluirColunaY = True
  tipoYlabel = '(Porcentagem)'
  title = 'Monitoramento de Recursos da CPU'

  for col in data_frame.columns:
    if type(tipoYlabel) is str and incluirColunaY is True:
      parte_coluna_df = f"{col} {tipoYlabel}"

    else:
      parte_coluna_df = f"{tipoYlabel}"

    if col != 'date_time':
      x = data_frame.index.values.reshape(-1, 1)
      y = data_frame[col].fillna(0)

      model = LinearRegression().fit(x, y)

      Y_pred = model.predict(x)

      if type(tipoYlabel) is str:
        ylabel = parte_coluna_df

      elif type(tipoYlabel) is dict and col in tipoYlabel:
        ylabel = ylabel[col]

      else:
        ylabel = col


      if type(title) is str:
        title = title

      elif type(title) is dict and col in title:
        title = title[col]

      else:
        title = col

      ax = data_frame.plot(
          title=title,
          figsize=(10, 5),
          legend=0,
          y=col,
          xlabel='Time(H)',
          ylabel=ylabel,
          style='k'
      )
      
      # Adicionar a linha da regressão
      ax.plot(x, Y_pred, color='red')
      
      if os.path.exists(f'{diretorio_plots}/{nome_arquivo}/'):
        pass
    
      else:
          os.makedirs(f'{diretorio_plots}/{nome_arquivo}/')
      
      plt.savefig(f'{diretorio_plots}/{nome_arquivo}/{nome_arquivo}_{col}.png')
      
      plt.close()
      
      # plt.show()
      
      
      adicionar_statistica_regressao(
        modelo=model, 
        x=x, y=y, 
        nome_arquivo=nome_arquivo,
        col=col,
        diretorio_plots=diretorio_plots
      )