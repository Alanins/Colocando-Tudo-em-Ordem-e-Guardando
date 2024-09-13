import random

array = [random.randint(1, 100) for _ in range(15)]

for i in range(len(array)):
    c = i
    
    for j in range(i + 1, len(array)):
        if array[c] > array[j]:
            c = j
          
    if c != i:  # Verifica se houve troca
        array[i], array[c] = array[c], array[i]

print(array)