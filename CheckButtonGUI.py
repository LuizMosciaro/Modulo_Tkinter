from tkinter import *

def printar():
    if(x.get())== 1:            #se não colocar o .get não funciona, só identifica o "else" e não o "if" (fica apenas Botão OFF)
        print('Botão ON')
    else:
        print('Botão OFF')

def printarstring():
    if(y.get())=='SIM':
        print('Botão String ON')
    else:
        print("Botão String OFF")

def printarboolean():
    if(z.get()):
        print('Botão Boolean ON')
    else:
        print("Botão Boolean OFF")


window = Tk()

x = IntVar() #integral que retornará
y = StringVar()
z = BooleanVar()

window.geometry('200x150')

melao = PhotoImage(file='bart1.png')
melao2 = PhotoImage(file='homer.png')
melao3 = PhotoImage(file='duf.png')

check_botao = Checkbutton(window,
                          text='Marque para ligar o botão',
                          variable= x, #variavel
                          onvalue=1,   #valor on (PODE SER QUALQUER VALOR)
                          offvalue=0,  #valor off (PODE SER QUALQUER VALOR)
                          command=printar,
                          image=melao,
                          compound='left'
                          )


check_botao.pack() #anchor = 'ancora' em algum lugar (n,ne,nw,center,s,se,sw)

check_botao2 = Checkbutton(window,
                          text='Marque para ligar o botão',
                          variable= y, #string
                          onvalue='SIM',
                          offvalue='NAO',
                          command=printarstring,
                          image=melao2,
                          compound='left'
                          )
check_botao2.pack()

check_botao3 = Checkbutton(window,
                          text='Marque para ligar o botão',
                          variable= z, #boolean
                          onvalue= True,
                          offvalue= False,
                          command=printarboolean,
                          image=melao3,
                          compound='left'
                          )
check_botao3.pack()




window.mainloop()