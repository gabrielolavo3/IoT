# Equipe: Andrei Vieira, Camile Oliveira, Gabriel Olavo e Renato Barreto
# Turma: 88435/89686 - Vespertino

from tkinter import *
from tkinter import messagebox

# Inicializando a janela principal
window = Tk()
window.title("Cadastro de Caminhão")
window.geometry("1100x800+600+150")
#window.minsize(300, 300)
#window.maxsize(800, 800)
window.resizable(False, False)
window['bg'] = "CornflowerBlue"

# Métodos
def insercao():
    campos_vazios = []  # Lista para armazenar os campos vazios
    
    # Verificar cada campo
    if not inputModelo.get().strip():
        campos_vazios.append("Modelo")
    if not inputMarca.get().strip():
        campos_vazios.append("Marca")
    if not inputCor.get().strip():
        campos_vazios.append("Cor")
    if not inputPlaca.get().strip():
        campos_vazios.append("Placa")
    if not inputRenavam.get().strip():
        campos_vazios.append("Renavam")
    if not inputChassi.get().strip():
        campos_vazios.append("Chassi")
    if not inputCapacidade.get().strip():
        campos_vazios.append("Capacidade")
    
    # Exibir mensagem
    if campos_vazios:        
        messagebox.showwarning("Campos Vazios", "Os seguintes campos estão vazios:\n" + ", ".join(campos_vazios))
    else:
        messagebox.showinfo("Inserção", "Informação inserida com sucesso")

def pesquisar():
    messagebox.showinfo("Pesquisando informações!", "Efetuando a busca de dados")

def alterar():
    messagebox.showinfo("Alteração de informações!", "Concluindo a atualização de dados")

def exclusao():
    messagebox.showinfo("Removendo informações", "Exclusão permanente realizada com sucesso")

# Título do frame
titulo = Label(window, text="Cadastro de Caminhão", font=("Arial", 16, "italic"))
titulo.grid(row=0, column=0, sticky="w", padx=10, pady=20, columnspan=6)

# Texto informativo após o título
subtitulo = Label(window, text="Por favor, informe os dados do caminhão nos campos abaixo", font=("Arial", 12, "bold"))
subtitulo.grid(row=1, column=0, sticky="w", padx=10, pady=20, columnspan=6)

# Rótulo e caixa de entrada com grid (linhas e colunas)
labelModelo = Label(window, text="Modelo", font=("Arial", 12, "bold"))
labelModelo.grid(row=2, column=0, sticky="w", padx=10, pady=8)
inputModelo = Entry(window, width=35)
inputModelo.grid(row=2, column=1, padx=1, pady=5, sticky="w")

labelMarca = Label(window, text="Marca", font=("Arial", 12, "bold"))
labelMarca.grid(row=2, column=2, sticky="w", padx=15, pady=8)
inputMarca = Entry(window, width=35)
inputMarca.grid(row=2, column=3, padx=1, pady=8, sticky="w")

labelCor = Label(window, text="Cor", font=("Arial", 12, "bold"))
labelCor.grid(row=2, column=4, sticky="w", padx=30, pady=8)
inputCor = Entry(window, width=35)
inputCor.grid(row=2, column=5, padx=1, pady=8, sticky="w")

labelPlaca = Label(window, text="Placa", font=("Arial", 12, "bold"))
labelPlaca.grid(row=3, column=0, sticky="w", padx=10, pady=8)
inputPlaca = Entry(window, width=35)
inputPlaca.grid(row=3, column=1, padx=1, pady=8, sticky="w")

labelRenavam = Label(window, text="Renavam", font=("Arial", 12, "bold"))
labelRenavam.grid(row=3, column=2, sticky="w", padx=15, pady=8)
inputRenavam = Entry(window, width=35)
inputRenavam.grid(row=3, column=3, padx=1, pady=8, sticky="w")

labelChassi = Label(window, text="Chassi", font=("Arial", 12, "bold"))
labelChassi.grid(row=4, column=0, sticky="w", padx=10, pady=8)
inputChassi = Entry(window, width=35)
inputChassi.grid(row=4, column=1, padx=1, pady=8, sticky="w")

labelCapacidade = Label(window, text="Capacidade", font=("Arial", 12, "bold"))
labelCapacidade.grid(row=4, column=2, sticky="w", padx=15, pady=8)
inputCapacidade = Entry(window, width=35)
inputCapacidade.grid(row=4, column=3, padx=1, pady=8, sticky="w")

# Botões
escolhaAcao = Label(window, text="Escolha uma ação clicando em um dos botões", font=("Arial", 12, "bold"))
escolhaAcao.grid(row=5, column=0, sticky="w", padx=10, pady=30, columnspan=6)

btnInserir = Button(window, text="Inserir", height=1, width=15, relief="groove", command=insercao)
btnInserir.grid(row=6, column=0, padx=10, pady=5)

btnAlterar = Button(window, text="Atualizar", height=1, width=15, relief="groove", command=alterar)
btnAlterar.grid(row=6, column=1, padx=10, pady=5)

btnPesquisar = Button(window, text="Pesquisar", height=1, width=15, relief="groove", command=pesquisar)
btnPesquisar.grid(row=6, column=2, padx=10, pady=5)

btnExcluir = Button(window, text="Exclusão", height=1, width=15, relief="groove", command=exclusao)
btnExcluir.grid(row=6, column=3, padx=10, pady=5)

# Inicializando a interface Tkinter
window.mainloop()
