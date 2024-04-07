def filtrar_data_frame(data_frame):
    """ FILTRAR OS DADOS QUE SERAM ANALISADOS EM 4 OCORRENCIAS DO PROCESSO OU MAIS
    
        Argumentos:
            data_frame
            
        Retorno:
            Novo data frame filtrado
    """
    
    data_frame_filtrado = data_frame

    data_frame_filtrado = data_frame_filtrado[data_frame_filtrado['process_occurrences'] >= 4]

    print(f'tabela filtrada: {data_frame_filtrado}')

    return data_frame_filtrado