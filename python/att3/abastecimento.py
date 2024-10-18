# Exercício 11

import os

print ("Tabela de combustíveis")
print ("1 - Gasolina (R$ 6,50)")
print ("2 - Álcool (R$ 5,00)")
combustivel = int (input("\nSelecione um combustivel para abastecer: "))

litro = float (input("Informe quantos litros deseja: "))

os.system("cls")

# Impressão

if combustivel == 1:
    valorFinal = litro * 6.50
    print (f"O valor do abastecimento é R$ {valorFinal:.2f}, para {litro:.2f} L de gasolina")
else:    
    valorFinal = (litro * 5) * 0.95
    print (f"O valor do abastecimento é R$ {valorFinal:.2f}, para {litro:.2f} L de álcool")