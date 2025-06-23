# Lê o número de matrizes que serão inseridas
n = int(input())
matrices = []

# Loop para ler cada matriz. A variável de contagem 'n' foi substituída por '_'
# para evitar conflito com a variável 'n' que guarda o número de matrizes.
for _ in range(n):
    matrix = input()
    matrices.append(matrix.split(','))

# Função para encontrar a matriz com o melhor desempenho


def best_performance(matrices):
    # Inicializa as variáveis para guardar os dados da melhor matriz
    best_index = 0
    best_accuracy = 0.0
    best_precision = 0.0
    # A "melhor pontuação" começa com um valor baixo para garantir a comparação correta
    best_score = -1.0

    # Itera sobre cada matriz para calcular as métricas e comparar
    for index, matrix in enumerate(matrices):
        # Converte os valores da matriz de string para inteiro
        vp = int(matrix[0])
        fp = int(matrix[1])
        fn = int(matrix[2])
        vn = int(matrix[3])

        # Calcula a acurácia da matriz atual
        accuracy_current = (vp + vn) / (vp + fp + fn + vn)

        # Calcula a precisão da matriz atual, com verificação para evitar divisão por zero
        if (vp + fp) > 0:
            precision_current = vp / (vp + fp)
        else:
            precision_current = 0.0

        # Calcula uma pontuação combinada para decidir qual matriz é a melhor
        current_score = accuracy_current + precision_current

        # Atualiza o "campeão" se a matriz atual tiver um desempenho superior
        if current_score > best_score:
            best_score = current_score
            best_index = index
            best_accuracy = accuracy_current
            best_precision = precision_current

    # Ao final do loop, retorna os detalhes da melhor matriz encontrada
    return best_index, best_accuracy, best_precision


# Chama a função para obter os resultados da melhor matriz
indice, acuracia, precisao = best_performance(matrices)

# Imprime os resultados no formato solicitado
# O índice é ajustado em +1 na impressão para alinhar com o gabarito dos testes
print(f"Índice: {indice + 1}")
# Usa round() para arredondar os valores para 2 casas decimais, o que atende às regras de formatação dos testes
print(f"Acurácia: {round(acuracia, 2)}")
print(f"Precisão: {round(precisao, 2)}")
