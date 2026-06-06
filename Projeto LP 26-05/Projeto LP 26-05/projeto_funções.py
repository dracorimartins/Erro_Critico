import random
import projeto_arquivos

# LOGOS

def logo():
    print(150 * '/')
    print(r'''                                                                                                                        
        ▄▄▄▄▄▄▄▄                                             ▄▄▄▄                 ▄█▀                ██                        
        ██▀▀▀▀▀▀                                           ██▀▀▀▀█               ▀▀       ██         ▀▀                        
        ██         ██▄████   ██▄████   ▄████▄             ██▀        ██▄████   ████     ███████    ████      ▄█████▄   ▄████▄  
        ███████    ██▀       ██▀      ██▀  ▀██            ██         ██▀         ██       ██         ██     ██▀    ▀  ██▀  ▀██ 
        ██         ██        ██       ██    ██            ██▄        ██          ██       ██         ██     ██        ██    ██ 
        ██▄▄▄▄▄▄   ██        ██       ▀██▄▄██▀             ██▄▄▄▄█   ██       ▄▄▄██▄▄▄    ██▄▄▄   ▄▄▄██▄▄▄  ▀██▄▄▄▄█  ▀██▄▄██▀ 
        ▀▀▀▀▀▀▀▀   ▀▀        ▀▀         ▀▀▀▀                 ▀▀▀▀    ▀▀       ▀▀▀▀▀▀▀▀     ▀▀▀▀   ▀▀▀▀▀▀▀▀    ▀▀▀▀▀     ▀▀▀▀   
                                                                                                                        
                                                                                                                        ''')
    print(150 * '/')

# FONT - CODER MINI

def logo_cap01():
    print(r'''
                                ▄▀                                                  
 ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄    ▄▄▄   ▄▄▄▄   ▄▄▄▄▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄         ▄▄▄▄     ▄▄▄▄ 
███▀▀▀▀▀ ███▀▀▀▀▀ ████▄  ███ ▄██▀▀██▄ ███▀▀███▄  ███  ▄███████▄     ▄██████▄ ▄█████ 
███      ███▄▄    ███▀██▄███ ███  ███ ███▄▄███▀  ███  ███   ███     ███  ███    ███ 
███      ███      ███  ▀████ ███▀▀███ ███▀▀██▄   ███  ███▄▄▄███     ███▄▄███    ███ 
▀███████ ▀███████ ███    ███ ███  ███ ███  ▀███ ▄███▄  ▀█████▀       ▀████▀     ███ 
''')

def logo_cap02():
    print(r'''  
                                ▄▀                                                    
 ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄    ▄▄▄   ▄▄▄▄   ▄▄▄▄▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄         ▄▄▄▄   ▄▄▄▄▄▄▄  
███▀▀▀▀▀ ███▀▀▀▀▀ ████▄  ███ ▄██▀▀██▄ ███▀▀███▄  ███  ▄███████▄     ▄██████▄ ▀▀▀▀████ 
███      ███▄▄    ███▀██▄███ ███  ███ ███▄▄███▀  ███  ███   ███     ███  ███    ▄██▀  
███      ███      ███  ▀████ ███▀▀███ ███▀▀██▄   ███  ███▄▄▄███     ███▄▄███  ▄███▄▄▄ 
▀███████ ▀███████ ███    ███ ███  ███ ███  ▀███ ▄███▄  ▀█████▀       ▀████▀  ████████ 
''')

def logo_cap03():
    print(r'''
                                ▄▀                                                    
 ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄    ▄▄▄   ▄▄▄▄   ▄▄▄▄▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄         ▄▄▄▄   ▄▄▄▄▄▄▄  
███▀▀▀▀▀ ███▀▀▀▀▀ ████▄  ███ ▄██▀▀██▄ ███▀▀███▄  ███  ▄███████▄     ▄██████▄ ▀▀▀▀████ 
███      ███▄▄    ███▀██▄███ ███  ███ ███▄▄███▀  ███  ███   ███     ███  ███   ▄▄██▀  
███      ███      ███  ▀████ ███▀▀███ ███▀▀██▄   ███  ███▄▄▄███     ███▄▄███     ███▄ 
▀███████ ▀███████ ███    ███ ███  ███ ███  ▀███ ▄███▄  ▀█████▀       ▀████▀  ███████▀ 
''')
    
def logo_cap03D():
    print(r'''
                                ▄▀                                                             
 ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄    ▄▄▄   ▄▄▄▄   ▄▄▄▄▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄       ▄▄▄▄   ▄▄▄▄▄▄▄    ▄▄▄▄▄▄   
███▀▀▀▀▀ ███▀▀▀▀▀ ████▄  ███ ▄██▀▀██▄ ███▀▀███▄  ███  ▄███████▄   ▄██████▄ ▀▀▀▀████   ███▀▀██▄ 
███      ███▄▄    ███▀██▄███ ███  ███ ███▄▄███▀  ███  ███   ███   ███  ███   ▄▄██▀    ███  ███ 
███      ███      ███  ▀████ ███▀▀███ ███▀▀██▄   ███  ███▄▄▄███   ███▄▄███     ███▄   ███  ███ 
▀███████ ▀███████ ███    ███ ███  ███ ███  ▀███ ▄███▄  ▀█████▀     ▀████▀  ███████▀   ██████▀  
''')

def logo_cap03E():
    print(r'''                 
                                ▄▀                                                             
 ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄    ▄▄▄   ▄▄▄▄   ▄▄▄▄▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄       ▄▄▄▄   ▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄ 
███▀▀▀▀▀ ███▀▀▀▀▀ ████▄  ███ ▄██▀▀██▄ ███▀▀███▄  ███  ▄███████▄   ▄██████▄ ▀▀▀▀████   ███▀▀▀▀▀ 
███      ███▄▄    ███▀██▄███ ███  ███ ███▄▄███▀  ███  ███   ███   ███  ███   ▄▄██▀    ███▄▄    
███      ███      ███  ▀████ ███▀▀███ ███▀▀██▄   ███  ███▄▄▄███   ███▄▄███     ███▄   ███      
▀███████ ▀███████ ███    ███ ███  ███ ███  ▀███ ▄███▄  ▀█████▀     ▀████▀  ███████▀   ▀███████ 
''')

def logo_cap04():
    print(r'''                 
                                ▄▀                                                  
 ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄    ▄▄▄   ▄▄▄▄   ▄▄▄▄▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄       ▄▄▄▄   ▄▄▄  ▄▄▄ 
███▀▀▀▀▀ ███▀▀▀▀▀ ████▄  ███ ▄██▀▀██▄ ███▀▀███▄  ███  ▄███████▄   ▄██████▄ ███  ███ 
███      ███▄▄    ███▀██▄███ ███  ███ ███▄▄███▀  ███  ███   ███   ███  ███ ███▄▄███ 
███      ███      ███  ▀████ ███▀▀███ ███▀▀██▄   ███  ███▄▄▄███   ███▄▄███  ▀▀▀████ 
▀███████ ▀███████ ███    ███ ███  ███ ███  ▀███ ▄███▄  ▀█████▀     ▀████▀      ████ 
''')

# FIM DE JOGO

def saiu_do_jogo(nome_char):
    print(f'{nome_char} escolheu abandonar sua aventura...')
    projeto_arquivos.salvar(f'{nome_char} escolheu abandonar sua aventura...\n')

def fim_de_jogo():
    print(r'''                                                                                                  
                                                                                                                            
 ▄████  ▄████▄ ██▄  ▄██ ██████   ▄████▄ ██  ██ ██████ █████▄  
██  ▄▄▄ ██▄▄██ ██ ▀▀ ██ ██▄▄     ██  ██ ██▄▄██ ██▄▄   ██▄▄██▄ 
 ▀███▀  ██  ██ ██    ██ ██▄▄▄▄   ▀████▀  ▀██▀  ██▄▄▄▄ ██   ██ 
                                                              ''')
    projeto_arquivos.salvar(f'GAME OVER\n')
    projeto_arquivos.salvar(f'{100 * "_"}\n\n')
    
    def tentar_novamente():
        jogar_novamente = int(input('Deseja tentar novamente?\n 1 - Sim\n 2 - Não\n'))
        if jogar_novamente == 1:
            import main
            main.inicio_jogo()
        elif jogar_novamente == 2:
            print('\033[1;32mNosso grupo agradece o tempo dedicado ao nosso jogo! Até uma próxima vez!! ^^/\033[m')
            exit()
        else:
            print('Use um dos números acima ↑ para escolher a opção \n')
            tentar_novamente()

    tentar_novamente()




# DADOS E SEUS CENÁRIOS

def dados_cen1():

    resultado_dado = random.randint(1, 100)
    print(f'Na abordagem ao animal, o resultado foi: {resultado_dado}/100')

    if resultado_dado >= 30:
        return True
    else:
        return False

def dados_cen2():

    resultado_dado = random.randint(1, 100)
    print(f'Ao tentar agir em relação a ponte, o resultado foi: {resultado_dado}/100')

    if resultado_dado >= 30:
        return True
    else:
        return False

def dados_cen2_machucado():
    resultado_dado = random.randint(1, 100)
    print(f'Apesar de estar machucado(a) , o resultado foi: {resultado_dado}/100')

    if resultado_dado >= 65:
        return True
    else:
        return False

def dados_cen3D():

    resultado_dado = random.randint(1, 100)
    print(f'Ao tentar agir em relação ao goblim, o resultado foi: {resultado_dado}/100')

    if resultado_dado >= 40:
        return True
    else:
        return False


def dados_cen4():

    resultado_dado = random.randint(1, 100)
    print(f'Ao tentar agir em relação ao golem, o resultado foi: {resultado_dado}/100')

    if resultado_dado >= 30:
        return True
    else:
        return False





