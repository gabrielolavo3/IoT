# Exercício 3

nota1 = float(input("Informe a primeira nota: " ))
nota2 = float(input("Informe a segunda nota: " ))

media = (nota1 + nota2) / 2

if media >= 7 and media <= 10:
    print (f"Você está aprovado! Sua média foi {media:.2f}")
elif media >=5 and media < 7:
    print (f"Você está em recuperação! Sua média foi {media:.2f}")
else:
    print (f"Você está reprovado! Sua média foi {media:.2f}")
