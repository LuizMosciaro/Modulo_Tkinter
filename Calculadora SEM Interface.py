while True:
    try:
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        resposta = float(input("Qual operação matemática quer realizar?"))

        if resposta==1:
            x = float(input("Qual o primeiro número? "))
            y = float(input("Qual o segundo número? "))
            print("A resposta é: " +str(x+y))
            print()

        if resposta==2:
            x = float(input("Qual o primeiro número? "))
            y = float(input("Qual o segundo número? "))
            print("A resposta é: " +str(x-y))
            print()

        if resposta==3:
            x = float(input("Qual o primeiro número? "))
            y = float(input("Qual o segundo número? "))
            print("A resposta é: " +str(x*y))
            print()

        if resposta==4:
            x = float(input("Qual o primeiro número? "))
            y = float(input("Qual o segundo número? "))
            print("A resposta é: " +str(x/y))
            print()


    except:
        print(" ")
        print("Valor inserido inválido")
        print("Retornando ao menu inicial...")
        print("__________________")