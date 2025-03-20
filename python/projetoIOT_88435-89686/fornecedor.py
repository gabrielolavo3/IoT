# Equipe: Andrei Vieira, Camile Oliveira, Gabriel Olavo e Renato Barreto
# Turma: 88435/89686 - Vespertino

from tkinter import *
from tkinter import messagebox

# Inicializando a janela principal
window = Tk()
window.title("Cadastro de Fornecedor")
window.geometry("1100x800+600+150")
#window.minsize(300, 300)
#window.maxsize(800, 800)
window.resizable(False, False)
window['bg'] = "CornflowerBlue"

# Métodos
def insercao():
    campos_vazios = []  # Lista para armazenar os campos vazios
    
    # Verificar cada campo
    if not inputNome.get().strip():
        campos_vazios.append("Nome")
    if not inputCNPJ.get().strip():
        campos_vazios.append("CNPJ")
    if not inputRazaoSocial.get().strip():
        campos_vazios.append("Razão Social")
    if not inputSegmento.get().strip():
        campos_vazios.append("Segmento")
    if not inputTelefoneFixo.get().strip():
        campos_vazios.append("Telefone Fixo")
    if not inputCelular.get().strip():
        campos_vazios.append("Celular")
    if not inputEmail.get().strip():
        campos_vazios.append("Email")
    if not inputLogradouro.get().strip():
        campos_vazios.append("Logradouro")
    if not inputBairro.get().strip():
        campos_vazios.append("Bairro")
    if not inputNumero.get().strip():
        campos_vazios.append("Número")
    if not inputCidade.get().strip():
        campos_vazios.append("Cidade")
    if not inputCEP.get().strip():
        campos_vazios.append("CEP")
    if not inputComplemento.get().strip():
        campos_vazios.append("Complemento")
    
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
titulo = Label(window, text="Cadastro de Fornecedor", font=("Arial", 16, "italic"))
titulo.grid(row=0, column=0, sticky="w", padx=10, pady=20, columnspan=6)

# Parte Fornecedor
subtitulo_fornecedor = Label(window, text="Por favor, informe os dados do fornecedor.", font=("Arial", 12, "bold"))
subtitulo_fornecedor.grid(row=1, column=0, sticky="w", padx=10, pady=10, columnspan=6)

labelNome = Label(window, text="Nome", font=("Arial", 12))
labelNome.grid(row=2, column=0, sticky="w", padx=10, pady=8)
inputNome = Entry(window, width=35)
inputNome.grid(row=2, column=1, padx=1, pady=5, sticky="w")

labelCNPJ = Label(window, text="CNPJ", font=("Arial", 12))
labelCNPJ.grid(row=2, column=2, sticky="w", padx=15, pady=8)
inputCNPJ = Entry(window, width=35)
inputCNPJ.grid(row=2, column=3, padx=1, pady=8, sticky="w")

labelRazaoSocial = Label(window, text="Razão Social", font=("Arial", 12))
labelRazaoSocial.grid(row=2, column=4, sticky="w", padx=30, pady=8)
inputRazaoSocial = Entry(window, width=35)
inputRazaoSocial.grid(row=2, column=5, padx=1, pady=8, sticky="w")

labelSegmento = Label(window, text="Segmento", font=("Arial", 12))
labelSegmento.grid(row=3, column=0, sticky="w", padx=10, pady=8)
inputSegmento = Entry(window, width=35)
inputSegmento.grid(row=3, column=1, padx=1, pady=8, sticky="w")

# Parte Contato
subtitulo_contato = Label(window, text="Por favor, informe os dados de contato.", font=("Arial", 12, "bold"))
subtitulo_contato.grid(row=4, column=0, sticky="w", padx=10, pady=20, columnspan=6)

labelTelefoneFixo = Label(window, text="Telefone Fixo", font=("Arial", 12))
labelTelefoneFixo.grid(row=5, column=0, sticky="w", padx=10, pady=8)
inputTelefoneFixo = Entry(window, width=35)
inputTelefoneFixo.grid(row=5, column=1, padx=1, pady=8, sticky="w")

labelCelular = Label(window, text="Celular", font=("Arial", 12))
labelCelular.grid(row=5, column=2, sticky="w", padx=15, pady=8)
inputCelular = Entry(window, width=35)
inputCelular.grid(row=5, column=3, padx=1, pady=8, sticky="w")

labelEmail = Label(window, text="Email", font=("Arial", 12))
labelEmail.grid(row=5, column=4, sticky="w", padx=30, pady=8)
inputEmail = Entry(window, width=35)
inputEmail.grid(row=5, column=5, padx=1, pady=8, sticky="w")

# Parte Endereço
subtitulo_endereco = Label(window, text="Por favor, informe os dados de endereço.", font=("Arial", 12, "bold"))
subtitulo_endereco.grid(row=6, column=0, sticky="w", padx=10, pady=20, columnspan=6)

labelLogradouro = Label(window, text="Logradouro", font=("Arial", 12))
labelLogradouro.grid(row=7, column=0, sticky="w", padx=10, pady=8)
inputLogradouro = Entry(window, width=35)
inputLogradouro.grid(row=7, column=1, padx=1, pady=8, sticky="w")

labelBairro = Label(window, text="Bairro", font=("Arial", 12))
labelBairro.grid(row=7, column=2, sticky="w", padx=15, pady=8)
inputBairro = Entry(window, width=35)
inputBairro.grid(row=7, column=3, padx=1, pady=8, sticky="w")

labelNumero = Label(window, text="Número", font=("Arial", 12))
labelNumero.grid(row=7, column=4, sticky="w", padx=30, pady=8)
inputNumero = Entry(window, width=35)
inputNumero.grid(row=7, column=5, padx=1, pady=8, sticky="w")

labelCidade = Label(window, text="Cidade", font=("Arial", 12))
labelCidade.grid(row=8, column=0, sticky="w", padx=10, pady=8)
inputCidade = Entry(window, width=35)
inputCidade.grid(row=8, column=1, padx=1, pady=8, sticky="w")

labelCEP = Label(window, text="CEP", font=("Arial", 12))
labelCEP.grid(row=8, column=2, sticky="w", padx=15, pady=8)
inputCEP = Entry(window, width=35)
inputCEP.grid(row=8, column=3, padx=1, pady=8, sticky="w")

labelComplemento = Label(window, text="Complemento", font=("Arial", 12))
labelComplemento.grid(row=8, column=4, sticky="w", padx=30, pady=8)
inputComplemento = Entry(window, width=35)
inputComplemento.grid(row=8, column=5, padx=1, pady=8, sticky="w")

# Botões
escolhaAcao = Label(window, text="Escolha uma ação clicando em um dos botões", font=("Arial", 12, "bold"))
escolhaAcao.grid(row=9, column=0, sticky="w", padx=10, pady=30, columnspan=6)

btnInserir = Button(window, text="Inserir", height=1, width=15, relief="groove", command=insercao)
btnInserir.grid(row=10, column=0, padx=10, pady=5)

btnAlterar = Button(window, text="Atualizar", height=1, width=15, relief="groove", command=alterar)
btnAlterar.grid(row=10, column=1, padx=10, pady=5)

btnPesquisar = Button(window, text="Pesquisar", height=1, width=15, relief="groove", command=pesquisar)
btnPesquisar.grid(row=10, column=2, padx=10, pady=5)

btnExcluir = Button(window, text="Excluir", height=1, width=15, relief="groove", command=exclusao)
btnExcluir.grid(row=10, column=3, padx=10, pady=5)

window.mainloop()
