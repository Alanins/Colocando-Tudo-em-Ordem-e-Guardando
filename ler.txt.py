with open("loremipsum.txt", "r") as arquivo:
    conteudo = arquivo.read()

# Imprime na tela todo o conteúdo da variável
print("Conteúdo do arquivo:")
print(conteudo)

# Imprime na tela apenas a primeira linha do arquivo txt
primeira_linha = conteudo.splitlines()[0]
print("\nPrimeira linha do arquivo:")
print(primeira_linha)

# Imprime na tela apenas os 3 primeiros caracteres do arquivo txt
tres_primeiros_caracteres = conteudo[:3]
print("\nTrês primeiros caracteres do arquivo:")
print(tres_primeiros_caracteres)

# Abrir o arquivo text novamente
with open("loremipsum.txt", "r") as arquivo:
    conteudo_novo = arquivo.read()
    print("\nConteúdo do arquivo usando 'with':")
    print(conteudo_novo)
