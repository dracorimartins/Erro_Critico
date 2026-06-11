#  Projeto LP - Jogo de Aventura Textual

Um jogo de aventura interativo baseado em texto desenvolvido em Python, onde você vive uma emocionante missão para derrotar (ou negociar com) a poderosa maga Pythoria Finalis.

##  Sinopse

O reino está em apuros novamente. Desta vez, a culpada é uma maga poderosa chamada **Pythoria Finalis** que vive em uma torre distante, transformando guardas em galinhas e cobrando impostos de viajantes perdidos.

Cansado do problema, o **Rei Boolean**, O Guardião da Verdade, toma uma medida extrema: contratar **você**. Talvez você derrote a maga. Talvez convença ela a fazer uma trégua. Talvez você acabe no fundo de um penhasco.

Seja como for, sua aventura começa agora.

##  Características

- **5 Classes de Personagem** com características únicas:
  -  **Guerreiro**: Força física e resistência
  -  **Arqueiro**: Velocidade e destreza
  -  **Mago**: Inteligência e magia
  -  **Druida**: Poderes da natureza
  -  **Cozinheiro?**: Carisma e culinária

- **Narrativa Ramificada**: Suas escolhas afetam o rumo da história
- **4 Capítulos** de aventura com bifurcações na trama
- **Sistema de Status**: Rastreie as condições do seu personagem durante a jornada
- **Interface Colorida**: Texto em cores ANSI para melhor experiência visual
- **Persistência de Dados**: Seu progresso é registrado em arquivo

##  Estrutura do Projeto

```
Projeto LP/
├── main.py                 # Arquivo principal - inicia o jogo
├── projeto_funções.py      # Funções utilitárias (logos ASCII e dados aleatórios)
├── projeto_arquivos.py     # Gerenciamento de arquivos
├── cores_texto.py          # Definições de cores ANSI
├── escolha_classe.py       # Sistema de seleção de classe
├── arquivo_EC.txt          # Registro de progresso
├── cenarios/               # Capítulos da aventura
│   ├── cap_01.py          # Capítulo 1
│   ├── cap_02.py          # Capítulo 2
│   ├── cap_03.py          # Capítulo 3 (com bifurcação)
│   ├── cap_03D.py         # Capítulo 3 - Rota Direita
│   ├── cap_03E.py         # Capítulo 3 - Rota Esquerda
│   ├── cap_04.py          # Capítulo 4 
│   ├── cap_05.py          # Capítulo 5 (final)
│   └── cap_base.py        # Base/utilitários dos cenários
└── README.md              # Este arquivo
```

##  Como Executar

### Pré-requisitos
- Python 3.7 ou superior
- Terminal com suporte a cores ANSI

### Instalação e Execução

1. Clone ou baixe o repositório
2. Navegue até a pasta do projeto:
   ```bash
   cd "Projeto LP"
   ```
3. Execute o jogo:
   ```bash
   python main.py
   ```

##  Fluxo do Jogo

1. **Início**: Exibe logo do jogo
2. **Criação do Personagem**:
   - Digite o nome do seu personagem
   - Escolha uma das 5 classes disponíveis
3. **Aventura**: Passe pelos 4 capítulos:
   - Capítulo 1: Primeiros passos
   - Capítulo 2: Desenvolvendo a trama
   - Capítulo 3: Bifurcação crucial (escolha entre rota D ou E)
   - Capítulo 4: Chegada ao objetivo
   - Capítulo 5: Capítulo final
4. **Progresso**: Suas ações são registradas em `arquivo_EC.txt`

##  Componentes

### arquivo_EC.txt
Arquivo de log que registra:
- Nome do personagem
- Eventos importantes da aventura
- Progresso e status durante a jornada

### Sistema de Cores
O jogo utiliza cores ANSI para melhor experiência:
-  Vermelho: Falhas/ações negativas 
-  Verde: Sucesso/ações positivas
-  Amarelo: Informações importantes sobre os cenários

##  Notas para Desenvolvedores

- O sistema de status (`status_list`) rastreia condições do personagem como "machucado"
- Os dados do personagem (nome e classe) são passados entre os capítulos
- Companheiro canino (`dog`) acompanha o personagem ao longo da aventura
- A estrutura modular permite fácil adição de novos capítulos ou cenários

##  Tratamento de Erros

O jogo inclui tratamento básico de erros:
- Validação de entrada para classe (apenas números de 1-5)
- Confirmação de escolha de classe antes de prosseguir
- Tratamento de exceções para entradas inválidas

##  Sobre o Projeto

Este é um projeto educacional desenvolvido em Python que demonstra:
- Programação modular
- Estruturas de controle de fluxo (match/case)
- Manipulação de arquivos
- Entrada/saída de dados
- Criação de narrativas interativas

##  Suporte

Para reportar bugs ou sugerir melhorias, verifique os arquivos do projeto e considere expandir o sistema de cenários ou adicionar novos tipos de classes.

##  Créditos

**Criadores do Projeto:**
- Douglas Leonardo - Responsável pelo fluxograma.

- Grazielli Sena - Responsável pelo sistema de escolha de classes, a base dos códigos dos cenários e a criação Capítulo 5.

- Ricardo Jorge - Responsável pela criação dos capítulos, organicação dos arquivos, arquivamento (e todo o resto).

- (Apoio - Allesson Carneiro)

**Ano:** 2026

**Diciplina** Lógica da Programação

---
