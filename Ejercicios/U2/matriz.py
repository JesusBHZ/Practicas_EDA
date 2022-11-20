# funcion que crea los areglos y los llena
def ferreteria():
  print("---MI LISTA DE PRODUCTOS---")
  # definimos el arreglo productos es bidimensional
  productos = []
  # solicitamos un valor, que sera el numero de productos a registrar
  tamano = int(input("Cuantos productos planea almacenar? "))
  # t nos permite llevar un control del el numero de productos a registrar entre dos, sirve para el llenado
  t = tamano / 2
  # creamos los ciclos para llenar el arreglo
  for x in range(tamano):
    # creamos una fila
    productos.append([])
    # creamos las columnas
    for i in range(int(t)):
      # solictamos el nombre del producto y lo guardamos en el arreglo
      dimension = str(input("Nombre: "))
      productos[x].append(dimension)
      # solictamos la cantidad del producto y lo guardamos en el arreglo
      dimension1 = int(input("Cantidad: "))
      productos[x].append(dimension1)
  print("---MI LISTA DE PRODUCTOS---")
  print("LO QUE TENGO")
  print()

  # con ciclo for rrecoremos el arreglo para imprimir los valores que lo componen
  for i in range(len(productos)):
    print(productos[i])

  print()
  # definimos un nuevo areglo unidimensional que almacena los productos con 0 existencias
  comprar = []
  # recorremos el arreglo de productpos
  for i in range(len(productos)):
    for l in range(len(productos)):
      # obtemos el valor del indice segun la fila en posicion de i con la columna con la posicion de l -1
      # esto es para obtener el nombre del producto
      val2 = productos[i][l - 1]
      # guardamos cada valor por separado en val
      val = productos[i][l]
      print(val)
      # evaluamos si val es 0 por que es la existencia en 0
      if val == 0:
        # si hay un producto con 0 lo guardamos en el arreglo comprar
        comprar.append(val2)
  print()
  print("---MI LISTA DE COMPRAS---")
  print("LO QUE DEBO COMPRAR")
  # impirmimos el arreglo que tiene los productos a comprar
  for i in range(len(comprar)):
    print("Producto: ", comprar[i])

  print()
  print()
  print("Instrucciones")
  print()

# llamamos la funcion ferreteria
ferreteria()

# ciclo infinito que se repetira hasta que el usuario diga que no quiere continuar
while True:
  print("Escriba: Si")
  print("Para continuar")
  print()
  print("Escriba: No")
  print("Para terminar")
  print()
  p = str(input("Quiere registrar una nueva lista de productos? "))
  # detenemos el ciclo si es otra resouesta que no sea "si"
  if p == "si":
    ferreteria()
  else:
    break
