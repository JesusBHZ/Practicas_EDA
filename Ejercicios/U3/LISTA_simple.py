# Listas SIMPLE
# creamos la lista y sus valores
print("Esta es tu lista: ")
lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
print(lista)
print()

print("Tu lista tiene ", len(lista))  # cuantos elementos tiene una lista

lista.append("Sabado")  # agrega al final un valor
print()
print("A tu lista se le agrego la palabra 'Sabado'", lista)
print()
lista.insert(2, 3)  # agrega el valor donde queramos
print("Agregamos un 3 en la posicion 2 de la lista", lista)
lista.pop()  # elimina el ultimo elemento de la lista
print()
print("El ultimo elemento de la lista fue eliminado", lista)
print()

lista2 = ["Sabado", "Domingo"]
lista3 = lista + lista2  #  sumar listas
print("Dos listas se han sumado ", lista3)
print()
lista.reverse()  # voltear la lista
print("Tu lista se volteo ", lista)
lista.clear()  # limpia la lista
print()
print("Tu lista se vacio ", lista)
