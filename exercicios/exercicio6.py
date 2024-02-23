import random

numeros = []

for i in range(10):
    numeros.append(random.randint(1,20))

print(numeros)

def maiorQue5(lista):
    contador = 0
    for i in lista:
        if i >= 5:
            contador +=1
    return contador

quantidade = maiorQue5(numeros)
print(f"A quantidade de numeros maior que 5 nessa lista é de {quantidade}")

