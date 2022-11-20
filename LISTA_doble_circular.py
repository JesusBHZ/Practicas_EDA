# LISTA DOBLE CIRCULAR
class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None

class DoublyLinkedList:
  def __init__(self):
    self.start_node = None

  def insert_in_emptylist(self, data):
    if self.start_node is None:
      new_node = Node(data)
      self.start_node = new_node
    else:
      print("list is not empty")

  def insert_at_start(self, data):
    if self.start_node is None:
      new_node = Node(data)
      self.start_node = new_node
      print("node inserted")
      return
    new_node = Node(data)
    new_node.nref = self.start_node
    self.start_node.pref = new_node
    self.start_node = new_node

  def insert_at_end(self, data):
    if self.start_node is None:
      new_node = Node(data)
      self.start_node = new_node
      return
      n = self.start_node
      while n.nref is not None:
        n = n.nref
      new_node = Node(data)
      n.nref = new_node
      new_node.pref = n


  def delete_at_start(self):
    if self.start_node is None:
        print("The list has no element to delete")
        return 
    if self.start_node.nref is None:
        self.start_node = None
        return
    self.start_node = self.start_node.nref
    self.start_prev = None

  def im(self):
    n = self.start_node
    while n.nref is not None:
      n = n.nref
      print(n)

      
new_linked_list = DoublyLinkedList()
new_linked_list.insert_in_emptylist(50)
new_linked_list.insert_at_start(10)
new_linked_list.insert_at_start(5)
new_linked_list.insert_at_start(18)
new_linked_list.insert_at_end(29)
new_linked_list.insert_at_end(39)
new_linked_list.insert_at_end(49)

new_linked_list.delete_at_start()
new_linked_list.im()
