class Nodo():
  def __init__(self,dato):
    self.dato = dato
    self.siguiente = None
    self.anterior =None


class ListaDoblementeEnlazada():
  def __init__(self):
    self.primero = None
    self.ultimo = None
    self.size = 0

  def vacia(self):
    return self.primero == None

  def agregarfinal(self, dato):
    if self.vacia():
      self.primero = self.ultimo = Nodo(dato)
    else:
      aux = self.ultimo
      self.ultimo = aux.siguiente = Nodo(dato)
      self.ultimo.anterior = aux
    self.size +=1
    self.size = self.size + 1 

  def agregarinicio(self,dato):
    if self.vacia():
      self.primero = self.ultimo = Nodo(dato)
    else:
      aux = Nodo(dato)
      aux.siguiente = aux.primero
      self.primero.anterior = aux
      self.primero = aux
    self.size +=1
    self.size = self.size + 1

  def rrecorrer_inic1io(self):
    aux = self.primero
    while aux:
      print(aux.dato)
      aux = aux.siguiente

  def rrecorrer_fin(self):
    aux = self.ultimo 
    while aux:
      print(aux.dato)
      aux = aux.anterior


lista = ListaDoblementeEnlazada()
lista.agregarfinal(12)
lista.agregarfinal(13)
lista.agregarfinal(14)
lista.rrecorrer_inicio()


"""from os import system
system("clear")"""

""" investigar porgrajma lisas circulastes
doblememte enlazadas circulares """