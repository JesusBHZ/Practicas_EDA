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
v = int(input("Numero a multiplicar: "))
print(f"Tu resultado es: {suma(v,v)}")

"""
num = int(input("Ingresa un numero"))
def cuadrado(num,b):
    if b== num:
        return num
    else:
        b+=1
        return num+cuadrado(num,b)
print("El cuadrado es: ", cuadrado(num,1))

"""

