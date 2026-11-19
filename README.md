🍎 Jogo da Forca – Frutas
📌 Descrição do projeto

Este projeto consiste no desenvolvimento de um jogo da forca em Python, utilizando frutas como tema principal.

O objetivo é descobrir uma palavra secreta por meio de tentativas de letras, antes que o limite máximo de erros seja atingido.

A cada partida, o programa seleciona aleatoriamente uma fruta de uma lista predefinida e apresenta sua representação oculta ao jogador. Conforme as letras são informadas, o jogo verifica se elas pertencem à palavra secreta e atualiza seu estado, indicando os acertos e erros.

🎯 Objetivo

O projeto tem como objetivo aplicar e consolidar conceitos fundamentais da linguagem Python, especialmente:

Funções e modularização.
Estruturas condicionais (if, elif e else).
Estruturas de repetição (while e for).
Listas (list).
Conjuntos (set).
Tuplas (tuple).
Manipulação de strings.
Entrada e saída de dados (input e print).
Importação e utilização de módulos (random).
⚙️ Funcionalidades

O jogo apresenta as seguintes funcionalidades:

Seleção aleatória de uma fruta.
Representação da palavra secreta por letras ocultas (_).
Recebimento e validação das letras informadas pelo jogador.
Identificação de letras corretas e incorretas.
Verificação de letras repetidas.
Revelação de todas as ocorrências de uma letra encontrada.
Exibição do histórico de letras já tentadas.
Controle de até 6 tentativas incorretas.
Identificação automática das condições de vitória ou derrota.
Exibição da palavra secreta ao final da partida.
🍓 Banco de palavras

O jogo utiliza uma lista predefinida de frutas:

BANANA
MORANGO
LARANJA
ABACAXI
MANGA
UVA

A seleção da palavra é realizada por meio da função random.choice(), que escolhe um elemento aleatório da lista.

🧩 Organização do código

O código está organizado em três funções principais, cada uma com uma responsabilidade específica.

1. iniciar_jogo(lista_palavras)

Responsável pela inicialização da partida.

Suas principais operações são:

Selecionar aleatoriamente a palavra secreta.
Criar uma lista de caracteres ocultos (_), com o mesmo comprimento da palavra escolhida.
Inicializar um conjunto vazio para armazenar as letras tentadas.
Definir o limite inicial de 6 tentativas.

Ao final, retorna uma tupla contendo o estado inicial do jogo.

2. processar_tentativa(letra, palavra_secreta, palavra_oculta, letras_tentadas)

Responsável por processar cada tentativa realizada pelo jogador.

A função verifica se a letra já foi utilizada e, caso seja uma nova tentativa, verifica sua presença na palavra secreta.

Quando a letra é encontrada, todas as suas ocorrências são reveladas na palavra oculta. Caso contrário, a função informa que houve um erro.

O retorno indica o resultado do processamento:

"repetida": a letra já havia sido escolhida.
"acertou": a letra pertence à palavra secreta.
"errou": a letra não pertence à palavra secreta.
3. jogo()

Responsável por coordenar a execução da partida.

Suas principais responsabilidades são:

Definir o banco de palavras.
Inicializar o estado do jogo.
Exibir o progresso da partida.
Solicitar e validar as entradas do jogador.
Chamar a função processar_tentativa().
Atualizar o número de tentativas restantes.
Verificar as condições de encerramento.
Exibir a mensagem de vitória ou derrota.

A partida continua enquanto houver tentativas disponíveis e ainda existirem letras ocultas na palavra.

💻 Tecnologias utilizadas
Python 3: linguagem utilizada no desenvolvimento do projeto.
Módulo random: biblioteca nativa utilizada para realizar a seleção aleatória da palavra secreta.

Não é necessária a instalação de bibliotecas externas.

▶️ Como executar o projeto
Pré-requisitos
Ter o Python 3 instalado no computador.
Ter acesso a um terminal ou editor de código compatível com Python.
Clonando o repositório

Faça o download do projeto utilizando o comando:

bash
git clone https://github.com/Lucas4878/forca.py.git


Em seguida, acesse a pasta:

bash
cd jogo-da-forca

Executando o programa

Execute o arquivo principal com o seguinte comando:

bash
python jogo_forca.py


Em alguns sistemas operacionais, pode ser necessário utilizar:

bash
python3 jogo_forca.py

🎮 Como jogar
Execute o programa.
Aguarde o sorteio aleatório de uma fruta.
Observe a quantidade de letras ocultas.
Digite uma letra por vez.
Caso a letra pertença à palavra, sua posição será revelada.
Caso contrário, será descontada uma tentativa.
Letras repetidas serão identificadas e não descontarão tentativas.
Descubra todas as letras antes de esgotar as 6 tentativas para vencer.

A partida termina quando o jogador descobre a palavra completa ou quando não possui mais tentativas disponíveis.

Exemplo de execução
text
=== JOGO DA FORCA - FRUTAS ===

Palavra: _ _ _ _ _ _
Tentativas restantes: 6
Letras tentadas:

Digite uma letra: A
Boa! A letra 'A' está na palavra.

Palavra: _ A _ A _ A
Tentativas restantes: 6
Letras tentadas: A

Digite uma letra: E
A letra 'E' não está na palavra.
Você perdeu uma tentativa.

Palavra: _ A _ A _ A
Tentativas restantes: 5
Letras tentadas: A E


Observação: a palavra e os resultados apresentados são ilustrativos e podem variar conforme o sorteio aleatório.

📂 Estrutura do projeto
text
jogo-da-forca/
│
├── jogo_forca.py    # Código-fonte do jogo
└── README.md        # Documentação do projeto

📚 Estruturas de dados e decisões de implementação

Durante o desenvolvimento, foram utilizadas diferentes estruturas de dados, escolhidas de acordo com as necessidades de cada parte do programa.

Lista (list)

Utilizada para armazenar o banco de frutas e representar a palavra oculta.

A escolha dessa estrutura permite acessar e modificar elementos por meio de índices, possibilitando revelar individualmente as letras descobertas.

Conjunto (set)

Utilizado para armazenar as letras já tentadas pelo jogador.

A escolha do conjunto evita automaticamente elementos duplicados e permite verificar a existência de uma letra com complexidade média O(1), tornando a identificação de tentativas repetidas mais eficiente.

Tupla (tuple)

Utilizada como estrutura de retorno da função iniciar_jogo().

Permite agrupar e retornar os diferentes elementos do estado inicial da partida em uma única estrutura, facilitando o desempacotamento das variáveis na função principal.

Modularização

O programa foi dividido em funções com responsabilidades específicas, favorecendo a organização, a reutilização de código, a legibilidade e a manutenção.

👨‍💻 Considerações finais

O desenvolvimento do Jogo da Forca proporcionou a aplicação prática de conceitos fundamentais da programação em Python, especialmente no uso de funções, estruturas condicionais, laços de repetição e estruturas de dados.

A separação das responsabilidades em funções independentes contribuiu para uma melhor organização do código, facilitando sua compreensão e manutenção.

Além de exercitar a lógica de programação, o projeto demonstra a importância de selecionar estruturas de dados adequadas para resolver problemas de maneira organizada e eficiente.

Projeto desenvolvido para fins educacionais, com o objetivo de praticar conceitos fundamentais da linguagem Python.
