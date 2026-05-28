import projeto_funções, escolha_classe
import projeto_arquivos

txt_red = '\033[1;31m'
txt_green = '\033[1;32m'
txt_yellow = '\033[1;93m'
end_txt = '\033[m'

def iniciar(nome_char, classe, status_list):
    # CAPÍTULO 2.5 - BIFURCAÇÃO
    print(f'{150*'-'}\n\n')

    projeto_funções.logo_cap03()

    print(f'Ao sair da ponte {nome_char} encontra uma bifurcação e no meio dela uma {txt_yellow}placa em uma linguagem distinta{end_txt}')

    cap_3 = True

    while cap_3 == True:

        print(f'{txt_green}O que você decide fazer?{end_txt} \n 1 - Seguir o caminho da direita \n 2 - Seguir o caminho da esquerda \n 3 - Tentar ler o que a placa diz \n\n')

        cap_3_escolha = int(input('O que você decide fazer? '))
        cap_3_arq = ''

        match cap_3_escolha:
            case 1: # Direita
                direita(nome_char, classe)
                cap_3_arq = f'Na bifurcação, {nome_char} escolheu o caminho da direita'
                break

            case 2: # Esquerda
                esquerda(nome_char, classe)
                cap_3_arq = f'Na bifurcação, {nome_char} escolheu o caminho da esquerda'
                break

            case 3: # Tentar ler (Sucesso somente 3 - Mago)
                if classe == 3:
                    print(f'Se concentrou e leu a escrição pra ir pra {txt_green}esquerda{end_txt}')
                    cap_3_arq = f'Na bifurcação, {nome_char} usou sua inteligência elevada para ler a placa e compreender que o caminho certo era o da esquerda'
                else:
                    print(f'Por mais que {nome_char} tente, não consegue entender o que diz a placa\n')
                    cap_3_arq = f'Na bifurcação, {nome_char} tentou ler a placa, sem sucesso'

            case 0:
                projeto_funções.saiu_do_jogo(nome_char)
                projeto_funções.fim_de_jogo()
                break

            case _:
                print(f'{txt_red}Opção inválida{end_txt} \n')

        projeto_arquivos.salvar(cap_3_arq)

def direita(nome_char, classe):
    print(f'{nome_char}, escolheu direita')

def esquerda(nome_char, classe):
    print(f'{nome_char} escolheu esquerda')
