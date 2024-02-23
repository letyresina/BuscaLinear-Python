meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
         "Novembro", "Dezembro")

print(f"O terceiro mês do ano é: {meses[2]}")

print(f"Do segundo mês ao quarto, são os meses: {meses[1:5]}")

frutas = ["Maça", "Banana", "Morango"]

print(frutas)

frutas.extend(["Abacaxi", "Uva"])
del frutas[1]

print(f"A lista atualizada: {frutas}")

numeros = []

numeros.extend([1, 2, 3, 4, 5])
print(numeros)

numeros.remove(3)
print(f"Lista de números atualizada: {numeros}")

lista1 = [2, 4, 6]
lista2 = [8, 10, 12]

listaConcatenada = lista1 + lista2
print(f"Concatenando listas: {listaConcatenada}")

numeros = list(range(1,11))
print(numeros)

#print(f"Números de 1 a 6: {numeros[2:6]}")

#print(f"Números do primeiro ao quinto, saltando de 2 em 2: {numeros[:5:2]}")
