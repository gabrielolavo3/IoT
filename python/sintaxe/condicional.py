# Estrutura de decisão ou condicional

"""
idade = int(input("Digite sua idade: "))

if idade > 17:
    print("Pode entrar na festa")
else:
    print("Não pode entrar na festa")
"""

# Número positivo, negativo e neutro

"""
num = int(input("Informe um número inteiro qualquer: "))

if num > 0:
    print ("Número é positivo")
elif num == 0:
    print ("Número neutro")
else:
    print("Número é negativo")
"""

# Par ou ímpar

"""
valor = int(input("Informe um número inteiro: "))

if valor % 2 == 0:
    print ("É par")
else:
    print ("É impar")
"""

# Ano bissexto

"""
ano = int(input("Digite um ano: "))

if  (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print ("O ano é bissexto")
else:
    print ("O ano não é bissexto")    
"""

# IMC

"""
peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))

imc = peso / pow(altura, 2)

if imc < 18.5:
    print ("\nVocê está abaixo do peso")
    
elif imc >= 18.5 and imc <= 24.9:
    print ("\nVocê está com peso normal")

else:
    print ("\nVocê está com exceso de peso")
"""

# Operador de divisão no python

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
print (numero1 / numero2) # divisão normal
print (numero1 // numero2) # retorna apenas o número inteiro da divisão

