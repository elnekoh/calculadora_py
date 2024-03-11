def sumar(n1, n2):
    return n1+n2

def restar(n1, n2):
    return n1-n2

def multiplicar(n1, n2):
    return n1*n2

def dividir(n1, n2):
    if n2!=0:
        return n1/n2
    else:
        print("no se puede dividir por cero!")
        return(None)

num1 = int(input("pone un numerito: "))
num2 = int(input("pone otro numerito: "))

resultado = dividir(num1,num2)

if resultado is not None:
    print(resultado)