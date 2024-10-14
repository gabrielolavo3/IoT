# Exercício 18

tamanho_arquivo = float(input("Digite o tamanho do arquivo, em MegaByte(MB): "))
velocidadeDownload= int(input("Digite a velocidade de download da sua internet, em Megabits(Mb/s): "))

tempoDownload = (tamanho_arquivo / (velocidadeDownload / 8)) / 60

print (f"O tempo de download é de {tempoDownload:.2f} minutos para um arquivo de {tamanho_arquivo:.2f} MB, baixando a {velocidadeDownload} Mb/s")