import time

palavras = list()
# Ler arquivo
with open('texto.txt', 'r') as arquivo:
    for linha in arquivo:
        palavras.extend(linha.split())
# Implementa o algoritmo de ordenação bolha
def bubble_sort(lista):
    # Obtém o tamanho da lista
    n = len(lista)
    # Itera sobre a lista, diminuindo o número de iterações internas a cada passagem.
    for i in range(n): 
        # Itera sobre os elementos da lista, comparando pares adjacentes.
        for j in range(0, n-i-1):
            # Se o elemento atual é maior que o próximo, os elementos são trocados de lugar
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        # Inicializa o índice do menor elemento como i
        min_idx = i
        # Itera sobre os elementos restantes, buscando o menor
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        #Troca o elemento atual pelo menor elemento encontrado.
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

# Usando Bubble Sort
inicio = time.time()
bubble_sorted = palavras.copy()
bubble_sort(bubble_sorted)
fim = time.time()
print("Bubble Sort:", bubble_sorted)
print("Tempo de execução Bubble Sort:", fim - inicio)

# Selection Sort
inicio = time.time()
selection_sorted = palavras.copy()
selection_sort(selection_sorted)
fim = time.time()
print("Selection Sort:", selection_sorted)
print("Tempo de execução Selection Sort:", fim - inicio)

# Método nativo sort()
inicio = time.time()
sorted_nativo = palavras.copy()
sorted_nativo.sort()
fim = time.time()
print("Método nativo sort():", sorted_nativo)
print("Tempo de execução sort():", fim - inicio)

# Salvar as palavras ordenadas em um novo arquivo
with open('texto_ordenado.txt', 'w') as arquivo_saida:
    for palavra in sorted_nativo:
        arquivo_saida.write(palavra + '\n')

