# Exercício 15

import os

salarioHora = float(input("Informe qual o valor do seu salário-hora: "))
horasTrabalhadas = int(input("Informe sua carga horária semanal de trabalho: "))

salarioBruto = salarioHora * horasTrabalhadas

impostoDeRenda = (salarioBruto * 11) / 100
inss = (salarioBruto * 8) / 100
sindicato = (salarioBruto * 5) / 100
salarioLiquido = salarioBruto - (impostoDeRenda + inss + sindicato)

os.system("cls")

print (f"Salário bruto: R$ {salarioBruto:.2f}")
print (f"Desconto do INSS: R$ {inss:.2f}")
print (f"Desconto do Imposto de Renda: R$ {impostoDeRenda:.2f}")
print (f"Desconto do Sindicato: R$ {sindicato:.2f}")
print (f"\nSalário líquido: R$ {salarioLiquido:.2f}")