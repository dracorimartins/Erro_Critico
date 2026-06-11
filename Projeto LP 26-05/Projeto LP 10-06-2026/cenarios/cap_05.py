import projeto_funções
import projeto_arquivos

txt_red = '\033[1;31m'
txt_green = '\033[1;32m'
txt_yellow = '\033[1;93m'
txt_magenta = '\033[1;95m'
txt_cyan = '\033[1;36m'
end_txt = '\033[m'


def iniciar(nome_char, classe, status_list, name_dog):
    
    print(f'{150*'-'}\n\n')

    projeto_funções.logo_cap_final()

    if 'companheiro' in status_list:
        print(f'{nome_char} conseguiu... {nome_char} derrotou o golem e entrou na fortaleza.\n{nome_char} subiu as escadas e chegou a uma porta no fim de um corredor. {nome_char} decide deixar {name_dog} do lado de fora, é perigoso demais para ele. Chegou a hora de enfrentar Pythoria Finalis...\n')
    else:
        print(f'{nome_char} conseguiu... {nome_char} derrotou o golem e entrou na fortaleza.\n{nome_char} subiu as escadas e chegou a uma porta no fim de um corredor. Chegou a hora de enfrentar Pythoria Finalis...\n')

    print(f'{txt_magenta}Pythoria Finalis: Então, você é o aventureiro que o Rei Boolean enviou? Esperava alguém mais... impressionante.{end_txt}\n')
    print(f'{txt_cyan}{nome_char}: E eu esperava uma maga mais assustadora. Você transformou metade dos guardas em galinhas.{end_txt}\n')
    print(f'{txt_magenta}Pythoria Finalis: Foi um experimento arcano! O fato de ter sido extremamente engraçado foi apenas um bônus.{end_txt}\n')
    print(f'{txt_cyan}{nome_char}: E os impostos absurdos cobrados dos viajantes?!{end_txt}\n')
    print(f'{txt_magenta}Pythoria Finalis: A manutenção da torre não é barata! Você tem ideia de quanto custa alimentar um dragão de estimação?{end_txt}\n')
    print(f'{txt_cyan}{nome_char}: Você tem um dragão de estimação?!{end_txt}\n')
    print(f'{txt_magenta}Pythoria Finalis: Não. Mas eu gostaria de ter um...{end_txt}\n')
    print(f'{txt_yellow}Pythoria Finalis ergue seu cajado e uma energia mágica preenche o salão.{end_txt}\n')
    print(f'{txt_magenta}Pythoria Finalis: Chega de conversa. Se quer acabar com meus planos, terá que me derrotar!{end_txt}\n')

    vida_player = 100
    vida_phytoria = 100

    while vida_player > 0 and vida_phytoria > 0:

        print(f'Vida de {nome_char}: {txt_green}{vida_player}{end_txt}')
        print(f'Vida de Pythoria: {txt_red}{vida_phytoria}{end_txt}\n')

        if classe == 5:
            print(f'{txt_green}O que você decide fazer?{end_txt}\n 1 - Atacar\n 2 - Defender\n 3 - Conversar\n')
        else:
            print(f'{txt_green}O que você decide fazer?{end_txt}\n 1 - Atacar\n 2 - Defender\n')

        cen5_escolha = int(input('O que você decide fazer? \n'))
        print(f'{150*"-"}\n\n')

        defendendo = False

        match cen5_escolha:

            case 1:  # Atacar
                if projeto_funções.dados_player():
                    dmg = projeto_funções.dano_player(classe, status_list)
                    print(f'{txt_green}{nome_char} atacou Pythoria, causando {dmg} de dano!{end_txt}')
                    vida_phytoria -= dmg
                    projeto_arquivos.salvar(f'{nome_char} causou {dmg} de dano em Pythoria\n')
                else:
                    print(f'{txt_red}{nome_char} tentou atacar Pythoria mas errou o golpe!{end_txt}')
                    projeto_arquivos.salvar(f'{nome_char} errou o ataque contra Pythoria\n')

            case 2:  # Defender
                defendendo = True
                print(f'{nome_char} assume postura defensiva...')

            case 3:
                if classe != 5:
                    print(f'{txt_red}Você não tem o carisma necessário para isso... Pythoria ignora sua tentativa.{end_txt}')
                else:
                    print(f'{txt_cyan}{nome_char}: Espere!{end_txt}\n')
                    print(f'{txt_magenta}Pythoria Finalis: O que?{end_txt}\n')
                    print(f'{txt_cyan}{nome_char}: Antes de continuarmos, responda uma coisa.{end_txt}\n')
                    print(f'{txt_magenta}Pythoria Finalis: Estou prestes a jogar uma bola de fogo em você, seja rápido.{end_txt}\n')
                    print(f'{txt_cyan}{nome_char}: Há quanto tempo você não faz uma refeição decente?{end_txt}\n')
                    print(f'{txt_yellow}Pythoria Finalis fica em silêncio por alguns segundos.{end_txt}\n')
                    print(f'{txt_magenta}...Isso não é da sua conta.{end_txt}\n')
                    print(f'{txt_cyan}{nome_char}: Então faz muito tempo. Agora entendo por que você anda transformando guardas em galinhas.{end_txt}\n')
                    print(f'{txt_magenta}Pythoria Finalis: O que isso tem a ver?{end_txt}\n')
                    print(f'{txt_cyan}{nome_char}: Fome, irritação, falta de nutrientes... Diagnóstico clássico.{end_txt}\n')
                    print(f'{txt_yellow}{nome_char} retira uma panela de sua mochila.{end_txt}\n')
                    print(f'{txt_cyan}{nome_char}: Experimente meu Ensopado Supremo.{end_txt}\n')
                    print(f'{txt_magenta}Pythoria Finalis: Isso é uma armadilha?{end_txt}\n')
                    print(f'{txt_yellow}Você serve o prato. Pythoria Finalis prova um pouco.{end_txt}\n')
                    print(f'{txt_magenta}Pythoria Finalis: ...Isso está absurdamente bom. Como você fez isso?{end_txt}\n')
                    print(f'{txt_cyan}{nome_char}: Amor, manteiga e uma quantidade irresponsável de alho.{end_txt}\n')
                    print(f'{txt_yellow}Pythoria Finalis abaixa o cajado.{end_txt}\n')
                    print(f'{txt_magenta}Pythoria Finalis: Talvez eu tenha exagerado um pouco. Talvez os impostos mágicos tenham saído do controle. E talvez transformar guardas em galinhas não \ntenha sido necessário.{end_txt}\n')
                    print(f'{txt_cyan}{nome_char}: Então temos um acordo?{end_txt}')
                    print(f'{txt_magenta}Pythoria Finalis: Temos. Em troca da receita desse ensopado.{end_txt}\n')
                    print(f'\n{txt_green}FINAL PACÍFICO DESBLOQUEADO!\nPythoria Finalis abandonou seus planos malignos e abriu um restaurante.{end_txt}\n')
                    print(f'{txt_green}Nosso grupo agradece o tempo dedicado ao nosso jogo! Até uma próxima vez!! ^^/{end_txt}')
                    projeto_arquivos.salvar(f'{nome_char} convenceu Pythoria com culinária e alcançou o final pacífico\n')
                    projeto_arquivos.salvar(f'{100 * "_"}\n\n')
                    exit()
                    return

            case 0:
                projeto_funções.saiu_do_jogo(nome_char)
                projeto_arquivos.salvar(f'{nome_char} abandonou o jogo...\n {50 * '-'}')
                projeto_funções.fim_de_jogo()

            case _:
                print(f'{txt_red}Opção inválida{end_txt}\n')
                continue

        if defendendo:
            dmg = projeto_funções.dano_phytoria() // 2
            print(f'{txt_yellow}Pythoria lança uma bola de fogo! {nome_char} se defende e absorve metade do dano: {dmg}!{end_txt}')
            vida_player -= dmg
            projeto_arquivos.salvar(f'Pythoria causou {dmg} de dano em {nome_char} (defendendo)\n')
            
        else:
            if projeto_funções.dados_phytoria():
                dmg = projeto_funções.dano_phytoria()
                print(f'{txt_red}Pythoria lança uma bola de fogo em {nome_char}, causando {dmg} de dano!{end_txt}')
                vida_player -= dmg
                projeto_arquivos.salvar(f'Pythoria causou {dmg} de dano em {nome_char}\n')
                
            else:
                print(f'{txt_green}Pythoria errou o feitiço! O cajado soltou faíscas para o lado errado.{end_txt}')
        print()

    if vida_phytoria <= 0:
        print(f'\n{txt_green}{"=" * 50}')
        print(f'VITÓRIA! {nome_char} derrotou Pythoria Finalis!')
        print(f'{"=" * 50}{end_txt}\n')
        print(f'{txt_magenta}Pythoria Finalis: Impossível... Derrotada por um mero programador...{end_txt}\n')
        print(f'{txt_green}Nosso grupo agradece o tempo dedicado ao nosso jogo! Até uma próxima vez!! ^^/{end_txt}')
        projeto_arquivos.salvar(f'{nome_char} derrotou Pythoria Finalis!\n')
        projeto_arquivos.salvar(f'{100 * "_"}\n\n')
        projeto_funções.jogo_finalizado()

    elif vida_player <= 0:
        print(f'\n{txt_red}{nome_char} foi derrotado por Pythoria Finalis...{end_txt}\n')
        projeto_arquivos.salvar(f'{nome_char} foi derrotado por Pythoria Finalis\n')
        projeto_funções.fim_de_jogo()
        projeto_funções.jogo_finalizado()
