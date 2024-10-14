# Exercício 16

# Biblioteca de operações matemáticas e do SO

import math
import os

# Dados e leitura

cobertura_por_litro = 3
latas_por_litro = 18
preco_por_lata = 80.00

area_pintada = int(input("Informe o tamanho da área que deseja pintar: "))

# Calculos

litros_necessarios = area_pintada / cobertura_por_litro
tintas_necessarias = math.ceil(litros_necessarios / latas_por_litro) # Math.ceil() arredondar um número para cima
precoFinal = tintas_necessarias * preco_por_lata

# Impressão

os.system("cls")

print ("Área a ser pintada:",area_pintada)
print (f"Litros de tinta: {litros_necessarios:.2f}")
print ("Quantidade de latas:",tintas_necessarias)
print (f"Preço final: {precoFinal:.2f}")