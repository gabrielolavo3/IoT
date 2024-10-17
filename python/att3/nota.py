# Exercício 5

nota = float(input("Informe uma nota entre 0 e 10: " ))

if nota >= 7 and nota <= 10:
    print ("Você está aprovado!")
elif nota >= 4 and nota < 7:
    print ("Você está em recuperação!")
else:
    print ("Você está reprovado!")
