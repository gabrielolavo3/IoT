# Exercício 17

# Biblioteca de operações matemáticas e do SO

import math
import os

# Dados e leitura

cobertura_por_litro = 6
latas_por_litro = 18
galao_por_litro = 3.6
preco_por_galao = 25
preco_por_lata = 80.00
margem_folga = 1.1

area_pintada = int(input("Informe o tamanho da área que deseja pintar: "))

# Calculos para lata e galão

litros = area_pintada / cobertura_por_litro
latas_necessarias = math.ceil(litros / latas_por_litro)
galoes_necessarios = litros / galao_por_litro
precoLata = latas_necessarias * preco_por_lata
precoGalao = galoes_necessarios * preco_por_galao

# Cálculo para compra mista

consumo_litro = (area_pintada / cobertura_por_litro) * margem_folga
galao_misto = consumo_litro / galao_por_litro
lata_misto = math.ceil((consumo_litro - galao_misto * galao_por_litro) / latas_por_litro)
precoMisto = (galao_misto * preco_por_galao) + (lata_misto * preco_por_lata)

# Impressão

os.system("cls")

while True:
    print ("Selecione o formato de compra")
    print ("1 - Lata de tinta")
    print ("2 - Galão de tinta")
    print ("3 - Compra mista")
    print ("4 - Sair")
    opcao = int(input("Informe a opção desejada: "))

    match opcao:
        case 1:
            print (f"Litros: {litros}")
            print (f"Lata de tinta: {latas_necessarias}")
            print (f"Preço da compra: R$ {precoLata:.2f}")
        
        case 2:
            print (f"Litros: {litros}")
            print (f"Galão de tinta: {galoes_necessarios}")
            print (f"Preço da compra: R$ {precoGalao:.2f}")
        
        case 3:
            print (f"Litros: {consumo_litro}")
            print (f"Galão de tinta: {galao_misto} | Lata de tinta: {lata_misto}")
            print (f"Preço da compra: R$ {precoMisto:.2f}")
        
        case _:
            print("Opção inválida!")
        
    if opcao == 4:
        print ("Programa encerrado")
        break