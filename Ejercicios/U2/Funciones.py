import numpy as np
# Libreria necesaria para poder trabajar de una manera mas facil con las funciones y operaciones que nos permite realizar Pyhton 

def preguntas():
  a = np.array([[5, 1], [5, 10]])
  b = np.array([[2, 3], [7, 2]])
  print("------------------ Menu ------------------")
  print()
  print("Matriz a = ([[5, 1], [5, 10]])")
  print("Matriz b = ([[2, 3], [7, 2]])")
  print()
  print("Presione 1 para: Sumar arreglos")
  print("Presione 2 para: Restar arreglos ")
  print("Presione 3 para: Multiplicar arreglos")
  print("Presione 4 para: Dividir arreglos")
  print("Presione 5 para: Transponer la arreglo a")
  print("Presione 6 para: Elevar al cuadrado el arreglo a")
  print("Presione 7 para: Sumar todos los elementos del arreglo a ")

  print("Presione cualquier tecla para terminar")
  while True:
    print()
    option = str(input("¿Que Opcion Quiere? "))
    if option == "1":
      c = a + b
      print("Resultado: ")
      print(c)
      print()
      print("Funcionamiento: Cada valor de n posicion del arreglo a se suma directamnete con cada valor de n posicion del arreglo b, donde n tanto en a y b es la misma posicion pero con diferente arreglo")
      print("NOTA: Para poder aplicar esta operacion es necesario que ambos arreglos (a y b) sean de las mismas dimensiones (2 * 2)")
      print()

    elif option == "2":
      c = a - b
      print("Resultado: ")
      print(c)
      print()
      print("Funcionamiento: Cada valor de n posicion del arreglo a se resta directamente con cada valor de n posicion del arreglo b, donde n tanto en a y b es la misma posicion pero con diferente arreglo")
      print("NOTA: Para poder aplicar esta operacion es necesario que ambos arreglos (a y b) sean de las mismas dimensiones (2 * 2)")
      print()
      pass
    elif option == "3":
      c = a*b
      print("Resultado: ")
      print(c)
      print()
      print("Funcionamiento: Cada valor de n posicion del arreglo a se multiplica directamente con cada valor de n posicion del arreglo b, donde n tanto en a y b es la misma posicion pero con diferente arreglo")
      print("NOTA: Para poder aplicar esta operacion es necesario que ambos arreglos (a y b) sean de las mismas dimensiones (2 * 2)")
      print()
    elif option == "4":
      c = a/b
      print("Resultado: ")
      print(c)
      print()
      print("Funcionamiento: Cada valor de n posicion del arreglo a se divide directamente con cada valor de n posicion del arreglo b, donde n tanto en a y b es la misma posicion pero con diferente arreglo")
      print("NOTA: Para poder aplicar esta operacion es necesario que ambos arreglos (a y b) sean de las mismas dimensiones (2 * 2)")
      print()
    elif option == "5":
      c = a.transpose()
      print("Resultado: ")
      print(c)
      print()
      print("La trasposicion consiste en cambiar las filas por las columnas y viceversa.")
      print("Para trasponer un arreglo, se usa el método transpose.")
      print()
    elif option == "6":
      c = a**a
      print("Resultado: ")
      print(c)
      print()
      print("Funcionamiento: Cada valor de n posicion del arreglo a se multiplica a si mismo")
      print()
    elif option == "7":
      c = a.sum()
      print("Resultado: ")
      print(c)
      print()
      print("Funcionamiento: Se recorre los valores del arreglo, y a medida que se hce esto cada valor encontrado se va acumulando: a0+b0+a1+b2")
      print()
    else:
      break


preguntas()