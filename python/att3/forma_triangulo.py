# Exercício 8

primeiroLado = int(input("Informe o primeiro lado do triângulo: "))
segundoLado = int(input("Informe o segundo lado do triângulo: "))
terceiroLado = int(input("Informe o terceiro lado do triângulo: "))

# Impressão

if primeiroLado == segundoLado and primeiroLado == terceiroLado:
    print ("É um triângulo equilátero")
elif primeiroLado != segundoLado and primeiroLado != terceiroLado and segundoLado != terceiroLado:
    print ("É um triângulo escaleno")
else:
    print ("É um triângulo isósceles")