def buscaLinear(array, n, x): # n = tamanho e o x é o alvo
    for i in range(0,n):
        if array[i] == x:
            return i # alvo encontrado -> retorna a posição
    return -1 # caso não encontre o alvo

array = [2, 4, 0, 1, 9]

n = len(array)

x = 1

resultado = buscaLinear(array, n, x)

if resultado != -1:
    print(f"Elemento encontrado na posição {resultado}")
    
else:
   print("Resultado não encontrado")