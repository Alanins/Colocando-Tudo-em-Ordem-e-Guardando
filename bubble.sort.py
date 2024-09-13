def bubbleSort(array):
    # Itera sobre todos os elementos do array
    for i in range(len(array)):
        # Itera sobre os elementos restantes
        for j in range(0, len(array) - i - 1):
            # Compara os elementos adjacentes
            if array[j] > array[j + 1]:
                # Troca os elementos se estiverem na ordem errada
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

# Declara um array com 15 números
numeros = [64, 34, 25, 12, 22, 11, 90, 42, 56, 78, 23, 45, 67, 89, 10]

# Aplica o método bubbleSort
bubbleSort(numeros)

# Imprime o array ordenado
print("Array ordenado:")
print(numeros)