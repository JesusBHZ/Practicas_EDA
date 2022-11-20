# Programa que permite generar una tabla de multiplicar


def suma(numero, num, val):
  if numero == 0:
    return
  suma(numero - 1, num, val)

  # print("num: ",num)
  global c
  c = c + num
  print(val, " * ", numero, " = ", c)
  return c


c = 0
a = 10
y = int(input("Tabla a multiplicar: "))
d = y

suma(a, y, d)
"""
---- PSEUDOCODIGO -----
procedimiento suma(num,num,val)
    // lo siguiente se hara por cada vuelta hasta que numero sea igual a 0
    SI numero == 0 entonces:
        no regreses nada
    END IF   
    procedimiento suma(numero-1,num,val)
    // hace la cuenta hacia atras (el numero de vueltas que debe dar) 
    c //llamamos a la variable global c que sirve como acumulador

    c = c+num // suma de el numero por cada vuelta

    ESCRIBIR "numero, " * ", val, " = ", c" //imprime el valor de numero el cual se decrementa en 1, despues el valor de val que solo sirve para guardar el valor inicial, despues imprime c, el cual es el acumulador
    return c // regresa c

FIN PROCEDIMIENTO
c = 0 // declaramos c con un valor inicial de 0
a = 10 // declaramos a con un valor inicial de 10, el cual se ira decrementando

ESCRIBIR "Tabla a multiplicar: "
LEER (y)
d = y // declaramos d que valdra igual que y
FIN ALGORTIMO


------ EXPLICACION DE FUNCIONABILIDAD -------- 
Tabla a multiplicar(y): 4

VUELTAS (y)     |   sumatoria(c)  | impresion
1               |   4 (4+0)       | 1*4 = 4
2               |   8 (8+4)       | 2*4 = 8
3               |   12 (12+4)      | 3*4 = 12
4               |   16(16+4)       | 4*4 = 16
5               |   20(20+4)       | 5*4 = 20
6               |   24(24+4)       | 6*4 = 24
7               |   28(28+4)       | 7*4 = 28
8               |   32(32+4)       | 8*4 = 32
9               |   36(36+4)       | 9*4 = 36
10              |   40(40+0)       | 10*4 = 40

"""
