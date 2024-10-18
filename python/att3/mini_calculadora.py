# Exercício 12

import os

print ("Escolha uma operação disponível")
print ("+ : soma")
print ("- : subtração")
print ("* : multiplicação")
print ("/ : divisão")
operador = input("\nSelecione o operador matemático: ")

primeiroValor = float(input ("\nDigite o valor A: "))
segundoValor = float(input ("Digite o valor B: "))

os.system("cls")

# Impressão e cálculos

if operador == "+":
    print ("\nSoma:",primeiroValor + segundoValor)
elif operador == "-":
    print ("\nSubtração:",primeiroValor - segundoValor)
elif operador == "*":
    print ("\nMultiplicação:",primeiroValor * segundoValor)
else:    
    if primeiroValor == 0 or segundoValor == 0:
        print ("\nEssa operação de divisão não é válida por causa do algarismo 0!")
    else:
        print ("\nDivisão:",primeiroValor / segundoValor)