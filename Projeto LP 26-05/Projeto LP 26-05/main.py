import projeto_funções
from cenarios import cap_01, cap_02, cap_03 , cap_03D , cap_03E, cap_04
from escolha_classe import escolher_classe
import projeto_arquivos

txt_red = '\033[1;31m'
txt_green = '\033[1;32m'
txt_yellow = '\033[1;93m'
end_txt = '\033[m'


def inicio_jogo():
    projeto_funções.logo()

    print('\n\n')

    print('O reino está em apuros. De novo.\n\nDesta vez, a responsável é uma maga poderosa chamada Pythoria Finalis que vive em uma torre distante e parece ter como passatempo transformar guardas em galinhas e cobrar impostos de viajantes perdidos.\n\nCansado de lidar com o problema, o Rei Boolean, O Guardião da Verdade decidiu tomar uma medida extrema: contratar você.\n\nTalvez você derrote a maga. Talvez convença ela a fazer uma trégua. Talvez você acabe no fundo de um penhasco. Seja como for, sua aventura começa agora.\n\nDiga seu nome e escolha sua classe.\n\n')

    nome_char = input('Escolha o nome do seu personagem: ')
    nome_char_arq = f'{100 * '_'} \n Nome do personagem : {nome_char}\n'
    projeto_arquivos.salvar(nome_char_arq)

    print(150 * '_' + '\n\n')



    print(f'{txt_green}Escolha sua classe:{end_txt}\n\n 1 - Guerreiro\n 2 - Arqueiro\n 3 - Mago\n 4 - Druida\n 5 - Cozinheiro\n')
    classe = escolher_classe(nome_char)
    print('\n\n')

    print(f'\n{txt_green}Então {nome_char} sai para sua missão [...]\n{end_txt}')

    machucado = False

    status_list = []
    # if machucado:
    #     status_list.append('machucado')


    cap_01.iniciar(nome_char, classe, status_list)

    dog = cap_01.trazer_nome_dog()
    # print(dog)
    print(status_list)

    cap_02.iniciar(nome_char, classe, status_list, dog)

    print(status_list)

    bifur = cap_03.iniciar(nome_char, classe, status_list, dog)

    if bifur == True: # Seguiu pela direita
        cap_03D.iniciar(nome_char, classe, status_list, dog)

    elif bifur == False: # Seguiu pela esquerda
        cap_03E.iniciar(nome_char, classe, status_list, dog)

    cap_04.iniciar(nome_char, classe, status_list, dog)

inicio_jogo()