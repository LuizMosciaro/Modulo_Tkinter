from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg = 'gray',
                  font = ('Constantia',35),
                  width= 12,
                  selectmode=MULTIPLE, #Quando se adiciona isso, da erro! Então tem que mudar a função do botão "Enviar" linha 21

                  )

listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Hamburguer")
listbox.insert(3,"Pipoca")
listbox.insert(4,"Hotdog")
listbox.insert(5,"Churrasco")

def enviar():
    food = []
    if True:
        for index in listbox.curselection():            #Traduzindo: para cada variavel 'index' na seleção atual da listbox:
            food.insert(index, listbox.get(index))      #pegará o indice (que é 'index) e atribuirá o nome da listbox nele (listbox.get(index)
        for index in food:                              #Loop para printar a variavel "index"
            print("Você pediu: " + index)
    else:
        print("Nenhuma opção escolhida")

   #if listbox.curselection(): <<<Ta em comentario pois mudamos para "multiplas seleções" a listbox
         #print("Você pediu: ")
         #print(listbox.get(listbox.curselection())) #'.get' pega o item que selecionamos e printa, o item é o
                                               # 'current selection'(curselection), ou seja, pega a seleção atual e printa quando
                                               #clicarmos no botão "enviar"




novo_item = Entry(window)
novo_item.pack()

#Metodo abaixo já envia a ordem ao clicar em "add" :
#def add():
#    print("Você incluiu o item:")
#    print(novo_item.get())

#Esse metodo faz que o item da entrybox seja adicionado a listagem de itens:
def add():
    listbox.insert(listbox.size(),novo_item.get()) #.insert = coloca um novo item, aceita 2 argumentos
                                                   #.size = pega retorna o numero de linhas de uma listbox
                                                   #novo_item.get = pega a entrybox e coloca como ultimo item da lista
    listbox.config(height=listbox.size())          #ajusta o tamanho da lista ASSIM QUE CLICAR EM ADD

def delete(): #vou colocar trocar algumas linhas pois agora está em seleção multipla e não funcionará mais.
#    (listbox.delete(listbox.curselection()))
#    listbox.config(height=listbox.size())  # diminuirá o tamanho da lista ASSIM QUE CLICAR EM DELETE

    for index in reversed(listbox.curselection()):      #Traduzindo: Vai começar do maior 'index' até index 0 e deletar os selecionados
        listbox.delete(index)

add_item = Button(window,text='Adicionar Item',command=add)
add_item.pack()

delete_item = Button(window,text='Deletar Item',command=delete)
delete_item.pack()

botao_envio = Button(window,text='Enviar Pedido',command=enviar)
botao_envio.pack()



listbox.config(height=listbox.size()) #ajusta o tamanho da lista aos itens


window.mainloop()