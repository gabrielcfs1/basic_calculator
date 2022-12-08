## CALCULADORA SIMPLES ##

def sum( a ,  b ):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a, b):
    answer = a -b 
    print(str(a) + "-" + str(b) + "=" + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer))

while True:
    print("1 - SOMA ")
    print("2 - SUBTRAÇÃO ")
    print("3 - MULTIPLICAÇÃO ")
    print("4 - DIVISÃO ")
    print("5 - SAIR ")

    choice = input("ESCOLHA UMA DAS OPÇÕES: ")

    if choice == "1" :
        a = int(input("DIGITE O PRIMEIRO NÚMERO: "))
        b = int(input("DIGITE O SEGUNDO NÚMERO: "))
        sum = f'A SOMA DE  {a} + {b} É IGUAL A = {a + b} \n ' 
        print(sum)
    elif choice == "2" :
        a = int(input("DIGITE O PRIMEIRO NÚMERO: "))
        b = int(input("DIGITE O SEGUNDO NÚMERO: "))
        sub = f'A SUBTRAÇÃO DE  {a} - {b} É IGUAL A = {a - b} \n'
        print(sub)
    elif choice == "3" :
        a = int(input("DIGITE O PRIMEIRO NÚMERO: "))
        b = int(input("DIGITE O SEGUNDO NÚMERO: "))
        mul =  f'A MULTIPLICAÇÃO DE  {a} * {b} É IGUAL A = {a * b} \n'
        print(mul)
    elif choice == "4" :
        a = int(input("DIGITE O PRIMEIRO NÚMERO: "))
        b = int(input("DIGITE O SEGUNDO NÚMERO: "))
        div = f'A DIVISÃO DE  {a} / {b} É IGUAL A = {a / b:.0f} \n'
        print(div)
    elif choice == "5" :
        print("SAINDO...")
        quit()