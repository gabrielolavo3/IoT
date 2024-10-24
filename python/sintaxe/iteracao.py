#ESTRUTURAS DE REPETIÇÃO

#WHILE
"""
x = 0
while x <= 10:
    print (x)
    x = x + 1
    
#loop infinito
x = 1
while True:
    print (x)

#outro loop infinito
x = 1
while x ==1:
    print (x)

#tabuada de adição
n = int (input ("Digite um numero: "))
x = 1
while x <= 10:
    print (n * x)
    x = x + 1

#atributos especiais
+=
-=
*=
/=
**=

#Interromper um while

x = 1
while x <= 10:
    if x == 5:
        break
    print (x)
    x = x + 1


#ESTRUTURA DE REPETIÇÃO FOR

#for simples
for i in range(6):
    print (i)

#Range delimitado
for i in range(1,6):
    print (i)
   

for char in "Vanessa":
    print (char)


#exemplo de for em uma lista (vetor)

lista = [1,2,3,4,5]
for i in lista:
    print(i)


computador = ['processador', 'memoria', 'SSD']
for i in computador:
    print (i)
"""

#somar numeros e exibir no final da repetição
x = 0
while True:
    num = int (input ("Digite um número: "))
    if num == 0:
        break
    x = x + num
print (x)