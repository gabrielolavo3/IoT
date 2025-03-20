# Equipe: Andrei Vieira, Camile Oliveira, Gabriel Olavo e Renato Barreto
# Turma: 88435/89686 - Vespertino

from tkinter import *
from tkinter import messagebox

# Função para validar todos os campos
def validar_campos():
    campos = {**campos_funcionario, **campos_contato, **campos_endereco}  # Combina todos os dicionários
    for label, entry in campos.items():
        if not entry.get():
            messagebox.showwarning("Campo obrigatório", f"O campo {label} deve ser preenchido.")
            entry.focus()
            return False
    return True

# Funções para botões
def inserir():
    if validar_campos():
        messagebox.showinfo("Inserção", "Dados inseridos com sucesso!")

def pesquisar():
    messagebox.showinfo("Pesquisar", "Função pesquisar acionada")

def alterar():
    messagebox.showinfo("Alterar", "Função alterar acionada")

def excluir():
    messagebox.showinfo("Excluir", "Função excluir acionada")


janela = Tk()
janela.title("Cadastro de Funcionários")
janela.geometry("1100x800+600+150")
janela.resizable(False, False)
janela['bg'] = "CornflowerBlue"

titulo = Label(janela, text="Cadastro de Funcionários", font=("Arial", 16, "italic"))
titulo.grid(row=0, column=0, sticky="w", padx=10, pady=20, columnspan=6)

subtitulo_funcionario = Label(janela, text="Informações do Funcionário", font=("Arial", 12, "bold"))
subtitulo_funcionario.grid(row=1, column=0, sticky="w", padx=10, pady=20, columnspan=6)

labels_funcionario = ["Nome", "CPF", "Cargo"]
campos_funcionario = {}

for i, (label, row, col) in enumerate(zip(labels_funcionario, [2, 2, 3], [0, 2, 0])):
    Label(janela, text=label + ":", font=("Arial", 12)).grid(row=row, column=col, sticky="w", padx=10, pady=8)
    entry = Entry(janela, width=35, font=("Arial", 12))
    entry.grid(row=row, column=col + 1, padx=10, pady=8)
    campos_funcionario[label] = entry

subtitulo_contato = Label(janela, text="Informações de Contato", font=("Arial", 12, "bold"))
subtitulo_contato.grid(row=4, column=0, sticky="w", padx=10, pady=20, columnspan=6)

labels_contato = ["Telefone", "Email", "WhatsApp"]
campos_contato = {}

for i, (label, row, col) in enumerate(zip(labels_contato, [5, 5, 6], [0, 2, 0])):
    Label(janela, text=label + ":", font=("Arial", 12)).grid(row=row, column=col, sticky="w", padx=10, pady=8)
    entry = Entry(janela, width=35, font=("Arial", 12))
    entry.grid(row=row, column=col + 1, padx=10, pady=8)
    campos_contato[label] = entry

subtitulo_endereco = Label(janela, text="Informações de Endereço", font=("Arial", 12, "bold"))
subtitulo_endereco.grid(row=7, column=0, sticky="w", padx=10, pady=20, columnspan=6)

labels_endereco = ["Logradouro", "Bairro", "Cidade", "Estado", "Número", "CEP"]
campos_endereco = {}

for i, (label, row, col) in enumerate(zip(labels_endereco, [8, 8, 9, 9, 10, 10], [0, 2, 0, 2, 0, 2])):
    Label(janela, text=label + ":", font=("Arial", 12)).grid(row=row, column=col, sticky="w", padx=10, pady=8)
    entry = Entry(janela, width=35, font=("Arial", 12))
    entry.grid(row=row, column=col + 1, padx=10, pady=8)
    campos_endereco[label] = entry

# Botões de Ações
escolhaAcao = Label(janela, text="Escolha uma ação clicando em um dos botões", font=("Arial", 12, "bold"))
escolhaAcao.grid(row=11, column=0, sticky="w", padx=10, pady=30, columnspan=6)

botoes = [
    ("Inserir", inserir),
    ("Pesquisar", pesquisar),
    ("Alterar", alterar),
    ("Excluir", excluir)
]

for i, (texto, comando) in enumerate(botoes):
    Button(janela, text=texto, font=("Arial", 12), width=15, relief="groove", command=comando).grid(row=12, column=i, padx=10, pady=5)

# Executar janela
janela.mainloop()
