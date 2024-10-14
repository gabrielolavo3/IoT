# Exercício 8

salarioHora = float(input("Informe qual o valor do seu salário-hora: "))
horasTrabalhadas = int(input("Informe sua carga horária semanal de trabalho: "))

salarioDoMes = salarioHora * horasTrabalhadas

print (f"Recebendo um salário-hora de R$ {salarioHora:.2f} por {horasTrabalhadas} horas semanais, o salário final é de R$ {salarioDoMes:.2f}")