class Nodo():
  def __init__(self,dato):
    self.dato = dato
    self.siguiente = None
        
class ListaCircular():
  def __init__(self):
    self.primero = None
    self.ultimo = None
        
  def vacia(self):
    return self.primero == None
    
  def agregarInicio(self,dato):
    if self.vacia():
        self.primero = self.ultimo = Nodo(dato)
        self.ultimo.siguiente = self.primero
    else:
        aux = Nodo(dato)
        aux.siguiente = self.primero
        self.primero = aux
        self.ultimo.siguiente = self.primero
        
  def agregarFinal(self,dato):
    if self.vacia():
      self.primero = self.ultimo = Nodo(dato)
      self.ultimo.siguiente = self.primero
    else:
      aux = self.primero
      self.ultimo = aux.siguiente = Nodo(dato)
      self.ultimo.siguiente = self.primero
        
  def rrecorrer(self):
    aux = self.primero
    while aux.siguiente != self.primero:
      print(aux.dato)
      aux = aux.siguiente
      if aux == self.primero:
        break
    print(aux.dato) 
          
            

lista = ListaCircular()

lista.agregarFinal(10)
lista.agregarFinal(11)
lista.agregarFinal(11)
lista.agregarFinal(123)

lista.agregarInicio(15)
lista.agregarInicio(15)

lista.rrecorrer()      
