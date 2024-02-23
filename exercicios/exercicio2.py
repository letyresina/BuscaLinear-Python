listaNum = []

# jeito tradicional
#listaNum.extend([2, 4, 6, 8, 10])
#print(listaNum)

# jeito automático
def adicionarPares(lista):
    numero = 0
    quantidade = 6
    while quantidade > 0:
        if numero % 2 == 0:
            lista.append(numero)
            quantidade -= 1
        numero += 1

adicionarPares(listaNum)

print(listaNum)
