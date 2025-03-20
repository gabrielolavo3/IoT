import os

idVendedor = input("Digite o ID do vendedor: ")
codigoPeca = input("Digite o ID da peça adquirida: ")
precoUnitario = float(input("Digite o preço unitário da peça: "))
quantidade = int(input("Digite a quantidade: "))

valor = quantidade * precoUnitario
comissao = (valor * 5) / 100

os.system("cls")

print ("A comissão é do vendedor é", comissao)