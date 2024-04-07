from analise_dados.monitoramentos.monitoramentos_start import monitoramentos_start
from analise_dados.fragmentacao.fragmentacao_start import fragmentacao_start
from utils.criar_dir import criar_dir

def main():
    diretorio_plots = criar_dir()
        
    fragmentacao_start(diretorio_plots)
    monitoramentos_start(diretorio_plots)
    
if __name__ == '__main__':
    main()