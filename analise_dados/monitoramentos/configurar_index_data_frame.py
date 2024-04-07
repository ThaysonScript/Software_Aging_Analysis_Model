import pandas as pd

def configurar_index_data_frame(data_frame):  
  try:
      data_frame['date_time'] = pd.to_datetime(data_frame['date_time'], format='%d-%m-%Y-%H:%M:%S')
      
  except ValueError as e:
      # Imprima o erro e o valor problemático que está causando o erro
      print("Erro:", e)
      valor_problematico = data_frame.loc[data_frame['date_time'].str.match(r'\d{2}-\d{2}-\d{4}-\d{2}:\d{2}:\d{2}') == False, 'date_time'].iloc[0]
      print("Valor problemático:", valor_problematico)
      return data_frame
      
  # data_frame['date_time'] = pd.to_datetime(data_frame['date_time'], format='%d-%m-%Y-%H:%M:%S')
  data_frame_formatado_index = data_frame.set_index(data_frame['date_time'])

  data_frame_formatado_index['tempo_passado'] = data_frame_formatado_index['date_time'].dt.strftime('%H:%M:%S')
  data_frame_formatado_index['tempo_passado'] = abs(data_frame_formatado_index.index - data_frame_formatado_index.index[0]).total_seconds() / 3600

  data_frame_formatado_index = data_frame_formatado_index.set_index('tempo_passado')

  return data_frame_formatado_index