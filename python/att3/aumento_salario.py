# Exercício 9

salario = float(input("Informe o valor atual do seu salário (em R$): "))

if salario < 1000:
    aumentoSalario = salario * 1.01
else:
    aumentoSalario = salario * 1.005

# Impressão

print (f"Seu salário aumentou para R$ {aumentoSalario:.2f}")