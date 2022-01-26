#OBS:
#   widget = elementos do GUI: botões, imagens, textos
#   window = recipiente para abrigar widgets

from tkinter import *

window = Tk() #instancia uma janela, mas ainda não a mostra

window.geometry('300x300') #configura o tamanho da janela, em formato de string
window.title('Programa X - Kuiz Bosciaro') #titulo do programa

window_icon = PhotoImage(file='homer.png') #imagem do icone do programa, tem que formatar pra essa forma
window.iconphoto(True,window_icon) #associando a variavel icon para icone do programa

window.config(background="gray") #cor do fundo

label_icon = PhotoImage(file='duf.png')
label = Label(window,text='Duff Beer',
                      font=('Arial',18,'bold'),
                      fg='black', # cor da fonte do widget
                      bg='white', # cor do fundo do widget
                      padx=5,pady=5,   # espaçamento da borda do widget
                      relief='ridge',  # estilo da borda do widget
                      borderwidth=5,   # largura da borda DO WIDGET
                      image=label_icon,# imagem que eu escolhi para o widget label
                      compound='left') # = faz a imagem ficar ajustada ao texto (top,bottom,left,right) e sem isso fica em cima do texto
label.pack()  #adiciona o label no programa no centro
#label.place(x=150,y=50) #coloca o label em um local x/y determinado


contagem = 0
def click():
    global contagem     #defini que contagem agora é global
    contagem += 1
    if contagem <= 1:
        print('Você clicou no botão',contagem,'vez!')
    elif contagem > 1:
        print('Você clicou no botão', contagem, 'vezes!')

botao1_icon = PhotoImage(file='bart1.png')
botao1 = Button(window,
                text='Click',
                image=botao1_icon,
                compound='top',
                command=click, #executa o comando da função 'click' definida na linha 30
                font=("Times",12),
                bg='white',
                activebackground='white', #quando o botão for clicado fica da cor escolhida enquanto o mouse estiver pressionado
                activeforeground='gray')  #faz a fonte ficar da cor escolhida enquanto o mouse estiver pressionado
botao1.pack()



entry = Entry(window,                   # entry = uma caixa para escrever algo
              font=('Arial',11),
              width=200)
              #show='*')                 #show = vai mostrar apenas '*' no campo digitado

def imprimir_texto():
    usuario = entry.get() #.get = pegará o valor digitador no widget "entry" e ao apertar o botao_de_envio printa no console
    print('Olá',usuario)

botao_de_envio_texto = Button(window,text='Enviar',font=('Times',8),command=imprimir_texto)
botao_de_envio_texto.pack(side=RIGHT)   #side=RIGHT coloca na direita o widget

def deletar():
    delet = entry.delete(0,'end') #.delete = deletará o último digito / adicionando o ",'end'" = deleta tudo

botao_delete = Button(window,text="Deletar",font=("Arial",8),command=deletar, width=5)
botao_delete.pack(side=RIGHT)


def backspace():
    entry.delete(len(entry.get())-1, 'end') # o len -1 pega a contagem de digitos do widget entry e tira o ultimo.

botao_backspace = Button(window,text="BkSpace",font=("Arial",8),command=backspace,width=10)
botao_backspace.pack(side=RIGHT)


entry.pack(side=LEFT) #side=LEFT coloca na esquerda o widget

check_botao = Checkbutton(window,text='Checkbox')
check_botao.pack(anchor=NE)





window.mainloop() #esse comando faz mostrar a janela criada