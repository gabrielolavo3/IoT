# Equipe: Andrei Vieira, Camile Oliveira, Gabriel Olavo e Renato Barreto
# Turma: 88435/89686 - Vespertino

from tkinter import *
from tkinter import messagebox

# Funções específicas para cada botão
def inserir():
    if not validar_campos():
        return
    messagebox.showinfo("Ação Executada", "Adicionado com sucesso")

def pesquisar():
    messagebox.showinfo("Ação Executada", "Botão Pesquisar clicado")

def alterar():
    if not validar_campos():
        return
    messagebox.showinfo("Ação Executada", "Alterado com sucesso")

def excluir():
    if not validar_campos():
        return
    messagebox.showinfo("Ação Executada", "Excluído com sucesso")

def validar_campos():
    if not entry_data.get():
        mensagem_erro("Data")
        entry_data.focus()
        return False
    if not entry_servico.get():
        mensagem_erro("Serviço")
        entry_servico.focus()
        return False
    if not entry_id_produto.get():
        mensagem_erro("ID do Produto")
        entry_id_produto.focus()
        return False
    if not entry_id_caminhao.get():
        mensagem_erro("ID do Caminhão")
        entry_id_caminhao.focus()
        return False
    if not entry_id_funcionario.get():
        mensagem_erro("ID do Funcionário")
        entry_id_funcionario.focus()
        return False
    return True

def mensagem_erro(campo):
    messagebox.showwarning("Campo Obrigatório", f"O campo '{campo}' deve ser preenchido.")

# Configuração da janela principal
janela = Tk()
janela.title("Cadastro de Manutenção")
janela.geometry("1100x800+600+150")
janela.resizable(False, False)
janela['bg'] = "CornflowerBlue"

# Título
titulo = Label(janela, text="Cadastro de Manutenção", font=("Arial", 16, "italic"))
titulo.grid(row=0, column=0, sticky="w", padx=10, pady=20, columnspan=6)

# Texto informativo para dados da manutenção
subtitulo_manutencao = Label(janela, text="Por favor, informe os dados da manutenção.", font=("Arial", 12, "bold"))
subtitulo_manutencao.grid(row=1, column=0, sticky="w", padx=10, pady=10, columnspan=6)

# Criação dos campos e rótulos
label_data = Label(janela, text="Data:", font=("Arial", 12))
label_data.grid(row=2, column=0, sticky="w", padx=10, pady=8)
entry_data = Entry(janela, width=35)
entry_data.grid(row=2, column=1, padx=10, pady=8, sticky="w")

label_servico = Label(janela, text="Serviço:", font=("Arial", 12))
label_servico.grid(row=2, column=2, sticky="w", padx=15, pady=8)
entry_servico = Entry(janela, width=35)
entry_servico.grid(row=2, column=3, padx=10, pady=8, sticky="w")

label_id_produto = Label(janela, text="ID do Produto:", font=("Arial", 12))
label_id_produto.grid(row=3, column=0, sticky="w", padx=10, pady=8)
entry_id_produto = Entry(janela, width=35)
entry_id_produto.grid(row=3, column=1, padx=10, pady=8, sticky="w")

label_id_caminhao = Label(janela, text="ID do Caminhão:", font=("Arial", 12))
label_id_caminhao.grid(row=3, column=2, sticky="w", padx=15, pady=8)
entry_id_caminhao = Entry(janela, width=35)
entry_id_caminhao.grid(row=3, column=3, padx=10, pady=8, sticky="w")

label_id_funcionario = Label(janela, text="ID do Funcionário:", font=("Arial", 12))
label_id_funcionario.grid(row=4, column=0, sticky="w", padx=10, pady=8)
entry_id_funcionario = Entry(janela, width=35)
entry_id_funcionario.grid(row=4, column=1, padx=10, pady=8, sticky="w")

# Mensagem para selecionar ação
escolhaAcao = Label(janela, text="Escolha uma ação clicando em um dos botões", font=("Arial", 12, "bold"))
escolhaAcao.grid(row=5, column=0, sticky="w", padx=10, pady=30, columnspan=6)

# Criação dos botões
botoes = [
    ("Inserir", inserir),
    ("Pesquisar", pesquisar),
    ("Alterar", alterar),
    ("Excluir", excluir)
]
for i, (texto, comando) in enumerate(botoes):
    Button(janela, text=texto, height=1, width=15, relief="groove", command=comando).grid(row=6, column=i, padx=10, pady=5)

# Executa a janela
janela.mainloop()
