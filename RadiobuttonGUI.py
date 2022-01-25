from tkinter import *
#() = tupla(imutavel)
#[] = lista(modificavel)

food = ['Pizza','Frango','Drink'] #<<lista



win = Tk()
win.geometry('350x250')

pizza = PhotoImage(file='pizza.png')
frango = PhotoImage(file='galinha.png')
drink = PhotoImage(file='drink.png')
comidas = [pizza,frango,drink] #lista de caminhos das imagens

x = IntVar()

for index in range(len(food)):                          #range(len(listaqualquer)) faz enumerar os itens da lista
    botao_radio = Radiobutton(win,text=food[index],
                              variable=x,
                              value= index,             #colocar "onvalue=1,offvalue=0" não da certo!
                              font=('Impact',15),
                              image= comidas[index],     #associa o indice da imagem ao botão
                              compound='left',
                              

                              )
    botao_radio.pack()






win.mainloop()