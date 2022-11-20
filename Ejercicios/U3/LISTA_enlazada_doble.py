#LISTA ENLAZADA DOBLE
class Node():
  # mtodo principal de la clase Node y su contructor que se compone de data
  def __init__(self,data : str):
    self.data = data
    self.next = None
    self.prev = None
    
class double_linked():

    def __init__(self):
        self.head  = None
        self.end  = None
    # metodo para insertar un valor de tipo str
    def append(self,data: str):

        new_node = Node(data)
        # asiganamos el valor del valor ingresado como Data en new_mode
        # si mi lista esta vacia entonces definimos que el valor de new_mode sera el primer nodo y el sisguiente nodo sera el mismo
        if self.end != None:
            new_no de.prev = self.end
            self.end.next = new_node
            self.end = new_node
            return
        # asignamos los valores a new_mode
        self.head = new_node
        self.end  = new_node
    
      # metodo para contruir la lista, por cada valor nuevo se le agrega una ,
    
    def __str__(self):
        result = ""
        temp_node = self.head
        # rrecorre el nodo y va acomodando los valores
        while temp_node != None:
            result += temp_node.data + ","
            temp_node = temp_node.next
        return result 
    # metodo para encontrar un valor en la lista
    def find(self,data : str) -> Node:

        temp_node = self.head
      # rrecorre la lista hasta encontrar el valor
        while temp_node != None:
            if temp_node.data == data:
                return temp_node
            
            temp_node = temp_node.next

        return None
  # imprime la lista en reversa, empezando por el ultimo valor de la lista
    def print_reverse(self) -> str:
        result = ""
        temp_node = self.end

        while temp_node != None:
            result += temp_node.data + ","
            temp_node = temp_node.prev
        
        return result


# s ahora maneja la clase y a partir de s controlamos todo
s = double_linked() # Instancia de la clase
s.append("2")
print(s.print_reverse())# Imprimimos la lista de nodos

