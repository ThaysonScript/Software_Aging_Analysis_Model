import pandas as pd

def configurar_index_data_frame(data_frame):
    """ CONFIGURAR INDICE DO DATA_FRAME
    
        argumento: data_frame
        
        retorno data frame com indice configurado
    """
    
    # COPIAR DATA FRAME ORIGINAL
    data_frame_index_configurado = data_frame

    # CONVERTER TIPO OBJETO PARA DATETIME64[ns]
    data_frame_index_configurado['datetime'] = pd.to_datetime(data_frame_index_configurado['datetime'])

    # DEFINIR INDICE COMO DATETIME
    data_frame_index_configurado = data_frame_index_configurado.set_index('datetime')

    """ NOVA COLUNA NO DATAFRAME    'time_passed'
        data_frame_index_configurado.index = todos valores do indice datetime
        data_frame_index_configurado.index[0] = primeiro valor do indice datetime
        total_seconds() / 3600 = converta tempo para segundos e divida pelos segundos totais que contem 1 hora
    """
    data_frame_index_configurado['time_passed'] = (data_frame_index_configurado.index -
                                                   data_frame_index_configurado.index[0]).total_seconds() / 3600

    # FACA NOVA COLUNA SE TORNAR O NOVO INDICE DO DATA_FRAME = TEMPO PASSADO TOTAL DE REGISTRO DE DADOS
    data_frame_index_configurado = data_frame_index_configurado.set_index('time_passed')

    return data_frame_index_configurado # RETORNE O NOVO DATA_FRAME
