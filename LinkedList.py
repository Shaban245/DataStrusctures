
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:

    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.lenght = 0


    def size(self) -> int:
        return  self.lenght


    def append_front(self, value: int):
        node = Node(value)
        self.lenght += 1
        if self.first_node is None:
            self.first_node = node
            self.last_node = node

        else:
            node.next = self.first_node
            self.first_node = node


    def append_back(self, value: int):
        node = Node(value)
        self.lenght += 1
        if self.last_node is None:
            self.first_node = node
            self.last_node = node

        else:
            self.last_node.next = node

    def set(self, index,  value):
        if self.first_node is None:
            return

        elif index > self.lenght - 1:
            raise ValueError

        elif self.lenght - 1 == index:
            self.last_node.value = value

        else:
            count = 0
            current_node = self.first_node

            while count != index:
                count += 1
                current_node = current_node.next

            current_node.value = value

    def get(self, index):
        if self.first_node is None:
            return

        elif index > self.lenght - 1:
            raise ValueError

        elif self.lenght - 1 == index:
            return self.last_node.value


        else:
            count = 0
            current_node = self.first_node

            while count != index:
                count += 1
                current_node = current_node.next

            return current_node.value

    def remove_front(self):
        if self.first_node is None:
            return
        else:
            self.lenght -= 1
            self.first_node = self.first_node.next

    def remove_back(self):
        if self.first_node is None:
            return

        else:
            current_node = self.first_node

            while current_node.next is not self.last_node:
                current_node = current_node.next

            current_node = self.last_node

    def insert(self, index, value):
        node = Node(value)
        if self.first_node is None and index >  0:
            return
        elif index > self.lenght - 1:
            raise ValueError



        elif index == 0:
            node.next = self.first_node
            self.first_node = node

        elif index == self.lenght - 1:
            node.next = self.last_node
            self.last_node = node

        else:
            count = 0
            current_node = self.first_node

            while count < index - 1:
                current_node  = current_node.next
                count += 1

            node.next = current_node.next
            current_node.next = node


    









