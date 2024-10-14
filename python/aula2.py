nome = "Gabriel"
idade = 22
peso = 74

"""
# Impressão antiga
print ("My name is %s" %nome)
print ("%s tem %d anos de idade e %.2f de peso " %(nome,idade,peso))

#Impressão nova
print ("{} tem {} anos e {:.2f} Kg peso".format(nome, idade, peso))

#Impressão mais recente
print(f"{nome} tem {idade} anos e {peso:.2f} de peso")
"""

#Entrada de dados
print("Adoro megacavaleiro")
nome = input("Informe o seu nome: ")
idade = int(input("Informe a sua idade: "))
peso = float(input("Informe o seu peso: "))

print(f"{nome} tem {idade} anos e {peso:.2f} de peso")


