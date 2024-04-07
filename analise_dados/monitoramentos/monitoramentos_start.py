from analise_dados.monitoramentos.carregar_data_frame import carregar_data_frame
from analise_dados.monitoramentos.configurar_index_data_frame import configurar_index_data_frame
from analise_dados.monitoramentos.formatar_tipo_coluna_data_frame import formatar_tipo_coluna_data_frame
from analise_dados.caminho_logs import logs_gerais, logs_vbox, logs_kvm, logs_xen, logs_lxc

def tipo_log(qual_log):
    if qual_log == 'vbox':
        return logs_vbox
    
    elif qual_log == 'kvm':
        return logs_kvm
    
    elif qual_log == 'xen':
        return logs_xen
    
    else:
        return logs_lxc


def monitoramentos_start(diretorio_plots):
    logs_tipo = tipo_log('kvm')
    
    for nome_arquivo, caminho_arquivo in logs_gerais.items():        
        novo_data_frame = carregar_data_frame(caminho_arquivo)

        if novo_data_frame.empty:
            pass
        
        else:
            novo_data_frame = configurar_index_data_frame(novo_data_frame)
            novo_data_frame = formatar_tipo_coluna_data_frame(novo_data_frame, nome_arquivo, diretorio_plots)
        
    for nome_arquivo, caminho_arquivo in logs_tipo.items():        
        novo_data_frame = carregar_data_frame(caminho_arquivo)
        
        if novo_data_frame.empty:
            pass
        
        else:
            novo_data_frame = configurar_index_data_frame(novo_data_frame)
            novo_data_frame = formatar_tipo_coluna_data_frame(novo_data_frame, nome_arquivo, diretorio_plots)