import projeto_funções
from cenarios import cap_01, cap_02, cap_03 , cap_03D
from escolha_classe import escolher_classe
import projeto_arquivos

txt_red = '\033[1;31m'
txt_green = '\033[1;32m'
txt_yellow = '\033[1;93m'
end_txt = '\033[m'


def inicio_jogo():
    projeto_funções.logo()

    print('\n\n')

    nome_char = input('Escolha o nome do seu personagem: ')
    nome_char_arq = f'{100 * '_'} \n Nome do personagem : {nome_char}\n'
    projeto_arquivos.salvar(nome_char_arq)
    print(f'\nEntão {nome_char} sai para sua missão [...]\n')
    print(150 * '_' + '\n\n')



    print(f'{txt_green}Escolha sua classe:{end_txt}\n\n 1 - Guerreiro\n 2 - Arqueiro\n 3 - Mago\n 4 - Druida\n 5 - Cozinheiro\n')
    classe = escolher_classe(nome_char)
    print()

    machucado = False

    status_list = []
    if machucado:
        status_list.append('machucado')


    cap_01.iniciar(nome_char, classe, status_list)

    dog = cap_01.trazer_nome_dog()
    # print(dog)
    print(status_list)

    cap_02.iniciar(nome_char, classe, status_list, dog)

    cap_03.iniciar(nome_char, classe, status_list, dog)
    print(status_list)

    cap_03D.iniciar(nome_char, classe, status_list, dog)

inicio_jogo()