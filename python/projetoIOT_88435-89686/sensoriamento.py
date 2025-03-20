# Equipe: Andrei Vieira, Camile Oliveira, Gabriel Olavo e Renato Barreto
# Turma: 88435/89686 - Vespertino

from tkinter import *
from tkinter import messagebox

# Funções para ações de sensoriamento
def inserir_sensoriamento():
    if not validar_campos():
        return
    messagebox.showinfo("Inserir", "Registro inserido com sucesso!")

def pesquisar_sensoriamento():
    messagebox.showinfo("Pesquisar", "Função de pesquisa chamada!")

def alterar_sensoriamento():
    if not validar_campos():
        return
    messagebox.showinfo("Alterar", "Registro alterado com sucesso!")

def excluir_sensoriamento():
    messagebox.showinfo("Excluir", "Registro excluído com sucesso!")

def validar_campos():
    campos = {
        "ID Sensoriamento": id_sensoriamento_entry,
        "Data": data_entry,
        "Temperatura": temperatura_entry,
        "Luminosidade": luminosidade_entry,
        "Gás": gas_entry,
        "Presença": presenca_entry
    }
    for campo, entry in campos.items():
        if not entry.get():
            messagebox.showwarning("Atenção", f"O campo '{campo}' deve ser preenchido.")
            entry.focus()
            return False
    return True

# Configuração da janela
root = Tk()
root.title("Sensoriamento")
root.geometry("1100x800+600+150")
root.resizable(False, False)
root['bg'] = "CornflowerBlue"

# Título
titulo = Label(root, text="Sistema de Sensoriamento", font=("Arial", 16, "italic"))
titulo.grid(row=0, column=0, sticky="w", padx=10, pady=20, columnspan=6)

# Texto informativo para dados do sensoriamento
subtitulo_sensoriamento = Label(root, text="Por favor, informe os dados de sensoriamento.", font=("Arial", 12, "bold"))
subtitulo_sensoriamento.grid(row=1, column=0, sticky="w", padx=10, pady=10, columnspan=6)

# Labels e Entries para os campos de sensoriamento
id_sensoriamento_label = Label(root, text="ID Sensoriamento", font=("Arial", 12))
id_sensoriamento_label.grid(row=2, column=0, sticky="w", padx=10, pady=8)
id_sensoriamento_entry = Entry(root, width=35)
id_sensoriamento_entry.grid(row=2, column=1, padx=1, pady=5, sticky="w")

data_label = Label(root, text="Data", font=("Arial", 12))
data_label.grid(row=2, column=2, sticky="w", padx=15, pady=8)
data_entry = Entry(root, width=35)
data_entry.grid(row=2, column=3, padx=1, pady=8, sticky="w")

temperatura_label = Label(root, text="Temperatura", font=("Arial", 12))
temperatura_label.grid(row=2, column=4, sticky="w", padx=30, pady=8)
temperatura_entry = Entry(root, width=35)
temperatura_entry.grid(row=2, column=5, padx=1, pady=8, sticky="w")

luminosidade_label = Label(root, text="Luminosidade", font=("Arial", 12))
luminosidade_label.grid(row=3, column=0, sticky="w", padx=10, pady=8)
luminosidade_entry = Entry(root, width=35)
luminosidade_entry.grid(row=3, column=1, padx=1, pady=8, sticky="w")

gas_label = Label(root, text="Gás", font=("Arial", 12))
gas_label.grid(row=3, column=2, sticky="w", padx=15, pady=8)
gas_entry = Entry(root, width=35)
gas_entry.grid(row=3, column=3, padx=1, pady=8, sticky="w")

presenca_label = Label(root, text="Presença", font=("Arial", 12))
presenca_label.grid(row=3, column=4, sticky="w", padx=30, pady=8)
presenca_entry = Entry(root, width=35)
presenca_entry.grid(row=3, column=5, padx=1, pady=8, sticky="w")

# Mensagem para selecionar ação
escolhaAcao = Label(root, text="Escolha uma ação clicando em um dos botões", font=("Arial", 12, "bold"))
escolhaAcao.grid(row=4, column=0, sticky="w", padx=10, pady=30, columnspan=6)

# Botões
botoes = [
    ("Inserir", inserir_sensoriamento),
    ("Pesquisar", pesquisar_sensoriamento),
    ("Alterar", alterar_sensoriamento),
    ("Excluir", excluir_sensoriamento)
]
for i, (nome, comando) in enumerate(botoes):
    Button(root, text=nome, height=1, width=15, relief="groove", command=comando).grid(row=5, column=i, padx=10, pady=5)

# Loop da aplicação
root.mainloop()
