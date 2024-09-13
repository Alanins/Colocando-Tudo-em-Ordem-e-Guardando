# Criando o array de strings
dados = [
    {
    "Nome: Ana Clara",
    "dataNascimento: 20/01/1990",
    "CPF: 088.888.888-88",
    "RG: 9.584.147"
    },
    {
    "Nome: Marcelo Alves",
    "dataNascimento: 20/06/1998",
    "CPF: 456.845.785-00",
    "RG:7.547.156"

    },
    {
    "Nome: Bruna Silva",
    "dataNascimento: 07/07/1995",
    "CPF: 123.874.987-02",
    "RG: 2.514.789"
    }
]

# Ordenando de forma decrescente
dados.sort(key=None, reverse=True)

# Exibindo o resultado
print(dados)