# Equipe: Andrei Vieira, Camile Oliveira, Gabriel Olavo e Renato Barreto
# Turma: 88435/89686 - Vespertino

from tkinter import *
from tkinter import messagebox

# Funções específicas para cada botão
def inserir():
    for field, entry in campos.items():
        if not entry.get():
            messagebox.showwarning("Campo Obrigatório", f"O campo '{field}' deve ser preenchido.")
            entry.focus()
            return
    messagebox.showinfo("Sucesso", "Produto inserido com sucesso!")

def pesquisar():
    messagebox.showinfo("Pesquisar", "Função de pesquisa chamada.")

def alterar():
    messagebox.showinfo("Alterar", "Função de alteração chamada.")

def excluir():
    messagebox.showinfo("Excluir", "Função de exclusão chamada.")

# Configuração da janela
janela = Tk()
janela.title("Cadastro de Produtos")
janela.geometry("1100x800+600+150")
janela.resizable(False, False)
janela['bg'] = "CornflowerBlue"

# Título
titulo = Label(janela, text="Cadastro de Produtos", font=("Arial", 16, "italic"))
titulo.grid(row=0, column=0, sticky="w", padx=10, pady=20, columnspan=6)

# Texto informativo para dados do produto
subtitulo_produto = Label(janela, text="Por favor, informe os dados do produto.", font=("Arial", 12, "bold"))
subtitulo_produto.grid(row=1, column=0, sticky="w", padx=10, pady=10, columnspan=6)

# Dicionário para armazenar campos e entradas
campos = {}

# Criação dos campos de entrada
labels = ["Descrição", "Validade", "Lote", "Armazenamento", "Segmento", "Fornecedor", "Quantidade"]
entries = []

# Organizamos os campos de entrada em linhas e colunas
for i, (label, row, col) in enumerate(zip(labels[:6], [2, 2, 3, 3, 4, 4], [0, 2, 0, 2, 0, 2])):
    Label(janela, text=label + ":", font=("Arial", 12)).grid(row=row, column=col, sticky="w", padx=10, pady=8)
    entry = Entry(janela, width=35, font=("Arial", 12))
    entry.grid(row=row, column=col + 1, padx=10, pady=8)
    campos[label] = entry

# Último campo "Quantidade"
Label(janela, text=labels[6] + ":", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=10, pady=8)
entry = Entry(janela, width=35, font=("Arial", 12))
entry.grid(row=5, column=1, padx=10, pady=8)
campos[labels[6]] = entry

# Mensagem para selecionar ação
escolhaAcao = Label(janela, text="Escolha uma ação clicando em um dos botões", font=("Arial", 12, "bold"))
escolhaAcao.grid(row=6, column=0, sticky="w", padx=10, pady=30, columnspan=6)

# Botões
botoes = [
    ("Inserir", inserir),
    ("Pesquisar", pesquisar),
    ("Alterar", alterar),
    ("Excluir", excluir),
]

for i, (texto, comando) in enumerate(botoes):
    Button(janela, text=texto, font=("Arial", 12), width=15, relief="groove", command=comando).grid(row=7, column=i, padx=10, pady=5)

# Execução da janela
janela.mainloop()
