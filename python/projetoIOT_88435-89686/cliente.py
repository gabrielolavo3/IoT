# Equipe: Andrei Vieira, Camile Oliveira, Gabriel Olavo e Renato Barreto
# Turma: 88435/89686 - Vespertino

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def inserir():
    if not validar_campos():
        return
    messagebox.showinfo("Inserir", "Dados inseridos com sucesso!")

def pesquisar():
    messagebox.showinfo("Pesquisar", "Função pesquisar acionada")

def alterar():
    messagebox.showinfo("Alterar", "Função alterar acionada")

def excluir():
    messagebox.showinfo("Excluir", "Função excluir acionada")

def validar_campos():
    campos = [entry_nome, entry_cpf, entry_telefone, entry_email, entry_whatsapp, entry_logradouro, entry_bairro, entry_cidade, entry_estado, entry_numero, entry_cep]
    nomes_campos = ["Nome", "CPF", "Telefone", "Email", "WhatsApp", "Logradouro", "Bairro", "Cidade", "Estado", "Número", "CEP"]

    for i, campo in enumerate(campos):
        if not campo.get():
            messagebox.showwarning("Campo obrigatório", f"O campo {nomes_campos[i]} deve ser preenchido.")
            campo.focus()
            return False
    return True

# Configuração da janela principal
janela = Tk()
janela.title("Cadastro de Clientes")
janela.geometry("1100x800+600+150")
janela.resizable(False, False)
janela['bg'] = "CornflowerBlue"

# Título
titulo = Label(janela, text="Cadastro de Clientes", font=("Arial", 16, "italic"))
titulo.grid(row=0, column=0, sticky="w", padx=10, pady=20, columnspan=6)

# Texto informativo para dados do cliente
subtitulo_cliente = Label(janela, text="Por favor, informe os dados do cliente.", font=("Arial", 12, "bold"))
subtitulo_cliente.grid(row=1, column=0, sticky="w", padx=10, pady=10, columnspan=6)

# Criação e posicionamento dos campos
labels = ["Nome", "CPF", "Telefone", "Email", "WhatsApp", "Logradouro", "Bairro", "Cidade", "Estado", "Número", "CEP"]
entries = []

# Campos gerais do cliente
for i, (label, row, col) in enumerate(zip(labels[:2], [2, 2], [0, 2])):
    Label(janela, text=label + ":", font=("Arial", 12)).grid(row=row, column=col, sticky="w", padx=10, pady=8)
    entry = Entry(janela, width=35, font=("Arial", 12))
    entry.grid(row=row, column=col + 1, padx=10, pady=8)
    globals()[f'entry_{label.lower()}'] = entry
    entries.append(entry)

# Subtítulo para campos de contato
subtitulo_contato = Label(janela, text="Informe os dados de contato.", font=("Arial", 12, "bold"))
subtitulo_contato.grid(row=3, column=0, sticky="w", padx=10, pady=10, columnspan=6)

# Campos de contato
for i, (label, row, col) in enumerate(zip(labels[2:5], [4, 4, 5], [0, 2, 0])):
    Label(janela, text=label + ":", font=("Arial", 12)).grid(row=row, column=col, sticky="w", padx=10, pady=8)
    entry = Entry(janela, width=35, font=("Arial", 12))
    entry.grid(row=row, column=col + 1, padx=10, pady=8)
    globals()[f'entry_{label.lower()}'] = entry
    entries.append(entry)

# Subtítulo para campos de endereço
subtitulo_endereco = Label(janela, text="Informe os dados de endereço.", font=("Arial", 12, "bold"))
subtitulo_endereco.grid(row=6, column=0, sticky="w", padx=10, pady=10, columnspan=6)

# Campos de endereço
for i, (label, row, col) in enumerate(zip(labels[5:], [7, 7, 8, 8, 9, 9], [0, 2, 0, 2, 0, 2])):
    Label(janela, text=label + ":", font=("Arial", 12)).grid(row=row, column=col, sticky="w", padx=10, pady=8)
    entry = Entry(janela, width=35, font=("Arial", 12))
    entry.grid(row=row, column=col + 1, padx=10, pady=8)
    globals()[f'entry_{label.lower()}'] = entry
    entries.append(entry)

# Mensagem para selecionar ação
escolhaAcao = Label(janela, text="Escolha uma ação clicando em um dos botões", font=("Arial", 12, "bold"))
escolhaAcao.grid(row=10, column=0, sticky="w", padx=10, pady=30, columnspan=6)

# Criação e posicionamento dos botões
botoes = [("Inserir", inserir), ("Pesquisar", pesquisar), ("Alterar", alterar), ("Excluir", excluir)]
for i, (nome, comando) in enumerate(botoes):
    ttk.Button(janela, text=nome, command=comando).grid(row=11, column=i, padx=5, pady=10)

# Executa a janela
janela.mainloop()
