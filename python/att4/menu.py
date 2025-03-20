print ("Escolha uma opção:")

for G in range(1,4):
    print (G,"- Opção", G)

opcao = int(input("Digite a opção desejada: "))

match opcao:
    case 1:
        print ("Você selecionou Assinha de Frango")
    case 2:
        print ("Você selecionou Carne bovina")
    case 3:
        print ("Sair")
    case _:
        print("Opção inválida")