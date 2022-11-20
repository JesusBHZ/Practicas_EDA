def pregunta(a,b):
  if a == "si":
    
    totales = []
    subtotales = []

    # text
    precio_u = []
    cantidades = []
    productos_list  = []
    
    global to
    to = 0

    global vueltas
    vueltas = 0
    
    while True:
      
      if b == "si":
        s = "si"
        b = "no"
      else:
       s = str(input("¿Quieres comprar? "))
        
      cal = 0
      instruccion = s
      
      if instruccion == "si" and b =="no":
        vueltas = vueltas+1
        name = str(input("Nombre producto: "))
        productos_list.append(name)
        
        precio = float(input("Precio: "))
        precio_u.append(precio)
        
        cantidad = int(input("Cantidad: "))
        cantidades.append(cantidad)
        
        c = cantidad * precio
        subtotales.append(c)

        to = to+c
        print(f"Subtotal: {to}")
 
      elif instruccion == "no":
        totales.append(to)
        
        print("")
        print("Producto - Cantidad - Precio_u - Subtotal")
        
        for i in range(int(vueltas)):
          print(f"{productos_list[i]} - {cantidades[i]} - {precio_u[i]}- {subtotales[i]}")
          
        print(f"Pagaras por todo:{totales}")
        print("")
        
        instruccion2 = str(input("¿Quieres comprar mas? "))
        
        if instruccion2 == "si":
          totales = []
          subtotales = []
      
          # text
          precio_u = []
          cantidades = []
          productos_list  = []
          
          to = 0
          vueltas = 0
          
          b = "si"
          pregunta(a,b)
        else:
            print("Fin")
            exit()
          
      else:
        print(" Solo acepto si y no")
    else:
      print("")
      print("Esta bien ... Termino")

a = "si"
b = "no"
pregunta(a,b)
