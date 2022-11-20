
"""def cuenta_atra(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_atra(numero)
    else:
        print("Hola")
    print(f"Orden de liberacion: {numero}")
        
#cuenta_atra(10)

def fac(numero):
    if numero > 1:
        numero = numero * fac(numero-1)
    return numero
print(fac(5))"""

def suma(numero):
    if numero == 1:
        return 1
    else:
        return numero + suma(numero-1)
"""
5 + 10 = 15
4 + 6
3 + 3
2 + 1
1 
"""
    
print(suma(5))

# 1.- Caso base (cuando detener la llamada recursiva)
# 2.- El trabajo que hay que hacer para llegar a el caso base
# 3.- La llama recursiva

# Numero del n a 10
def suma(numero):
    if numero > 10:
        return
    print(numero)
    suma(numero+1)
suma(3)

"""
5 + 10 = 15
4 + 6
3 + 3
2 + 1
1 
"""
# 1 2 3 4 5 6 7 8 9 10


# 1.- Caso base (cuando detener la llamada recursiva)
# 2.- El trabajo que hay que hacer para llegar a el caso base
# 3.- La llama recursiva

#  Multiplicacion 
def suma(numero,num):
    if numero <= 0:
        return
    # print("numero: ",numero)
    suma(numero-1,num)
    
    # print("num: ",num)
    global c 
    c = c+num
    return c 
c = 0
print(suma(4,4))

palabra_secreta = "python"
counter = 0

while True:
    palabra = input("Ingresa la palabra secreta: ").lower()
    counter = counter + 1
    if palabra == palabra_secreta:
        break
    if palabra != palabra_secreta and counter > 7: 
        break