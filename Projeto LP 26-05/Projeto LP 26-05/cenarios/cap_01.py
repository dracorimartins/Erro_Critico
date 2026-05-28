import projeto_funções, escolha_classe
import projeto_arquivos

txt_red = '\033[1;31m'
txt_green = '\033[1;32m'
txt_yellow = '\033[1;93m'
end_txt = '\033[m'

def iniciar(nome_char, classe, status_list):
    # CAPÍTULO 02 - O CATCHORO
    print(f'{150*'-'}\n\n')

    projeto_funções.logo_cap01()

    print(f'Ao sair do reino no começo da manhã, na entrada da floresta {nome_char} se depara com um cão selvagem de porte médio. O animal percebe a precença de {nome_char} e começa a rosnar, pronto para atacar \n')

    cen1 = True

    while cen1 == True:
        print(f'{txt_green}O que você decide fazer?{end_txt} \n 1 - Combater o animal (Sacar sua arma e atacar antes de ser atacado) \n 2 - Tentar desviar o caminho (Abrir distância e mudar a rota) \n 3 - Intimidação (Gritar e tentar assustar o animal) \n 4 - Manipulação e distração (Tentar tirar a atenção do animal de voçê) \n')


        cen1_escolha = int(input('O que você decide fazer? '))
        cen1_arq = ''
        print(f'{150*'-'}\n')


        if cen1_escolha != 0 and cen1_escolha != 4:
            sucesso = projeto_funções.dados_cen1()

        match cen1_escolha:

            case 1: # Atacar
                if classe == 2:
                    cen1 = False # Sucesso
                    print(f'Com sua alta destreza, {nome_char} saca seu arco e ataca o animal, o matando')
                    cen1_arq = f'Matou o cão selvagem com seu arco\n'
                    break
                
                if classe == 4:
                    print(f'Por ser um druida, {nome_char} se sente mal em atacar um animal...')
                    
                else:
                    if sucesso:
                        cen1 = False # Sucesso
                        print(f'{txt_green}Sucesso!{end_txt} {nome_char} ataca e mata o animal, a trilha está livre.')
                        cen1_arq = f'Matou o cão selvagem\n'
                    else:
                        cen1 = False # Falha
                        status_list.append('machucado')
                        print(f'{txt_red}Falha!{end_txt} {nome_char} não conseguiu sacar sua arma e o atacar a tempo. {nome_char} é atacado pelo cão selvagem e tem sua perna machucada antes de ceifar a vida do animal.')
                        cen1_arq = f'Ficou machudado na luta contra o cão selvagem, mas conseguiu matá-lo\n'

            case 2: # Desviar/Evitar
                if sucesso:
                    cen1 = False # Sucesso
                    print(f'{nome_char} dá alguns passos para trás, o animal segue seu caminho e deixa a trilha livre.')
                    cen1_arq = f'Desviou o caminho do cão selvagem\n'
                else:
                    cen1 = False # Falha
                    print(f'O cão percebeu a movimentação de {nome_char} e avançou em sua direção. {nome_char} saca sua arma, e consegue matar do animal.')
                    cen1_arq = f'Tentou desviar do cão selvagem, mas não conseguiu, tendo que o matar\n' 
                    if classe == 4:
                        print(f'Por ser um druida, {nome_char} se sente mal por matá-lo, mas foi necessário...')

            case 3: # Intimidar
                if sucesso: 
                    cen1 = False # Sucesso
                    print(f'{nome_char} respira fundo e grita com todo o ar em seus pulmões, conseguindo amedrontar o animal, que deixa a trilha livre.')
                    cen1_arq = f'Intimidou o cão selvagem\n'
                else:
                    cen1 = False # Falha
                    status_list.append('machucado')
                    print(f'{nome_char} respira fundo e grita com todo o ar em seus pulmões, mas não foi o suficiente, o animal ataca {nome_char} que consegue se defender a tempo, porém tem sua perna machucada no processo.')
                    cen1_arq = f'{nome_char} tentou intimidar o cão selvagem, mas falhou e se machucou\n'

            case 4: # Distrair (Sucesso)
                cen1 = False
                print((f'{nome_char} lembra de um osso do almoço do dia anterior que estava guardado no fundo da sua mochila, {nome_char} pega o osso e chama a atenção do animal, que desiste imediatamente de atacar {nome_char}, ficando muito feliz com o petisco, a trilha está livre, e o coração de {nome_char} mais leve '))
                cen1_arq = f'{nome_char} distraiu o cão selvagem com um osso, deixando-o muito feliz\n'

            case 0:
                cen1 = False
                projeto_funções.saiu_do_jogo(nome_char)
                projeto_funções.fim_de_jogo()
                projeto_arquivos.salvar(f'{nome_char} abandonou o jogo...\n {50 * '-'}')
                break

            case _:
                print(f'{txt_red}Opção inválida{end_txt} \n')

    projeto_arquivos.salvar(cen1_arq)

    status_list.append('teste')

    return cen1