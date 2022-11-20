# clase Nodo
class Nodo():
  # tiene el dato que guarda y el apuntado al siguiente nodo
  dato = None
  siguiente = None

  # metodo inicial que se compone de un dato(puede ser de cualquier tipo de dato)
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None


# la funcion agregar_al_final recibe el nodo inicial, y el dato a insertar
def agregar_al_final(nodo_inicial, dato):
  # creamos el nuevo nodo
  nuevo_nodo = Nodo(dato)
  # si la lista esta vacia entonces el nodo inical es el ultimo nodo
  if nodo_inicial == None:
    nodo_inicial = nuevo_nodo
    # retornamos el nodo inicial
    return nodo_inicial
  # si no esta vacia entonces temporal rrecoore la lista hasta llegar al ultimo valor ya que lo enocntro el nodo siguiente del ultimo es el dodo nuevo
  temporal = nodo_inicial
  while temporal.siguiente != None:
    temporal = temporal.siguiente
  temporal.siguiente = nuevo_nodo
  return nodo_inicial


# remplaza el nodo inicial por el nuevo nodo
def agregar_al_inicio(nodo_inicial, dato):
  nuevo_nodo = Nodo(dato)
  nuevo_nodo.siguiente = nodo_inicial
  return nuevo_nodo


# imprimir lista recibe el nodo inical para saber desde donde partir
def imprimir_lista(nodo):
  # mientras el nodo no este vacio imprime el nodo
  while nodo != None:
    print(f"Tenemos {nodo.dato}")  # se imprime el nodo con el dato
    nodo = nodo.siguiente


# esta funcion recibe el nodo inical y es lo que retorna
def obtener_cabeza(nodo_inicial):
  return nodo_inicial


# esta fucnion recibe el nodo inical, itera sobre los nodos hasta encontrar el que no tenga siguiente y retorna ese
def obtener_cola(nodo_inicial):
  temporal = nodo_inicial
  while temporal.siguiente:
    temporal = temporal.siguiente
  return temporal


# esta funcion recibe el nodo y el datos buscado
def existe(nodo, busqueda):
  # va a rrecorrer los nodos hasta encontrar el valor buscado y retorna True o Flase segun corresponda
  while nodo != None:
    if nodo.dato == busqueda:
      return True
    nodo = nodo.siguiente
  return False


# recibe el nodo y valor buscado
def eliminar(nodo, busqueda):
  # si el nodo esta vacio no retorna nada
  if nodo == None:
    return
  # si el nodo actual es el buscado entonces retornamos el siguiente
  if nodo.dato == busqueda:
    return nodo.siguiente

  temporal = nodo
  # avanzamos por los ndos hasta encontar el buscado y hacemos que el nodo anterior apunte al nodo siguiente siguiente del actual (o el siguinete del buscado)
  while temporal.siguiente != None:
    if temporal.siguiente.dato == busqueda:
      if temporal.siguiente.siguiente != None:
        temporal.siguiente = temporal.siguiente.siguiente
      else:
        temporal.siguiente = None
        return nodo
    temporal = temporal.siguiente
  return nodo


def main():
  lista = None
  lista = agregar_al_final(lista, "Luis")
  lista = agregar_al_final(lista, "Leon")
  lista = agregar_al_inicio(lista, "Link")
  print("Antes de eliminar: ")
  imprimir_lista(lista)  # Link, Luis, Leon
  lista = eliminar(lista, "Link")
  print("Después de eliminar: ")
  imprimir_lista(lista)  # Luis, Leon
  print(existe(lista, "Link"))  # False
  print(existe(lista, "Luis"))  # True
  # obtener_cabeza nos regresa el nodo, pero accedemos al dato para imprimirlo
  print(obtener_cabeza(lista).dato)  # Luis
  print(obtener_cola(lista).dato)  # Leon


main()
