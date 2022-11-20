# Programa que permite generar un rango de tablas de multiplicar


def suma(numero, num, val, num2, num3):
  global c
  if val > num2:
    print()
    return
  if numero == 0:
    print()
    suma(10, num3 + 1, val + 1, num2, num3 + 1)
    c =0
  if numero == 0:
    print()
    return
  suma(numero - 1, num, val, num2, num3)
  # print("num: ",num)
  c = c + num
  print(val, " * ", numero, " = ", c)
  return c


c = 0
a = 10
y = int(input("Tabla a multiplicar 1: "))
y2 = int(input("Tabla a multiplicar 2: "))

d = y

suma(a, y, d, y2, y)


"""
---- PSEUDOCODIGO -----
procedimiento suma(num,num,val,num2,num3)
    c //llamamos a la variable global c que sirve como acumulador
    // lo siguiente se hara por cada vuelta hasta que numero sea igual a 0
    SI val es mayor que num2 entonces:
    ESCRIBIR ""
        no regreses nada
    END IF 
    SI numero == 0 entonces:
        ESCRIBIR ""
    // llama al procedimiento suma:
    // explicacion: numero se actualiza a 10, para volver a decrementarse
    // num3 aumenta en 1 ya que es valor del rango
    // val se queda tal cual
    // num2 se queda tal cual
    // num3+1 aumenta en 1 para mantener los valores del numero a multiplicar
    procedimiento suma(10,num3+1,val,num2,num3+1)

    END IF
    SI numero == 0 entonces:
        ESCRIBIR ""
        no regreses nada
    END IF   
    procedimiento suma(numero-1,num,val,num2,num3)
    // hace la cuenta hacia atras (el numero de vueltas que debe dar) 

    c = c+num // suma de el numero por cada vuelta

    ESCRIBIR "numero, " * ", val, " = ", c" //imprime el valor de numero el cual se decrementa en 1, despues el valor de val que solo sirve para guardar el valor inicial, despues imprime c, el cual es el acumulador
    return c // regresa c

FIN PROCEDIMIENTO
c = 0 // declaramos c con un valor inicial de 0
a = 10 // declaramos a con un valor inicial de 10, el cual se ira decrementando

ESCRIBIR "Tabla a multiplicar 1: "
LEER (y)
ESCRIBIR "Tabla a multiplicar 2: "
LEER (y2)
d = y // declaramos d que valdra igual que y

procedimiento suma(a,y,d,y2,y) //enviamos los valores de la variable
FIN ALGORTIMO


------ EXPLICACION DE FUNCIONABILIDAD -------- 
Rango = 4 - 5
Tabla a multiplicar(y): 4

numero(a)| num(y) = 4|val(d)|c|num2(y2) = 5|num3(y)
10       | 4         | 4    |4|5            4
9        | 4         | 4    |8|5            4
8        | 4         | 4    |12|5            4
7        | 4         | 4    |16|5            4 
6        | 4         | 4    |20|5            4    
5        | 4         | 4    |24|5            4
4        | 4         | 4    |28|5            4
3        | 4         | 4    |32|5            4
2        | 4         | 4    |36|5            4
1        | 4         | 4    |40|5            4

Aumento ---- 
10       | 5         | 5    |5|5            5
9        | 5         | 5    |10|5            5
8        | 5         | 5    |15|5            5
7        | 5         | 5    |20|5            5 
6        | 5         | 5    |25|5            5    
5        | 5         | 5    |30|5            5
4        | 5         | 5    |35|5            5
3        | 5         | 5    |40|5            5
2        | 5         | 5    |45|5            5
1        | 5         | 5    |50|5            5

"""

