from tkinter import *

window = Tk()
window.title("Text Area")

texto = Text(window,bg='light yellow',font=('Ink Free',12,'bold'),fg='blue',height=10,width=20,
             pady=20,padx=20) #pady/padx faz que o texto não fique colado nas bordas
texto.pack()

def enviar():
    print(texto.get('1.0',END))         #no .get tem que colocar o index '1.0' ou não funcionará, que faz pegar o primeiro indice.
                                        #depois basta colocar o END para pegar tudo até o final

botao = Button(window, text="Enviar", command=enviar,compound='bottom')
botao.pack()

window.mainloop()