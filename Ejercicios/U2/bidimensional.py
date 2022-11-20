import numpy as np
def matriz():
  print("Primer Arreglo")
  matriz_1 = []
  tamano = int(input("Tamaño: "))
  for x in range(tamano):
    matriz_1.append([])
    for i in range(tamano):
      dimension = int(input("Valores: "))
      matriz_1[x].append(dimension)

  for j in matriz_1:
    print(j)

  print()

  print("Segundo Arreglo")
  matriz_2 = []
  tamano = int(input("Tamaño: "))
  for x in range(tamano):
    matriz_2.append([])
    for i in range(tamano):
      dimension = int(input("Numero: "))
      matriz_2[x].append(dimension)

  for j in matriz_2:
    print(j)

  print()
  print()

  Dm_1 = []
  for i in range(len(matriz_1)):
    for l in range(len(matriz_1)):
      val = matriz_1[i][l]
      if [i] == [l]:
        Dm_1.append(val)

  Dm_2 = []
  for i in range(len(matriz_2)):
    for l in range(len(matriz_2)):
      val = matriz_2[i][l]
      if [i] == [l]:
        Dm_2.append(val)

  print("La diagonal del primer arreglo es: ", Dm_1)
  print("La diagonal del primer arreglo es: ", Dm_2)

  print()

  print("La suma de ambas diagonal es:")
  b = 0
  d = ""
  if len(Dm_1) > len(Dm_2):
    b = len(Dm_1)
    d = "Dm_2"
  else:
    b = len(Dm_2)
    d = "Dm_1"

  resultado = []
  for i in range(b):
    try:
      c = Dm_1[i] + Dm_2[i]
    except IndexError:
      if d == "Dm_1":
        c = 0 + Dm_2[i]
      else:
        c = Dm_1[i] + 0
    resultado.append(c)

  print(resultado)


matriz()
while True:
  print("Escriba: Si")
  print("Para continuar")
  print()
  print("Escriba: No")
  print("Para terminar")
  print()
  p = str(input("Quiere seguir? "))
  if p == "si":
    matriz()
  else:
    break



# apunte 
"""
import numpy as np
m1 = []
m2 = []
def funcion():
  tamano = int(input("n1"))
  tamano2 = int(input("n2"))
  print("Matriz uno")
  for x in range(tamano):
    m1.append([])
    for i in range(tamano):
      dimension = int(input("")(x+1,i+1))
      m1[x].append(dimension)

  for j in m1:
    print(j)

  print("Matriz dos")
  for a in range(tamano1):
    m2.append([])
    for r in range(tamano1):
      dimension1 = int(input("")(a+1,r+1))
      m1[a].append(dimension1)

  for z in m2:
    print(z)


  print("diagonal 1")
  d = np.diagonal(m1)
  print(d)

  print("diagonal 2")
  d1 = np.diagonal(m2)
  print(d1)

  c = np.add(d,d1)
  print(c)
"""
  