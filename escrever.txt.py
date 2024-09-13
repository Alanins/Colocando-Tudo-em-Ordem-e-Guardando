# a. Abra um arquivo de texto, ainda não existente, chamado "texto.txt" e o atribua a uma variável
with open("texto.txt", "w") as arquivo:
    
    # b. Crie uma lista usando a sintaxe: texto = list();
    texto = list()
    
    # c. Utilizando o método "append", atribua algumas frases para a lista;
    texto.append("Esta é a primeira frase.")
    texto.append("Aqui está a segunda frase.")
    texto.append("E esta é a terceira frase.")
    
    # d. Escreva, no arquivo aberto, o conteúdo da lista.
    for frase in texto:
        arquivo.write(frase + "\n")  # Adiciona uma nova linha após cada frase
