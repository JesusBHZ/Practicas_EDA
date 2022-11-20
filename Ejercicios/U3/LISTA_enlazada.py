#lista simple enlazada
# Creamos la clase node la cual se encargara de crear nuestro meetodo principal
class node:
  # definimos la funcion inicial que recibe dos parametros, data y next
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Creamos la clase linked_list
class linked_list: 
  # funcion constructora
    def __init__(self):
        self.head = None
    
    # Método para agregar elementos en el frente de la linked list
    def add_at_front(self, data):
      # funciona añadiendo valores enfrente del nodo, pero dejando la data que ya habia al principio
        self.head = node(data=data, next=self.head)  

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
      # determina si la cabezera del nodo esta vacia
        return self.head == None

    # Método para agregar elementos al final de la linked list
    def add_at_end(self, data):
      # si la cabaeza esta vacia, entonces no hace ningun dezplazo de valores y entonces solo agrega los valores nuevos
        if not self.head:
            self.head = node(data=data)
                   return
        # si no entonces rrecorre los nodos y ya que llego al final deja el nuevo valor
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
    
    # Método para eleminar nodos
    def delete_node(self, key):
        curr = self.head
        prev = None
      # rrecorre los nodos hasta llegar al requerido o buscado
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # si no lo encuentra
        if prev is None:
            self.head = curr.next
        # si lo encuentra entonces cambia las pociones
        elif curr:
            prev.next = curr.next
            curr.next = None

    # Método para obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
      # rrecorre los areglos hasta el ultimo
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
      # rrecore los nodos y los imprime
        while node != None:
            print(node.data, end =" => ")
            node = node.next


# s ahora maneja la clase y a partir de s controlamos todo
s = linked_list() # Instancia de la clase
s.add_at_front(5) # Agregamos un elemento al frente del nodo
s.add_at_end(8) # Agregamos un elemento al final del nodo
s.add_at_front(9) # Agregamos otro elemento al frente del nodo
s.delete_node(2)
s.print_list() # Imprimimos la lista de nodos

s.delete_node(5)
print()
s.print_list()