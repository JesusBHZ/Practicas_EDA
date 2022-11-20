# Realizar programa realize la multiplicacion de dos numeros cualquiera
# ---- CODIGO -----
def suma(numero, num):
  if numero <= 0:
    return
  # print("numero: ",numero)
  suma(numero - 1, num)

  # print("num: ",num)
  global c
  c = c + num
  return c


c = 0
v = int(input("Numero a multiplicar 1: "))
y = int(input("Numero a multiplicar 2: "))

print(f"Tu resultado es: {suma(v,y)}")
"""
---- PSEUDOCODIGO -----
procedimiento suma(num,num)
    SI numero <= 0 entonces:
        no regreses nada
    // hace la cuenta hacia atras (el numero de vueltas que debe dar) 
    END IF   
    procedimiento suma(numero-1,num)
    c //llamamos a la variable global c que sirve como acumulador

    c = c+num // suma de el numero por cada vuelta
    return c // regresa c

    c = 0 // declaramos c con un valor inicial de 0
FIN PROCEDIMIENTO
ESCRIBIR "Numero 1: "
LEER (v)

ESCRIBIR "Numero 2: "
LEER (y)

ESCRIBIR "Tu resultado es: " + suma(v,y) // le enviamos a suma el valor de v y y
FIN ALGORTIMO


------ EXPLICACION DE FUNCIONABILIDAD -------- 
Numero 1(v): 3
Numero 2(y): 4

VUELTAS (y)     |   sumatoria(v)
1               |   3 (3+0)
2               |   6 (3+3)
3               |   9 (6+3)
4               |   12(9+3)

"""
