from tkinter import *
from tkinter import messagebox



window = Tk()

label = Label(window,text='Esse é um botão chato de avisos',font=)
label.pack()


def click():
# 1   messagebox.showinfo(title= 'Caixa de Mensagem',message= 'Destruir o PC?') => Enviar uma mensagem popup

# 2  while True: #Faz uma mensagem chata sempre reaparecer até o código ser fechado
#        messagebox.showinfo(title= 'Caixa de Mensagem',message= 'Destruir o PC?')

# 3 messagebox.showerror(title="ERRO!",message="Algo deu muito errado no código!!!")

# 4 while True:
#       if messagebox.askokcancel(title="Ok ou Cancelar", message="Quer fazer algo?"):
#          print("Você fez algo")
#       else:
#          print("Você cancelou algo")

   while True:
    resposta = messagebox.askyesnocancel(title="Escolha alguma opção",message="Sim, Não ou Cancelar?")
    if resposta == True:
        print("Você escolheu o Sim")
    elif resposta == False:
        print("Você escolhou o Não")
    else:
        print("Você fugiu da pergunta!")





botao = Button(window,command=click,text='Clicar')
botao.pack()



window.mainloop()