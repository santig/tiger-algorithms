from LinkedListDS.node import Node


class LinkedList(object):

  def __init__(self):
    self.head = None
    self.counter = 0

  #O(1)
  def size(self):
    return self.counter

  # O(n)
  def traverse_list(self):
    actual_node = self.head

    while actual_node is not None:
      print ("%s" % actual_node.data)
      actual_node = actual_node.next_node

  # O(1)
  def insert_start(self, data):
    self.counter += 1 

    new_node = Node(data)

    if self.head:
      new_node.next_node = self.head 

    self.head = new_node

    #if not self.head:
    #  self.head = new_node
    #else:
    #  new_node.next_node = self.head
    #  self.head = new_node

  # O(n)
  def insert_end(self, data):

    if self.head is None:
      self.insert_start(data)
      return

    self.counter += 1

    new_node = Node(data)
    actual_node = self.head

    while actual_node.next_node is not None:
      actual_node = actual_node.next_node

    actual_node.next_node = new_node

  #O(n)
  def remove(self, data):
    self.counter -= 1

    if self.head:
      if self.head.data == data:
        self.head = self.head.next_node
      else:
        # This is recursive 
        self.head.remove(data, self.head)
