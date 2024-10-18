# Exercício 10

produto = float(input("Informe o valor do produto (em R$): "))

# Impressão

if produto > 100:
    descontoProduto = produto * 0.90
    print (f"O produto recebeu um desconto, passando a custar R$ {descontoProduto:.2f}")
else:
    print (f"Produtos com valor igual ou menor a R$ 100 não recebem desconto no valor final!")