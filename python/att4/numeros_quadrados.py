import os # Biblioteca do limpatela

numero1 = float(input("Digite o 1º número: "))
numero2 = float(input("Digite o 2º número: "))
numero3 = float(input("Digite o 3º número: "))
numero4 = float(input("Digite o 4º número: "))

os.system("cls") # Limpatela
calculo = (numero1**2) + (numero2**2) + (numero3**2) + (numero4**2)

print ("Soma dos número ao quadrado:", calculo)