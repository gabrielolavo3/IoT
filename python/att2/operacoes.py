# Exercício 11
# Biblioteca para manipular o SO

import os

primeiroValor = int(input("Informe um número inteiro: "))
segundoValor = int(input("Informe outro número inteiro: "))
terceiroValor = float(input("Informe um número real: "))

produto = (primeiroValor * 2) * (segundoValor/2)
soma = (primeiroValor * 3) + terceiroValor
elevadoAoCubo = terceiroValor**3

# Limpando o console

os.system("cls")

print (f"produto do dobro do primeiro com metade do segundo: {produto:.2f}")
print (f"Soma do triplo do primeiro com o terceiro: {soma:.2f}")
print (f"Terceiro elevado ao cubo: {elevadoAoCubo:.2f}")