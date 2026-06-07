import projeto_funções, escolha_classe
import projeto_arquivos
from cenarios import cap_01, cap_02, cap_03

txt_red = '\033[1;31m'
txt_green = '\033[1;32m'
txt_yellow = '\033[1;93m'
txt_cyan = '\033[1;36m'
end_txt = '\033[m'


def iniciar(nome_char, classe, status_list, dog):


    projeto_funções.logo_cap04()


    print(f'Ao seguir o caminho, {nome_char} se depara com uma fortaleza, e no seu portão lhe espera um golem de pedra que bloqueia a passagem. O golem percebe a presença de {nome_char} e {txt_yellow}começa a avançar, em direção a {nome_char}{end_txt} \n')
    print()

    while True:
        print(f'{txt_green}O que você decide fazer?{end_txt} \n 1 - Combater o golem (Sacar sua arma e atacar) \n 2 - Tentar desviar o caminho (Se evadir da investida do golem) \n 3 - Usar magia (Concentrar seu poder mágico para agir nessa situação) \n 4 - Manipulação e distração (Tentar tirar a atenção do golem de voçê ou tentar dialogar) \n')
        print()
        
        cen4_escolha = int(input("O que você decide fazer? \n"))
        print(150 * '-')
        print()
    
        sucesso = projeto_funções.dados_cen4()

        cen4_arq = ''

        match cen4_escolha:
            case 1: # Lutar
                if classe == 1:
                    print(f'Com sua força bruta, {nome_char} saca sua espada e ataca o golem, o destruindo')
                    cen4_arq = f'{nome_char} sacou sua espada e atacou o golem, o destruindo\n'
                    projeto_arquivos.salvar(cen4_arq)
                    break
                else:
                    if sucesso:
                        print(f'{txt_green}{nome_char} saca sua espada e ataca o golem, o destruindo{end_txt}')
                        cen4_arq = f'{nome_char} sacou sua espada e atacou o golem, o destruindo\n'
                        projeto_arquivos.salvar(cen4_arq)
                        break
                    else:
                        print(f'{txt_red}{nome_char} falha em atacar o golem e é atingido em cheio{end_txt}')
                        cen4_arq = f'{nome_char} tentou atacar o golem, mas falhou e foi atingido em cheio\n'
                        projeto_arquivos.salvar(cen4_arq)
                        projeto_funções.fim_de_jogo()
                    
            case 2: # Desviar/Evitar
                if classe == 2:
                    print(f'Com sua alta destreza, {nome_char} consegue se evadir da investida do golem e escapar ileso')
                    cen4_arq = f'{nome_char} conseguiu se evadir da investida do golem e escapar ileso\n'
                    projeto_arquivos.salvar(cen4_arq)
                    break
                else:
                    if sucesso:
                        print(f'{txt_green}{nome_char} consegue se evadir da investida do golem e escapar ileso{end_txt}')
                        cen4_arq = f'{nome_char} conseguiu se evadir da investida do golem e escapar ileso\n'
                        projeto_arquivos.salvar(cen4_arq)
                    else:
                        print(f'{txt_red}{nome_char} falha em se desviar da investida do golem e é atingido em cheio{end_txt}')
                        cen4_arq = f'{nome_char} tentou se desviar da investida do golem, mas falhou e foi atingido em cheio\n'
                        projeto_arquivos.salvar(cen4_arq)
                        projeto_funções.fim_de_jogo()

            case 3: # Magia
                if classe == 3:
                    if sucesso: # Sucesso
                        print(f'{txt_green}{nome_char} concentrou as suas forças arcanas e conjurou um feitiço de raio mágico, atingindo o golem{end_txt}')
                        cen4_arq = f'{nome_char} concentrou as suas forças arcanas e conjurou um feitiço de raio mágico, atingindo o golem\n'
                        projeto_arquivos.salvar(cen4_arq)
                        break
                    else:# Falha
                        print(f'{txt_green}{nome_char} tentou se concentrar em um feitiço de raio mágico, mas falhou e foi atingido pelo golem{end_txt}')
                        cen4_arq = f'{nome_char} tentou se concentrar em um feitiço de raio mágico, mas falhou e foi atingido pelo golem\n'
                        projeto_arquivos.salvar(cen4_arq)
                        projeto_funções.fim_de_jogo()
                        break

                elif classe == 4:
                    if sucesso: # Sucesso
                        print(f'{txt_green}{nome_char}chamou a natureza e conjurou raízes para sustentar a ponte, dando tempo o suficiente para atravessar a mesma{end_txt}')
                        cen4_arq = f'{nome_char}chamou a natureza e conjurou raízes para sustentar a ponte que caía, dando tempo o suficiente para atravessar a mesma\n'
                        projeto_arquivos.salvar(cen4_arq)
                        break
                    else: # Falha
                        print(f'{txt_red}{nome_char} chamou a natureza, mas ela falou "Mais 5 minutinhos zZz" e {nome_char} caiu no penhasco{end_txt}')
                        cen4_arq = f'{nome_char} chamou a natureza, mas ela falou "Mais 5 minutinhos zZz" e {nome_char} caiu no penhasco\n'
                        projeto_arquivos.salvar(cen4_arq)
                        projeto_funções.fim_de_jogo()

                else: # if classe == 1 or 2 or 5:
                    print(f'Sua classe não possui habilidades mágicas... {nome_char} foi atingido em cheio pelo golem')
                    cen4_arq = f'{nome_char} tentou usar magia mesmo não tendo escolhido uma classe que possui essas habilidades, e foi esmagado pelo golem\n'
                    projeto_arquivos.salvar(cen4_arq)
                    projeto_funções.fim_de_jogo()

            case 4: # Manipulação e distração
                if sucesso:
                    print(f'{txt_green}{nome_char} espera o golem se aproximar e elogia o shape do golem, dizendo que ele tem um design incrível e que é a melhor escultura de golem que já viu, o que faz o golem ficar confuso e sem jeito, dando tempo para {nome_char} escapar{end_txt}')
                    cen4_arq = f'{nome_char} elogiou a aparência do golem e conseguiu distraí-lo, dando tempo para {nome_char} escapar\n'
                    projeto_arquivos.salvar(cen4_arq)
                    break
                else:
                    print(f'{txt_red}{nome_char} tentou falar com o golem, mas falhou e foi atingido em cheio pelo mesmo{end_txt}')
                    cen4_arq = f'{nome_char} tentou falar com o golem, mas falhou e foi atingido em cheio pelo mesmo\n'
                    projeto_arquivos.salvar(cen4_arq)
                    projeto_funções.fim_de_jogo()

            case 0:
                projeto_funções.saiu_do_jogo(nome_char)
                projeto_funções.fim_de_jogo()
                break
            
            case _:
                print('Opção inválida')