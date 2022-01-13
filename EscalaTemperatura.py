from tkinter import *

def enviar():
    print('Está fazendo', str(escala.get()),'graus Celsius')


window = Tk()
window.geometry('300x250')

termoicon = PhotoImage(file='temp.png')
label1 = Label(window,text='Termômetro',image=termoicon,compound='bottom')
label1.pack()

foguinho = PhotoImage(file='fire.png')
label2 = Label(window,image=foguinho)
label2.pack(anchor="e")

escala = Scale(window,cursor='sb_h_double_arrow',
               from_='-50',to='50',         #de onde até onde
               orient=HORIZONTAL,           #orientação
               length=500,                  #tamanho
               resolution = 5,              #de quanto em quanto incrementa a barra
               troughcolor='gray',          #cor da barra
               tickinterval=10,              #mostra os numeros de dez em dez
               bg= 'black',
               fg='white'
               )
escala.pack()

friozin = PhotoImage(file='cold.png')
label3 = Label(window,image=friozin)
label3.pack(anchor="w")

botao = Button(window, text='Enviar',command=enviar)
botao.pack()

window.mainloop()
