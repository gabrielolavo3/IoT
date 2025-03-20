primeiroValor = float(input("Digite o 1º número: "))
segundoValor = float(input("Digite o 2º número: "))
operacao = (input("Digite o sinal da operação (+,-,/,*): "))

if operacao == '+':
    resultado = primeiroValor + segundoValor

elif operacao == '-':
    resultado = primeiroValor - segundoValor

elif operacao == '*':
    resultado = primeiroValor * segundoValor

elif operacao == '/':
    resultado = primeiroValor / segundoValor

print ("Resultado da operação:", resultado)