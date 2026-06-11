import projeto_funções, escolha_classe
import projeto_arquivos
from cenarios import cap_01

txt_red = '\033[1;31m'
txt_green = '\033[1;32m'
txt_yellow = '\033[1;93m'
end_txt = '\033[m'

name_dog = None

def iniciar(nome_char, classe, status_list):
    # CAPÍTULO 01 - O CATCHORO
    print(f'{150*'-'}\n\n')

    projeto_funções.logo_cap01()

    print(f'Ao sair do reino no começo da manhã, na entrada da floresta {nome_char} se depara com um cão selvagem de porte médio. O animal percebe a precença de \n{nome_char} e {txt_yellow}começa a rosnar, pronto para atacar{end_txt} \n')

    cen1 = True
    cen1_arq = ''

    while cen1 == True:
        print(f'{txt_green}O que você decide fazer?{end_txt} \n 1 - Sacar sua arma e atacar antes de ser atacado \n 2 - Abrir distância e mudar a rota \n 3 - Gritar e assustar o animal \n 4 - Tirar a atenção do animal de você \n')


        cen1_escolha = int(input('O que você decide fazer? \n'))

        print(f'{150*'-'}\n')

        sucesso = None
        if cen1_escolha == 1 and cen1_escolha == 2 and cen1_escolha == 3: #and cen1_escolha > 4:
            sucesso = projeto_funções.dados_cen1()

        match cen1_escolha:

            case 1: # Atacar
                if classe == 2: # Arqueiro - sucesso garantido
                    print(f'Com sua alta destreza, {nome_char} saca seu arco e ataca o animal, o matando')
                    cen1_arq = f'Matou o cao selvagem com seu arco\n'
                    projeto_arquivos.salvar(cen1_arq)
                    break
                else:
                    sucesso = projeto_funções.dados_cen1()
                    if sucesso:
                        print(f'{txt_green}Sucesso!{end_txt} {nome_char} ataca e mata o animal, a trilha está livre.')
                        cen1_arq = f'Matou o cão selvagem\n'
                        projeto_arquivos.salvar(cen1_arq)
                        break
                    else:
                        status_list.append('machucado')
                        print(f'{txt_red}Falha!{end_txt} {nome_char} não conseguiu sacar sua arma e atacar a tempo. {nome_char} é atacado pelo cão selvagem e tem sua perna machucada antes de ceifar a vida do animal.')
                        cen1_arq = f'Ficou machucado na luta contra o cao selvagem, mas conseguiu matá-lo\n'
                        projeto_arquivos.salvar(cen1_arq)
                        break

            case 2: # Desviar/Evitar
                sucesso = projeto_funções.dados_cen1()
                if sucesso:
                    print(f'{nome_char} dá alguns passos para tras, o animal segue seu caminho e deixa a trilha livre.')
                    cen1_arq = f'Desviou o caminho do cao selvagem\n'
                    projeto_arquivos.salvar(cen1_arq)
                    break
                else:
                    print(f'O cão percebeu a movimentação de {nome_char} e avançou em sua direção. {nome_char} saca sua arma, e consegue matar o animal.')
                    cen1_arq = f'{nome_char} tentou desviar do cao selvagem, mas não conseguiu, tendo que o matar\n'
                    projeto_arquivos.salvar(cen1_arq)
                    if classe == 4:
                        print(f'Por ser um druida, {nome_char} se sente mal por matá-lo, mas foi necessário...')
                        projeto_arquivos.salvar(f'Por ser um druida, {nome_char} se sente mal por matá-lo, mas foi necessário...\n')
                    break

            case 3: # Intimidar
                sucesso = projeto_funções.dados_cen1()
                if sucesso:
                    print(f'{nome_char} respira fundo e grita com todo o ar em seus pulmoes, conseguindo amedrontar o animal, que deixa a trilha livre.')
                    cen1_arq = f'{nome_char} intimidou o cao selvagem\n'
                    projeto_arquivos.salvar(cen1_arq)
                    break
                else:
                    status_list.append('machucado')
                    print(f'{nome_char} respira fundo e grita com todo o ar em seus pulmões, mas não foi o suficiente, o animal ataca {nome_char} que consegue se defender a tempo, porém tem sua perna machucada no processo.')
                    cen1_arq = f'{nome_char} tentou intimidar o cao selvagem, mas falhou e se machucou\n'
                    projeto_arquivos.salvar(cen1_arq)
                    break

            case 4: # Distrair (Sucesso)
                print((f'{nome_char} lembra de um osso do almoço do dia anterior que estava guardado no fundo da sua mochila, {nome_char} pega o osso e chama a atenção do animal,\nque desiste imediatamente de atacar {nome_char}, ficando muito feliz com o petisco, a trilha está livre, e o coração de {nome_char} mais leve\n'))
                cen1_arq = f'{nome_char} distraiu o cao selvagem com um osso, deixando-o muito feliz\n'
                projeto_arquivos.salvar(cen1_arq)

                print(f'{150*'-'}\n')

                # cap_01.name_dog = cap_01.adotar(nome_char, status_list)
                global name_dog
                name_dog = cap_01.adotar(nome_char, status_list)
                break



            case 0:
                projeto_funções.saiu_do_jogo(nome_char)
                projeto_funções.fim_de_jogo()
                projeto_arquivos.salvar(f'{nome_char} abandonou o jogo...\n {50 * '-'}')
                break

            case _:
                print(f'{txt_red}Opção inválida{end_txt} \n')
    return cen1







def adotar(nome_char, status_list):
    escolha_dog = None
    try:
        escolha_dog = int(input(f'{txt_green}Deseja adotá-lo? {end_txt}\n 1 - Sim \n 2 - Não\n'))
    except:
        print('Use um dos números acima ↑ para escolher a opção \n')
        adotar(nome_char, status_list)

    if escolha_dog == 1:
        print(f'{100 * '_'}\n')
        print(f'{txt_green}Ele segue você!{end_txt}')
        nome_dog = input('Qual nome você quer dar para ele? \n')
        print(f'{txt_green}{nome_char} adotou o cão selvagem, dando o nome de {nome_dog}!{end_txt}\n')
        cen1_arq = f'Adotou o cao selvagem, dando o nome de {nome_dog}\n'
        projeto_arquivos.salvar(cen1_arq)

        status_list.append('companheiro')
        return nome_dog
    
    elif escolha_dog == 2:
        print('O cao fica para tras, feliz com seu osso\n')
        return None
    
    else:
        print(f'{txt_red}Opção inválida{end_txt}\n')
        adotar(nome_char, status_list)
        
    return nome_dog

def trazer_nome_dog():
    return name_dog
    nome_dog = adotar(nome_char, status_list)


    