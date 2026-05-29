import projeto_funções
from cenarios import cap_01, cap_02, cap_03
from escolha_classe import escolher_classe
import projeto_arquivos

txt_red = '\033[1;31m'
txt_green = '\033[1;32m'
txt_yellow = '\033[1;93m'
end_txt = '\033[m'

projeto_funções.logo()

print('\n\n')

nome_char = input('Escolha o nome do seu personagem: ')
nome_char_arq = f'{75 * '-'} \n Nome do personagem : {nome_char}\n'
projeto_arquivos.salvar(nome_char_arq)
print(f'\nEntão {nome_char} sai para sua missão [...]\n')
print(150 * '-')

print(f'{txt_green}Escolha sua classe:{end_txt}\n\n 1 - Guerreiro\n 2 - Arqueiro\n 3 - Mago\n 4 - Druida\n 5 - Cozinheiro\n')
classe = escolher_classe(nome_char)
print()

machucado = False

status_list = []
if machucado:
    status_list.append('machucado')

cap_01.iniciar(nome_char, classe, status_list)
cap_02.iniciar(nome_char, classe, status_list)
cap_03.iniciar(nome_char, classe, status_list)