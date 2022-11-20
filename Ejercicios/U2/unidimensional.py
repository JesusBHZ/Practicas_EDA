n = int(input("Cuantos nombres quieres almacenar: "))
# Iniicalizacion del arreglo
A = []
for i in range(0, n):
  m = input("Dime el nombre: ")
  # Entrada de datos al arreglo
  A.append(m)
# Salida de los datos del arreglo
print(f"Los nombres que guardaste son: {A}")
