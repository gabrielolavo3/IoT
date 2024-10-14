# Exercício 13

import os

altura = float(input("Informe a sua altura: "))

pesoFeminino = (72.7 * altura) - 58
pesoMasculino = (62.1 * altura) - 44.7

os.system("cls")

print (f"Com {altura:.2f} de altura, para o sexo feminino, o peso ideal é {pesoFeminino:.2f} Kg")
print (f"Com {altura:.2f} de altura, para o sexo masculino, o peso ideal é {pesoMasculino:.2f} Kg")