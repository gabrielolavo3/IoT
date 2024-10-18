# Exercício 2

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

if valor1 > valor2:
    print (f"{valor1} é maior do que {valor2}")
elif valor2 > valor1:
    print (f"{valor2} é maior do que {valor1}")
else:
    print ("São iguais!")
