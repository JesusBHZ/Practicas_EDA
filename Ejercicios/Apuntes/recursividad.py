def funcion_andy(x):
 if (x == 1):
  return 1
 else:
  x = (x*funcion_andy(x - 1))
 return x
n = input('Dime un numero: ')
num = int(n)
print("El factorial de " ,num," es: " ,funcion_andy(num))