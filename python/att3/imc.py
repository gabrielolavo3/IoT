# Exercício 13

peso = float(input("Informe o seu peso (em Kg): "))
altura = float(input("Informe a sua altura (em m): "))

imc = peso / pow(altura, 2)

# Impressão

if imc < 18.5:
    print ("\nVocê está abaixo do peso")
    
elif imc >= 18.5 and imc <= 24.9:
    print ("\nVocê está com peso normal")

elif imc >= 25.0 and imc <= 29.9:
    print ("\nVocê está com excesso de peso")

else:
    print ("\nVocê está com obesidade")