def get_size(self, value):
    self.__size = size.len(value)
    return self.__size

def is_empty(self, value):
    self.__empty = False
    if get_size(value) > 0:
        empty = True
    return empty

def find_from_head(self,value):
    curr_Node = self.__head
    encontrado = None

    while curr_Node.data != value:
        curr_Node = curr_Node.next

    if curr_Node.data == value:
        encontrado = curr_Node

    return encontrado

def find_from_tail(self, value):
    curr_Node = self.__tail
    encontrado = None

    while curr_Node.data != value:
        curr_Node = curr_Node.prev

        if curr_Node.data == value:
            encontrado = curr_Node

    return encontrado
