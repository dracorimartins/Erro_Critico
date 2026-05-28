import projeto_funções, escolha_classe

def iniciar(nome_char, classe, status_list):
    
    print(f'inserir historia')
    print()
    
    cen3 = True
    
    while cen3:
        print(f'inserir opções')
        print()
        
        cen3_escolha = int(input("O que você decide fazer? "))
        print(150 * '-')
        print()
    
        sucesso = projeto_funções.dados_cen1()
        match cen3_escolha:
            case 1:
                if sucesso:
                    cen3 = False
                    print(f'sucesso')
                else:
                    cen3 = False
                    print(f'falha')
                    
            case 2:
                if sucesso:
                    cen3 = False
                    print(f'sucesso')
                else:
                    cen3 = False
                    print(f'falha')
                    
            case 3:
                if sucesso:
                    cen3 = False
                    print(f'sucesso')
                else:
                    cen3 = False
                    print(f'falha')
                    
            case 4:
                if sucesso:
                    cen3 = False
                    print(f'sucesso')
                else:
                    cen3 = False
                    print(f'falha')
                    
            case 0:
                projeto_funções.saiu_do_jogo(nome_char)
                projeto_funções.fim_de_jogo()
                break
            
            case _:
                print('Opção inválida')