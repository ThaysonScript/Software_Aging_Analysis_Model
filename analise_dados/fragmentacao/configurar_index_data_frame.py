import pandas as pd


def configurar_index_data_frame(data_frame):
    data_frame_index_configurado = data_frame

    data_frame_index_configurado['datetime'] = pd.to_datetime(data_frame_index_configurado['datetime'])

    data_frame_index_configurado = data_frame_index_configurado.set_index('datetime')

    data_frame_index_configurado['time_passed'] = (data_frame_index_configurado.index -
                                                   data_frame_index_configurado.index[0]).total_seconds() / 3600

    data_frame_index_configurado = data_frame_index_configurado.set_index('time_passed')

    return data_frame_index_configurado
