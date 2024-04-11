from analise_dados.fragmentacao.ler_csv import ler_csv
from analise_dados.fragmentacao.configurar_index_data_frame import configurar_index_data_frame
from analise_dados.fragmentacao.fazer_plotagem import fazer_plotagem
from analise_dados.fragmentacao.filtrar_data_frame import filtrar_data_frame
from analise_dados.fragmentacao.pivotar_data_frame import pivotar_data_frame
from analise_dados.caminho_logs import logs_fragmentacao


def fragmentacao_start(diretorio_plots):
    novo_data_frame = ler_csv(logs_fragmentacao['fragmentation'])

    novo_data_frame = configurar_index_data_frame(novo_data_frame)

    novo_data_frame = filtrar_data_frame(novo_data_frame)

    data_frame_pivotado = pivotar_data_frame(novo_data_frame)
    
    data_frame_pivotado = fazer_plotagem(data_frame_pivotado, diretorio_plots)
    