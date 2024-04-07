from analise_dados.monitoramentos.fazer_plot_and_regress import fazer_plot_regressao


def formatar_tipo_coluna_data_frame(data_frame, nome_arquivo, diretorio_plots):
  data_frame_coluna_formatado_tipo = data_frame

  for coluna in data_frame.columns:
    if coluna != 'date_time' and coluna != 'tempo_passado' and data_frame_coluna_formatado_tipo[coluna].dtype == 'object':
      data_frame_coluna_formatado_tipo[coluna] = data_frame_coluna_formatado_tipo[coluna].str.replace(",", ".").astype(float)

  fazer_plot_regressao(data_frame_coluna_formatado_tipo, nome_arquivo, diretorio_plots)

  return data_frame_coluna_formatado_tipo