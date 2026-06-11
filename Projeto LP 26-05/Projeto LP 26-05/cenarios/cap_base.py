import projeto_funções, escolha_classe

def iniciar(nome_char, classe, status_list):
    
    print(f'inserir historia')
    print()
    
    while True:
        print(f'inserir opções')
        print()
        
        cenN_escolha = int(input("O que você decide fazer? "))
        print(150 * '-')
        print()
    
        sucesso = projeto_funções.dados_cenN()

        match cenN_escolha:
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