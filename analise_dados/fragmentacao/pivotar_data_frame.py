def pivotar_data_frame(data_frame):
    data_frame_pivotado = data_frame

    data_frame_pivotado = data_frame_pivotado.pivot(columns='process', values='process_occurrences')

    print(f'tabela pivotada: {data_frame_pivotado}')

    data_frame_pivotado = data_frame_pivotado.dropna()

    return data_frame_pivotado