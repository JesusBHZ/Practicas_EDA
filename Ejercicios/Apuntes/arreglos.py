"""n = int(input('Tamaño'))
m = int(input('Multiplo'))

A = []

for i in range(0,n):
  A.append(i*m)

print(A)
10 // 3= 3
10 % 3 = 1

** potencia

+	Realiza Adición entre los operandos	12 + 3 = 15
-	Realiza Substracción entre los operandos	12 - 3 = 9
*	Realiza Multiplicación entre los operandos	12 * 3 = 36
/	Realiza División entre los operandos	12 / 3 = 4
%	Realiza un módulo entre los operandos	16 % 3 = 1
**	Realiza la potencia de los operandos	12 ** 3 = 1728
//	Realiza la división con resultado de número entero	18 // 5 = 3


A = [1,5,8,9,30,9,13]
B = []
# impares a 3
for i in A:
  if i > 3 and i % 2 != 0:
    B.append(i)

print(B)

# calcular 10 numeros aleatorios

import random
def vector_aleatorio(n):
  vector = [0]*n
  for i in range(n):
    vector[i] = random.randint(0,10)
  return vector 
print("Cuantas numero ocupas : ")
n = int(input())

aleatorio = vector_aleatorio(n)

print(aleatorio)




"""

# ------------------
# arreglos multidimensionales
"""m = [[1,2],[3,4],[5,6]]
for f in range(3):
  for c in range(2):
    print(m[f][c], end=' ')
  print()
a = []
m = 3
n = 2
for f in range(m):
  a.append([])
  for c in range(n):
    a[f].append(None)

for f in range(m):
  for c in range(n):
    print(a[f][c], end=' ')
  print()"""

import random

fil = 3
col = 3
a = [[random.randint(1, 100) for i in range(fil)] for j in range(col)]
for f in range(fil):
  for c in range(col):
    print(a[f][c], end=' ')
  print()


def triangulo(n):
  """
    for i in range(1,n+1) -> hacemos un bucle entre el 1 y el numero introducido
    " "*(n-i) -> añade los espacios al inicio
    "*"*(i+i-1) -> por cada valor entre el 1 y n+1, devolvemos la cantidad de asteriscos
    [] -> el resultado lo devuelve dentro de un array
    "\n".join() -> divide el array en una cadena separando cada elemento con un \n (salto de linea)
    """
  return "\n".join(
    [" " * (n - i) + "*" * (i + i - 1) for i in range(1, n + 1)])


numero = int(input("indica un numero: "))
print(triangulo(numero))