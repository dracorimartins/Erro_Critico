import projeto_funções, escolha_classe

def iniciar(nome_char, classe, status_list):
    if direita :
        print(f'Ao sair da floresta, {nome_char} se depara com uma fortaleza, e no seu portão lhe espera um golem de pedra que bloqueia a passagem. O golem percebe a presença de {nome_char} e {txt_yellow}começa a avançar, em direção a {nome_char}{end_txt} \n')
        print()
    elif esquerda:
        print(f'Ao sair do acampamento, {nome_char} se depara com uma fortaleza, e no seu portão lhe espera um golem de pedra que bloqueia a passagem. O golem percebe a presença de {nome_char} e {txt_yellow}começa a avançar, em direção a {nome_char}{end_txt} \n')
        print()
    
    while cen4:
        print(f'{txt_green}O que você decide fazer?{end_txt} \n 1 - Combater o golem (Sacar sua arma e atacar) \n 2 - Tentar desviar o caminho (Se evadir da investida do golem) \n 3 - Usar magia (Concentrar seu poder mágico para agir nessa situação) \n 4 - Manipulação e distração (Tentar tirar a atenção do golem de voçê ou tentar dialogar) \n')
        print()
        
        cen4_escolha = int(input("O que você decide fazer? \n"))
        print(150 * '-')
        print()
    
        sucesso = projeto_funções.dados_cen4()

        match cen4_escolha:
            case 1:
                if sucesso:
                    print(f'sucesso')
                else:
                    print(f'falha')
                    
            case 2:
                if sucesso:
                    print(f'sucesso')
                else:
                    print(f'falha')
                    
            case 3:
                if sucesso:
                    print(f'sucesso')
                else:
                    print(f'falha')
                    
            case 4:
                if sucesso:
                    print(f'sucesso')
                else:
                    print(f'falha')
                    
            case 0:
                projeto_funções.saiu_do_jogo(nome_char)
                projeto_funções.fim_de_jogo()
                break
            
            case _:
                print('Opção inválida')