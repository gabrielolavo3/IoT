import os

print ("Digite o seu nome: ")
nome = input()
nota1 = float (input("Digite a 1ª nota: "))
nota2 = float (input("Digite a 2ª nota: "))

os.system("cls")
media = (nota1 + nota2) / 2

print (media)