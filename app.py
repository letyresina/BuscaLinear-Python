# Variável necessária

lista = [3, 6, 7, 10, 4, 12, 9, 5, 8]

# Função
def buscaLinear(lista, numero):
    '''
        Função criada para buscar o número presene da lista através do valor informado pelo usuário
    '''
    for i in range(len(lista)):
        if lista[i] == numero:
            print(f"O indíce do número {numero} nessa lista é de {i}")
        

# Aplicativo principal 

numBuscado = int(input("Informe o número que deseja buscar na lista: ")) # Usuário escolhe qual número deseja buscar

buscaLinear(lista, numBuscado) # Resultado da busca com o print

