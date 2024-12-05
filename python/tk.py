# Interface gráfica com Thinker

from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("My Windows")
janela.geometry("500x500") # tamanho da janela
janela.geometry("500x500+660+300") # posição da janela
janela.minsize(200,200) # tamanho minimo da janela
janela.maxsize(600,600) # tamanho maximo da janela
janela.resizable(False, False)
#janela.state("zoomed")  janela maximizada
#janela.state("iconic") janela minimizada
janela['bg'] = "pink" # muda a cor do background

def mensagemOne():
    texto = txtnome.get()
    print(texto)

def mensagemTwo():
    messagebox.showinfo("informação", "Mensagem de informação")
    messagebox.showwarning("Atenção", "Mensagem de atenção")
    messagebox.showerror("Erro", "Mensagem de erro")

# adicionar um label(rótulo)
nome = Label(janela, text = "Nome", font = "Arial 20 bold", fg = "blue")
nome.pack(pady=10)

# adicionar caixa de texto
txtnome = Entry(janela, font = "Arial 14", bg = "orange")
txtnome.pack(pady=20)

#adicionar um button
btn1 = Button(janela, text = "Clique aqui", font = "Arial 12", command = mensagemOne)
btn1.pack()
btn2 = Button(janela, text = "Clicar no red", bg = "purple", command = mensagemTwo)
btn2.pack(pady = 10)

janela.mainloop()
