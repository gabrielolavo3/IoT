import os

nota1 = float (input("Digite a 1ª nota: "))
nota2 = float (input("Digite a 2ª nota: "))

media = (nota1 * 2 + nota2 * 3)/(2+3)

os.system("cls")

print ("Sua média é", media)