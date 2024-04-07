def filtrar_data_frame(data_frame):
    data_frame_filtrado = data_frame

    data_frame_filtrado = data_frame_filtrado[data_frame_filtrado['process_occurrences'] >= 4]

    print(f'tabela filtrada: {data_frame_filtrado}')

    return data_frame_filtrado