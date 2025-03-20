import tkinter as tk
from tkinter import messagebox

# Funções para os botões
def inserir():
    # Verificar se todos os campos estão preenchidos
    if not descricao_entry.get():
        messagebox.showwarning("Campo obrigatório", "O campo 'Descrição' deve ser preenchido.")
        descricao_entry.focus()
        return
    elif not validade_entry.get():
        messagebox.showwarning("Campo obrigatório", "O campo 'Validade' deve ser preenchido.")
        validade_entry.focus()
        return
    elif not segmento_entry.get():
        messagebox.showwarning("Campo obrigatório", "O campo 'Segmento' deve ser preenchido.")
        segmento_entry.focus()
        return
    elif not lote_entry.get():
        messagebox.showwarning("Campo obrigatório", "O campo 'Lote' deve ser preenchido.")
        lote_entry.focus()
        return
    elif not armazenamento_entry.get():
        messagebox.showwarning("Campo obrigatório", "O campo 'Armazenamento' deve ser preenchido.")
        armazenamento_entry.focus()
        return
    elif not fornecedor_entry.get():
        messagebox.showwarning("Campo obrigatório", "O campo 'Fornecedor' deve ser preenchido.")
        fornecedor_entry.focus()
        return
    elif not quantidade_entry.get():
        messagebox.showwarning("Campo obrigatório", "O campo 'Quantidade' deve ser preenchido.")
        quantidade_entry.focus()
        return

    # Exemplo de ação ao inserir
    print("Produto inserido!")
    messagebox.showinfo("Sucesso", "Produto inserido com sucesso!")

def pesquisar():
    print("Função de pesquisa acionada.")
    messagebox.showinfo("Pesquisar", "Função de pesquisa será implementada aqui.")

def alterar():
    print("Função de alterar acionada.")
    messagebox.showinfo("Alterar", "Função de alterar será implementada aqui.")

def excluir():
    print("Função de excluir acionada.")
    messagebox.showinfo("Excluir", "Função de excluir será implementada aqui.")

# Criar a janela principal
root = tk.Tk()
root.title("Cadastro de Produtos")
root.geometry("600x400")
root.resizable(False, False)  # Impedir redimensionamento da janela

# Criar os rótulos e os campos de entrada
descricao_label = tk.Label(root, text="Descrição:")
descricao_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
descricao_entry = tk.Entry(root, width=40)
descricao_entry.grid(row=0, column=1, padx=10, pady=5)

validade_label = tk.Label(root, text="Validade:")
validade_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
validade_entry = tk.Entry(root, width=40)
validade_entry.grid(row=1, column=1, padx=10, pady=5)

segmento_label = tk.Label(root, text="Segmento:")
segmento_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
segmento_entry = tk.Entry(root, width=40)
segmento_entry.grid(row=2, column=1, padx=10, pady=5)

lote_label = tk.Label(root, text="Lote:")
lote_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
lote_entry = tk.Entry(root, width=40)
lote_entry.grid(row=3, column=1, padx=10, pady=5)

armazenamento_label = tk.Label(root, text="Armazenamento:")
armazenamento_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
armazenamento_entry = tk.Entry(root, width=40)
armazenamento_entry.grid(row=4, column=1, padx=10, pady=5)

fornecedor_label = tk.Label(root, text="Fornecedor:")
fornecedor_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
fornecedor_entry = tk.Entry(root, width=40)
fornecedor_entry.grid(row=5, column=1, padx=10, pady=5)

quantidade_label = tk.Label(root, text="Quantidade:")
quantidade_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
quantidade_entry = tk.Entry(root, width=40)
quantidade_entry.grid(row=6, column=1, padx=10, pady=5)

# Criar os botões
botao_inserir = tk.Button(root, text="Inserir", width=15, command=inserir)
botao_inserir.grid(row=7, column=0, padx=10, pady=20)

botao_pesquisar = tk.Button(root, text="Pesquisar", width=15, command=pesquisar)
botao_pesquisar.grid(row=7, column=1, padx=10, pady=20)

botao_alterar = tk.Button(root, text="Alterar", width=15, command=alterar)
botao_alterar.grid(row=7, column=2, padx=10, pady=20)

botao_excluir = tk.Button(root, text="Excluir", width=15, command=excluir)
botao_excluir.grid(row=7, column=3, padx=10, pady=20)

# Iniciar a interface
root.mainloop()
