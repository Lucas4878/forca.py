# jogo_forca.py
import random  # Importa o módulo random para permitir a escolha aleatória de palavras

def iniciar_jogo(lista_palavras):
    """Inicializa o jogo da forca.

    Propósito:
        Escolher a palavra secreta e preparar os estados iniciais do jogo.

    Argumentos:
        lista_palavras (list): lista contendo as palavras possíveis do jogo.

    Retorno:
        tuple: palavra_secreta (str), palavra_oculta (list), letras_tentadas
        (set), tentativas (int)
    """
    # Sorteia uma palavra aleatória da lista recebida como argumento
    palavra_secreta = random.choice(lista_palavras)

    # Cria uma lista de underscores ("_") com o mesmo comprimento da palavra secreta
    palavra_oculta = ["_"] * len(palavra_secreta)

    # Uso de set para armazenar letras já tentadas:
    # Escolhi 'set' em vez de lista pois conjuntos permitem verificar a existência
    # de um elemento com complexidade O(1) e evitam duplicatas automaticamente,
    # tornando a validação de tentativas repetidas mais eficiente.
    letras_tentadas = set()

    # Define o número máximo de erros que o jogador pode cometer
    tentativas = 6

    # Retorna o estado inicial do jogo estruturado em uma tupla
    return palavra_secreta, palavra_oculta, letras_tentadas, tentativas


def processar_tentativa(letra, palavra_secreta, palavra_oculta, letras_tentadas):
    """Processa a tentativa do jogador.

    Propósito:
        Verificar se a letra já foi usada, se está na palavra e atualizar o
        estado do jogo.

    Argumentos:
        letra (str): letra digitada pelo jogador
        palavra_secreta (str): palavra do jogo
        palavra_oculta (list): estado atual exibido ao jogador
        letras_tentadas (set): conjunto de letras já utilizadas

    Retorno:
        str: 'repetida', 'acertou' ou 'errou'
    """

    # Verifica se a letra informada já está no conjunto de letras utilizadas
    if letra in letras_tentadas:
        return "repetida"

    # Adiciona a nova letra ao conjunto de tentativas realizadas
    letras_tentadas.add(letra)

    # Verifica se a letra faz parte da palavra secreta
    if letra in palavra_secreta:
        # Percorre cada índice da palavra secreta para encontrar todas as ocorrências da letra
        # Lista é usada porque permite atualização por índice (posição exata da letra)
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_oculta[i] = letra
        return "acertou"
    else:
        # Se a letra não estiver na palavra secreta, indica erro
        return "errou"


def jogo():
    """
    Propósito:
        Coordena o loop principal do jogo, solicita a entrada do usuário,
        chama a função processar_tentativa e atualiza a contagem de tentativas.

    Argumentos:
        Nenhum.

    Retorno:
        None (A função apenas executa o loop principal e imprime o resultado final).
    """
    # Banco de palavras temático para o jogo
    frutas = ["BANANA", "MORANGO", "LARANJA", "ABACAXI", "MANGA", "UVA"]

    # Desempacota as variáveis de estado retornadas pela função de inicialização
    palavra_secreta, palavra_oculta, letras_tentadas, tentativas = iniciar_jogo(
        frutas
    )

    print("=== JOGO DA FORCA - FRUTAS ===")

    # O jogo roda enquanto o jogador tiver tentativas disponíveis E ainda existirem letras ocultas ("_")
    while tentativas > 0 and "_" in palavra_oculta:
        # Exibe o progresso atual com f-strings para formatação uniforme
        print(f"\nPalavra: {' '.join(palavra_oculta)}")
        print(f"Tentativas restantes: {tentativas}")
        # Exibe as letras tentadas ordenadas para melhor leitura do histórico
        print(f"Letras tentadas: {' '.join(sorted(letras_tentadas))}")

        # Solicita a entrada do usuário e a transforma em maiúscula
        letra = input("Digite uma letra: ").upper()

        # Validação simples de entrada: garante que é apenas 1 caractere e que este caractere é uma letra
        if not letra.isalpha() or len(letra) != 1:
            print("Entrada inválida! Digite apenas uma letra.")
            continue

        # Processa a letra validada e obtém o status da jogada
        resultado = processar_tentativa(
            letra, palavra_secreta, palavra_oculta, letras_tentadas
        )

        # Analisa o retorno da função de processamento para interagir com o jogador
        if resultado == "repetida":
            print(f"A letra '{letra}' já foi escolhida anteriormente. Escolha outra.")
        elif resultado == "acertou":
            print(f"Boa! A letra '{letra}' está na palavra.")
        else:
            print(f"A letra '{letra}' não está na palavra. Você perdeu uma tentativa.")
            tentativas -= 1

    # Fim do loop: Verifica a condição de vitória ou derrota
    if "_" not in palavra_oculta:
        print(f"\nParabéns! Você venceu! A fruta era: {palavra_secreta}")
    else:
        print(f"\nGame Over! Você perdeu. A fruta era: {palavra_secreta}")


# Garante que a função jogo() só será executada se o script for rodado diretamente
if __name__ == "__main__":
    jogo()