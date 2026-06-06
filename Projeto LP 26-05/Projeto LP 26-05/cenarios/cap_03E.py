# Passa ao lado da floresta e encontra um acampamento seguro, e vai direto para o cenário 4
import projeto_funções, escolha_classe
import projeto_arquivos
from cenarios import cap_01, cap_02, cap_03


txt_red = '\033[1;31m'
txt_green = '\033[1;32m'
txt_yellow = '\033[1;93m'
end_txt = '\033[m'


def iniciar(nome_char, classe, status_list, nome_dog):

    projeto_funções.logo_cap03E()

    if 'companheiro' in status_list:
        print(f'Ao seguir pela esquerda, {nome_char} junto com {nome_dog} passam ao lado de uma floresta e encontram um acampamento seguro, onde podem descansar e recuperar suas forças. Depois de descansar, {nome_char} decide seguir em frente \n')
    else:
        print(f'Ao seguir pela esquerda, {nome_char} passa ao lado de uma floresta e encontra um acampamento seguro, onde pode descansar e recuperar suas forças. Depois de descansar, {nome_char} decide seguir em frente \n')
        if 'machucado' in status_list:
            status_list.remove('machucado')
            print(f'{txt_green}Após descansar, {nome_char} se sente melhor e recuperou do machucado{end_txt} \n')