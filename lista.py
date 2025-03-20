# Listas

"""
# Lista básica
for i in "inconstitucionalissimamente":
    print(i)

# Lista de inteiros 
numeros = [1,2,3,4,5,6]
for x in numeros:
    print(x)

# Lista de Strings
personagem = ["Rainha Arqueira", "Princesa", "Bandida"]
for a in personagem:
    print(a)

# Tamanho de Array
lista = [1,2,3,4,5,6]
print(len(lista))


# Imprimir lista até o tamanho da lista
lista = [1,2,3,4]
x = 0

while x < len(lista):
    print(lista[x])
    x = x + 1

# Adicionando elemento no Array
lista = [5,6,3,7]
lista.append(0)
print(lista)

letras = ['a', 'e', 'i', 'o']
letras.append('u')
print(letras)

# Removendo elemento no Array
lista = [20, 30, 5, 15]
lista.remove(5)
print(lista)

# Removendo elemento pela indice no Array

# Comando pop
lista = [20, 30, 5, 15, 12]
lista.pop(3)
print(lista)

# Comando dell
lista = [20, 30, 5, 15, 12]
del lista[1]
print(lista)
"""

# Buscando um elemento na lista
lista = [15, 20, 30, 35, 45]


while True:
    p = int(input("Digite um numero: "))
    print("O número está na lista")
    break
else:
    print("O número não está na lista")
    chance = chance - 1
