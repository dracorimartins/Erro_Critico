import projeto_funções, escolha_classe
import projeto_arquivos
from cenarios import cap_01, cap_02, cap_03

txt_red = '\033[1;31m'
txt_green = '\033[1;32m'
txt_yellow = '\033[1;93m'
end_txt = '\033[m'

def iniciar(nome_char, classe, status_list, nome_dog):
    # CAPÍTULO 02 - A PONTE DO RIO QUE CAI
    print(f'{150*'-'}\n\n')

    projeto_funções.logo_cap02()

    print(f'Ao proceguir pela trilha, {nome_char} se depara com uma ponte feita de corda e madeira, que passa por cima de um precipício, o outro caminho mais seguro levaria dias para ser alcançado, então {nome_char} decide atravessar a ponte. Mesmo com o vento forte e a condição precária da ponte, {nome_char} está praticamente conseguindo atravessá-la, até que escuta um estalo, e ao olhar pra trás {nome_char}, percebe que {txt_yellow}a ponte está prestes a cair!{end_txt}\n')


    cen2_arq = ''

    while True:

        print(f'{txt_green}O que você decide fazer?{end_txt} \n 1 - Correr! Usar sua agilidade para tentar cruzar a ponte antes que ela caia \n 2 - Usar magia. Reunir poder mágico para cruzar o restante do caminho independente da ponte \n 3 - Segurar as cordas laterais e andar com cuidado \n 4 - Tentar voltar. Seguir parece não ser uma alternativa. {nome_char} tenta voltar ao início da ponte para usar o caminho mais seguro \n')

        cen2_escolha = int(input('O que você decide fazer? \n'))
        print(f'{150*'-'}\n')

        if cen2_escolha != 0 and cen2_escolha != 4:
            if 'machucado' in status_list:
                sucesso_machucado = projeto_funções.dados_cen2_machucado()
            else:
                sucesso_cen2 = projeto_funções.dados_cen2()



        match cen2_escolha:

            case 1: # Correr
                if 'machucado' in status_list:
                    if sucesso_machucado: # Machucado sucesso
                        print(f'{txt_green}Apesar de estar machucado(a) devido ao encontro com o cachorro, {nome_char} consegue correr e chegar ao outro lado do penhasco antes da ponte cair{end_txt}')
                        cen2_arq = f'Apesar de estar machucado(a), {nome_char} conseguiu cruzar a ponte\n'
                        break
                    else: # Machucado falha
                        print(f'{txt_red}{nome_char} tenta correr, mas como está machucado devido ao encontro com o cachorro, não consegue atravessar a ponte a tempo, e cai no penhasco{end_txt}')
                        cen2_arq = f'Por estar machucado(a), {nome_char} não conseguiu cruzar a ponte a tempo, e caiu para sua morte\n'
                        projeto_arquivos.salvar(cen2_arq)
                        projeto_funções.fim_de_jogo()

                else:
                    if sucesso_cen2: # Sucesso
                        print(f'{txt_green}{nome_char} corre com todas as suas forças e consegue cruzar a ponte antes que a mesma caia{end_txt}')
                        cen2_arq = f'Correu da ponte que caía e conseguiu cruza-la\n'
                        break
                    else: # Falha
                        print(f'{txt_red}{nome_char} corre com todas as suas forças e mas mesmo assim não cruzar a ponte antes que a mesma caia...{end_txt}')
                        cen2_arq = f'Tentou correr para cruzar a ponte, mas não seguiu e caiu pra sua morte\n'
                        projeto_arquivos.salvar(cen2_arq)
                        projeto_funções.fim_de_jogo()

            case 2: # Magia
                if classe == 3:
                    if sucesso_cen2: # Sucesso
                        print(f'{txt_green}{nome_char} concentrou as suas forças arcanas e conjurou um feitiço de vôo, cruzando o restante da ponte voando{end_txt}')
                        cen2_arq = f'{nome_char} concentrou as suas forças arcanas e conjurou um feitiço de vôo, e cruzou a ponte que caía voando\n'
                        break
                    else:# Falha
                        print(f'{txt_green}{nome_char} tentou se concentrar em um feitiço de vôo, mas falhou e caiu{end_txt}')
                        cen2_arq = f'{nome_char} tentou se concentrar em um feitiço de vôo para cruzar a ponte que caía, mas falhou e caiu no penhasco\n'
                        projeto_arquivos.salvar(cen2_arq)
                        projeto_funções.fim_de_jogo()
                        break

                elif classe == 4:
                    if sucesso_cen2: # Sucesso
                        print(f'{txt_green}{nome_char}chamou a natureza e conjurou raízes para sustentar a ponte, dando tempo o suficiente para atravessar a mesma{end_txt}')
                        cen2_arq = f'{nome_char}chamou a natureza e conjurou raízes para sustentar a ponte que caía, dando tempo o suficiente para atravessar a mesma\n'
                        break
                    else: # Falha
                        print(f'{txt_red}{nome_char} chamou a natureza, mas ela falou "Mais 5 minutinhos zZz" e {nome_char} caiu{end_txt}')
                        cen2_arq = f'{nome_char} chamou a natureza, mas ela falou "Mais 5 minutinhos zZz" e {nome_char} caiu no penhasco\n'
                        projeto_arquivos.salvar(cen2_arq)
                        projeto_funções.fim_de_jogo()

                else: # if classe == 1 or 2 or 5:
                    print(f'Sua classe não possui habilidades mágicas... {nome_char} caiu no penhasco')
                    cen2_arq = f'{nome_char} tentou usar magia mesmo não tendo escolhido uma classe que possui essas habilidades, e caiu da ponte no penhasco\n'
                    projeto_arquivos.salvar(cen2_arq)
                    projeto_funções.fim_de_jogo()
                    break


            case 3: # Andar com cuidado
                if sucesso_cen2: # Sucesso
                    print(f'{txt_green}{nome_char} segurou firme nas cordas, andou devagar e com cuidado, e conseguiu atressar a ponte {end_txt}')
                    cen2_arq = f'{nome_char} atravessou a ponte com cuidado e paciência\n'
                    break
                else: # Falha
                    print(f'{txt_red}{nome_char} andou lentamente, mas a ponte caiu antes de {nome_char} conseguisse atravessar{end_txt}')
                    cen2_arq = f'{nome_char} tentou atravessar a ponte com cuidado, mas a mesma caiu antes que {nome_char} conseguisse atravessar\n'
                    projeto_arquivos.salvar(cen2_arq)
                    projeto_funções.fim_de_jogo()

            case 4: # Voltar = Falha
                print(f'{txt_red}A ponte caiu ...{end_txt}')
                cen2_arq = f'{nome_char} tentou voltar em uma ponte que obviamente ia cair, e quem diria... ela caiu\n'
                projeto_funções.fim_de_jogo()
                break

            case 0: 
                projeto_funções.saiu_do_jogo(nome_char)
                projeto_funções.fim_de_jogo()
                projeto_arquivos.salvar(f'{nome_char} abandonou o jogo...\n {50 * '-'}')

            case _:
                print(f'{txt_red}Opção inválida{end_txt} \n')

    projeto_arquivos.salvar(cen2_arq)
