import projeto_funções
import projeto_arquivos

txt_red = '\033[1;31m'
txt_green = '\033[1;32m'
txt_yellow = '\033[1;93m'
end_txt = '\033[m'

def escolher_classe(nome_char):

    try:
        classe = int(input())
    except:
        print('Use um dos números acima ↑ para escolher a classe do seu parsonagem \n')
        escolher_classe(nome_char)
    
    nome_classe = ''

    match classe:
        case 1:
            print(f'O Guerreiro é a linha de frente do grupo. Ele resolve problemas com resistência, coragem e poder físico. \n{txt_yellow}Principal característica:{end_txt} Força física')
            print('Selecionar a classe de Guerreiro? \n 1 - Sim \n 2 - Não\n')
            escolha = int(input())

            if escolha == 1:
                print(f'{txt_green}Classe selecionada!{end_txt}')
                nome_classe = 'Guerreiro'

            elif escolha == 2:
                print('Escolha outra classe \n')
            else:
                print('Opção inválida')
        
        case 2:
            print(f'O Arqueiro é um combatente ágil e preciso que usa sua grande destreza e velocidade para atacar inimigos à distância com eficiência mortal. \n{txt_yellow}Principal característica:{end_txt} Velocidade e Destreza')
            print('Selecionar a classe de Arqueiro? \n1 - Sim \n2 - Não')
            escolha = int(input())

            if escolha == 1:
                print(f'{txt_green}Classe selecionada!{end_txt}')
                nome_classe = 'Arqueiro'

            elif escolha == 2:
                print('Escolha outra classe \n')
            else:
                print('Opção inválida')

        case 3:
            print(f'O Mago é um mestre das artes arcanas que utiliza sua enorme inteligência para manipular magia, desvendar conhecimentos antigos e lançar feitiços poderosos. \n{txt_yellow}Principal característica:{end_txt} Inteligência')
            print('Selecionar a classe de Mago? \n 1 - Sim \n 2 - Não')
            escolha = int(input())

            if escolha == 1:
                print(f'{txt_green}Classe selecionada!{end_txt}')
                nome_classe = 'Mago'

            elif escolha == 2:
                print('Escolha outra classe \n')
            else:
                print('Opção inválida')

        case 4:
            print(f'O Druida é ligado à natureza, aos espíritos e aos animais. \n{txt_yellow}Principal característica:{end_txt} Conexão animal e com a natureza')
            print('Selecionar a classe do Druida? \n 1 - Sim \n 2 - Não')
            escolha = int(input())

            if escolha == 1:
                print(f'{txt_green}Classe selecionada!{end_txt}')
                nome_classe = 'Druida'

            elif escolha == 2:
                print('Escolha outra classe \n')
            else:
                print('Opção inválida')

        case 5:
            print(f'O cozinheiro não tem experiência em batalha, espere chances menores de sucesso nessas situações. \n{txt_yellow}Principal característica:{end_txt} Carisma e... gastronimia?')
            print('Selecionar a classe do Cozinheiro? \n 1 - Sim \n 2 - Não')
            escolha = int(input())

            if escolha == 1:
                print(f'{txt_green}Classe selecionada!{end_txt}')
                nome_classe = 'Cozinheiro'
            elif escolha == 2:
                print('Escolha outra classe \n')
            else:
                print('Opção inválida')

        case 0:
            projeto_funções.saiu_do_jogo(nome_char)
            projeto_funções.fim_de_jogo()

            
        case _:
            print('Opção inválida.\n Use um dos números acima ↑ para escolher a classe do seu parsonagem \n Tente novamente \n')
            escolher_classe(nome_char)
            
    classe_arq = f'A classe selecionada foi : {nome_classe}\n'
    projeto_arquivos.salvar(classe_arq)

    return classe

print(150 * '-')