import projeto_funções, escolha_classe

txt_red = '\033[1;31m'
txt_green = '\033[1;32m'
txt_yellow = '\033[1;93m'
txt_magenta = '\033[1;95m'
end_txt = '\033[m'

def iniciar(nome_char, classe, status_list):
    
    print(f'Ao seguir pela direita, {nome_char} encontra uma floresta densa e sombria. O ambiente é silencioso, exceto pelo som de folhas sendo pisadas e galhos quebrando sob os pés. De repente, um goblim aparece, bloqueando o caminho de {nome_char}. O goblim é pequeno, com pele verde e olhos vermelhos brilhantes. {txt_yellow}Ele segura uma adaga enferrujada e parece hostil.{end_txt}\n')
    print()
    
    cen3D = True
    
    while cen3D:
        print(f'{txt_green}O que você decide fazer?{end_txt}\n 1 - Combater o goblim (Sacar sua arma e atacar antes de ser atacado) \n 2 - Tentar desviar o caminho (Abrir distância e mudar a rota) \n 3 - Intimidação (Gritar e tentar assustar o goblim) \n 4 - Manipulação e distração (Tentar dialogar com o goblim) \n 0 - Sair do jogo\n')
        print()
        
        cen3D_escolha = int(input("O que você decide fazer? "))
        print(150 * '-')
        print()
    
        sucesso = projeto_funções.dados_cen3D()
        
        match cen3D_escolha:
            case 1: # Lutar
                if classe == 1:
                    cen3D = False
                    print(f'Com sua força bruta, {nome_char} saca sua espada e ataca o goblim, o matando')
                elif classe == 2:
                    cen3D = False
                    print(f'Com sua destreza, {nome_char} esquiva do golpe do goblim e contra-ataca, o derrotando')
                else:
                    if sucesso:
                        cen3D = False
                        print(f'{txt_green}Sucesso!{end_txt} {nome_char} ataca e derrota o goblim, a trilha está livre.')
                    else:
                        cen3D = False
                        print(f'{txt_red}Falha!{end_txt} {nome_char} não consegue derrotar o goblim na primeira tentativa. O goblim contra-ataca e fere {nome_char} antes de ser derrotado.')
                    
            case 2: # Desviar
                if sucesso:
                    cen3D = False
                    print(f'{txt_green}Sucesso!{end_txt} {nome_char} consegue desviar do goblim e continua seu caminho.')
                else:
                    cen3D = False
                    print(f'{txt_red}Falha!{end_txt} {nome_char} não consegue desviar do goblim e é atacado.')
                    
            case 3: # Intimidar
                if sucesso:
                    cen3D = False
                    print(f'{txt_green}Sucesso!{end_txt} {nome_char} consegue assustar o goblim e ele foge.')
                else:
                    cen3D = False
                    print(f'{txt_red}Falha!{end_txt} {nome_char} não consegue assustar o goblim.')
                    
            case 4: # Diálogo
                if sucesso:
                    cen3D = False
                    print(f'{txt_green}Sucesso!{end_txt} {nome_char} consegue conversar com o goblim. Ele pergunta : {txt_magenta}O que você está fazendo aqui?{end_txt}')

                    goblim_talk = int(input(f'{txt_green}O que você responde?{end_txt}\n 1 - Dizer que está perdido \n 2 - Dizer que está procurando por alguém \n 3 - Atacar enquando o goblim está destraído \n'))
                    
                    if 'companheiro' in status_list:
                        print(f'{txt_cyan}4 - Tentar subornar o goblim oferecendo {nome_dog} em troca da sua passagem{end_txt} \n')

                    match goblim_talk:
                        case 1:
                            print(f'{nome_char} diz que está perdido e o goblim o deixa passar.\nO goblim responde: {txt_magenta}Humm, você parece perdido mesmo. Pode passar, mas cuidado com o que tem mais adiante... a fortaleza da minha mestra{end_txt}\n')
                            break
                        case 2:
                            print(f'{nome_char} diz que está procurando por alguém e o goblim o deixa passar.')
                            break
                        case 3:
                            print(f'{txt_green}Sucesso!{end_txt} {nome_char} ataca o goblim, e consegue matá-lo.')
                            break
                        case 4:
                            if 'companheiro' in status_list:
                                print(f'O goblim responde: {txt_magenta}...como você ousa oferecer a vida do seu amigo em troca da sua passagem?? PODEM ATACAR!{end_txt}\nNesse momento mais tres goblins caem das arvores, e {txt_red}atacam {nome_char}e o matam{end_txt}')
                                projeto_funções.fim_de_jogo()

                    cen3D = False
                else:
                    cen3D = False
                    print(f'{txt_red}Falha!{end_txt} {nome_char} tenta conversar com o goblim, mas ele não entende e ataca.')
            
            case 0:
                cen3D = False
                projeto_funções.saiu_do_jogo(nome_char)
                projeto_arquivos.salvar(f'{nome_char} abandonou o jogo...\n {50 * '-'}')
                projeto_funções.fim_de_jogo()
                break
            
            case _:
                print('Opção inválida')