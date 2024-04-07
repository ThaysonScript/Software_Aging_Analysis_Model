import os

def criar_dir():
    DIRETORIO_PADRAO = './images_plot/'
    DIR_NOME = ''
    
    if os.path.exists(DIRETORIO_PADRAO):
        pass
    
    else:
        os.makedirs('./images_plot')
        
    print('Os logs ficaram em images_plot')
    
    dir_personalizado = str(input('Deseja criar um subdiretorio personalizado? [s/n] -> '))
    if dir_personalizado in ['S', 's']:
        DIR_NOME = str(input('Digite o nome da subpasta: '))
        
    if os.path.exists(f'{DIRETORIO_PADRAO}{DIR_NOME}') and dir_personalizado in ['S', 's']:
        print('Diretorio personalizado ja existe!\nContinuando...')
        
    elif dir_personalizado in ['S', 's'] and os.path.exists(f'{DIRETORIO_PADRAO}{DIR_NOME}') == False:
        os.makedirs(f'{DIRETORIO_PADRAO}{DIR_NOME}')
        
    else:
        print('Continuando de onde parou!...')
        
    return f'{DIRETORIO_PADRAO}{DIR_NOME}'