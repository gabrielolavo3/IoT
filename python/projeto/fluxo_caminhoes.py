# Equipe: Andrei Vieira, Camile Oliveira, Gabriel Olavo e Renato Barreto
# Turma: 88435/89686 - Vespertino

from tkinter import *
from tkinter import messagebox

# Funções específicas para cada botão
def inserir_fluxo():
    if not validar_campos():
        return
    messagebox.showinfo("Inserir", "Registro inserido com sucesso!")

def pesquisar_fluxo():
    messagebox.showinfo("Pesquisar", "Função de pesquisa chamada!")

def alterar_fluxo():
    if not validar_campos():
        return
    messagebox.showinfo("Alterar", "Registro alterado com sucesso!")

def excluir_fluxo():
    messagebox.showinfo("Excluir", "Registro excluído com sucesso!")

def validar_campos():
    campos = {
        "ID Caminhão": id_caminhao_entry,
        "Carga": carga_entry,
        "Data/Hora Entrada": data_hora_entrada_entry,
        "Data/Hora Saída": data_hora_saida_entry,
        "Destino": destino_entry,
        "Proprietário": proprietario_entry,
        "Km Saída": km_saida_entry,
        "Km Retorno": km_retorno_entry
    }
    for campo, entry in campos.items():
        if not entry.get():
            messagebox.showwarning("Atenção", f"O campo '{campo}' deve ser preenchido.")
            entry.focus()
            return False
    return True

# Configuração da janela principal
root = Tk()
root.title("Fluxo de Caminhões")
root.geometry("1100x800+600+150")
root.resizable(False, False)
root['bg'] = "CornflowerBlue"

# Título
titulo = Label(root, text="Fluxo de Caminhões", font=("Arial", 16, "italic"))
titulo.grid(row=0, column=0, sticky="w", padx=10, pady=20, columnspan=6)

# Texto informativo para dados de fluxo
subtitulo_fluxo = Label(root, text="Por favor, informe os dados do fluxo de caminhões.", font=("Arial", 12, "bold"))
subtitulo_fluxo.grid(row=1, column=0, sticky="w", padx=10, pady=10, columnspan=6)

# Criação dos campos e rótulos
labels_entries = [
    ("ID Caminhão", "id_caminhao_entry"),
    ("Carga", "carga_entry"),
    ("Data/Hora Entrada", "data_hora_entrada_entry"),
    ("Data/Hora Saída", "data_hora_saida_entry"),
    ("Destino", "destino_entry"),
    ("Proprietário", "proprietario_entry"),
    ("Km Saída", "km_saida_entry"),
    ("Km Retorno", "km_retorno_entry"),
]

for i, (label, entry_name) in enumerate(labels_entries[:4]):
    lbl = Label(root, text=label + ":", font=("Arial", 12))
    lbl.grid(row=2 + i, column=0, sticky="w", padx=10, pady=8)
    ent = Entry(root, width=35)
    ent.grid(row=2 + i, column=1, padx=10, pady=8, sticky="w")
    globals()[entry_name] = ent

for i, (label, entry_name) in enumerate(labels_entries[4:]):
    lbl = Label(root, text=label + ":", font=("Arial", 12))
    lbl.grid(row=2 + i, column=2, sticky="w", padx=10, pady=8)
    ent = Entry(root, width=35)
    ent.grid(row=2 + i, column=3, padx=10, pady=8, sticky="w")
    globals()[entry_name] = ent

# Mensagem para selecionar ação
escolhaAcao = Label(root, text="Escolha uma ação clicando em um dos botões", font=("Arial", 12, "bold"))
escolhaAcao.grid(row=7, column=0, sticky="w", padx=10, pady=30, columnspan=6)

# Botões
botoes = [
    ("Inserir", inserir_fluxo),
    ("Pesquisar", pesquisar_fluxo),
    ("Alterar", alterar_fluxo),
    ("Excluir", excluir_fluxo)
]
for i, (texto, comando) in enumerate(botoes):
    Button(root, text=texto, height=1, width=15, relief="groove", command=comando).grid(row=8, column=i, padx=10, pady=5)

# Executa a janela
root.mainloop()
