import random

numeros = []

for i in range(10):
    numeros.append(random.randint(1,50))

print(f"A lista aleatória é de {numeros}")
print(f"O maior número da lista é {max(numeros)}")
