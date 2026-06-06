import projeto_funções, escolha_classe
import projeto_arquivos
from cenarios import cap_01, cap_02, cap_03

txt_red = '\033[1;31m'
txt_green = '\033[1;32m'
txt_yellow = '\033[1;93m'
txt_cyan = '\033[1;36m'
end_txt = '\033[m'

# def direita(nome_char, classe):
#     print(f'{txt_green}{nome_char}, escolheu o caminho da direita{end_txt}')
#     return False

# def esquerda(nome_char, classe):
#     print(f'{txt_green}{nome_char} escolheu o caminho da esquerda{end_txt}')
#     return True

def iniciar(nome_char, classe, status_list, nome_dog):
    # CAPÍTULO 3 - BIFURCAÇÃO
    print(f'{150*'-'}\n\n')

    projeto_funções.logo_cap03()

    print(f'Ao sair da ponte, {nome_char} encontra uma bifurcação e no meio dela uma {txt_yellow}placa em uma linguagem distinta{end_txt} \n')

    cen3_arq = ''

    while True:

        print(f'{txt_green}O que você decide fazer?{end_txt} \n 1 - Seguir o caminho da direita \n 2 - Seguir o caminho da esquerda \n 3 - Tentar ler o que a placa diz')
        
        if 'companheiro' in status_list:
            print(f'{txt_cyan} 4 - Perguntar para {nome_dog} que caminho vocês devem seguir{end_txt}\n')


        cap_3_escolha = int(input('O que você decide fazer? \n'))

        match cap_3_escolha:
            case 1: # Direita
                cen3_arq = f'Na bifurcação, {nome_char} escolheu o caminho da direita \n'
                projeto_arquivos.salvar(cen3_arq)
                return True
                break

            case 2: # Esquerda
                cen3_arq = f'Na bifurcação, {nome_char} escolheu o caminho da esquerda \n'
                projeto_arquivos.salvar(cen3_arq)
                return False
                break

            case 3: # Tentar ler (Sucesso somente 3 - Mago)
                if classe == 3:
                    print(f'Se concentrou e leu a escrição pra ir pra {txt_green}esquerda{end_txt}')
                    cen3_arq = f'Na bifurcação, {nome_char} usou sua inteligência elevada para ler a placa e compreender que o caminho certo era o da esquerda \n'
                    projeto_arquivos.salvar(cen3_arq)
                else:
                    print(f'Por mais que {nome_char} tente, não consegue entender o que diz a placa\n')
                    cen3_arq = f'Na bifurcação, {nome_char} tentou ler a placa, sem sucesso \n'
                    projeto_arquivos.salvar(cen3_arq)

            case 4: # Perguntar para o cachorro 
                print(f'{txt_cyan}Perguntou para {nome_dog} que caminho seguir, e ele indicou a esquerda abanando o rabo, e rosnou para a direita \n{end_txt}')
                cen3_arq = f'Na bifurcação, {nome_char} perguntou para {nome_dog} que caminho seguir, e ele indicou a esquerda abanando o rabo, e rosnou para a direita \n'
                projeto_arquivos.salvar(cen3_arq)

            case 0:
                projeto_funções.saiu_do_jogo(nome_char)
                projeto_arquivos.salvar(f'{nome_char} abandonou o jogo...\n {50 * '-'}')
                projeto_funções.fim_de_jogo()


            case _:
                print(f'{txt_red}Opção inválida{end_txt} \n')


# def direita(nome_char, classe):
#     print(f'{nome_char}, escolheu o caminho da direita')
#     return False

# def esquerda(nome_char, classe):
#     print(f'{nome_char} escolheu o caminho da esquerda')
#     return True
