def pregunta(a):
  if a == "si":
    alumnos = []
    calificaciones = []
    while True:
      instruccion = str(input("¿Quieres registrar un alumno? "))
      cal = 0
      if instruccion == "si":
        name = str(input("Nombre alumno: "))
        alumnos.append(name)
        for i in range(3):
          cali = int(input("Calificacion: "))
          cal = cal + cali
        c = cal / 3
        calificaciones.append(c)
      elif instruccion == "no":
        print("")
        print("Esta bien")
        if not alumnos:
          print("Fin")
          exit()
        else:
          pos = int(input("¿Que posición desea consultar? "))
          posF = pos - 1
          print(
            f"El alumno que corresponde con ese indice es: {alumnos[posF]}")
          print(f"Su calificacion es: {calificaciones[posF]}")
          
          while True:
            a = str(input("¿Quieres consultar otro indice? "))
            if a == "si":
              pos = int(input("¿Que índice o posición desea consultar? "))
              posF = pos - 1
              print(
                f"El alumno que corresponde con ese indice es: {alumnos[posF]}"
              )
              print(f"Su calificacion es: {calificaciones[posF]}")
            else:
              break

          print("")
          instruccion2 = str(
            input("¿Quieres registrar calificaciones de otra materia? "))
          if instruccion2 == "si":
            alumnos = []
            calificaciones = []
            pregunta(a)
          else:
            print("Fin")
            exit()
      else:
        print(" Solo acepto si y no")
    else:
      print("")
      print("Esta bien ... Termino")


a = "si"
pregunta(a)
