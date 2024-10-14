# Exercício 14

pesoPeixe = float(input("Informe o peso de peixes colhidos na atual pesca: "))
excesso = pesoPeixe - 50
multa = excesso * 4

print (f"\nCom a coleta de {pesoPeixe:.2f} Kg de peixe, há o excesso de peso de {excesso:.2f} Kg além do estabelecido. A multa aplicada é de R$ {multa:.2f}")