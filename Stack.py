class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None

class Stack:

    def __init__(self,):

        self.top = None
        self.bottom = None
        self.len = 0

    def is_empty(self):
        if self.top is None:
            return  False
        else:
            return True

    def peek(self):
        return self.bottom

    def size(self):
        return self.len

    def push(self, value):
        self.len += 1
        node = Node(value)

        if self.top is None:
            self.top = node
            self.bottom = node

        else:
            node.prev = self.bottom
            self.bottom = node
            

    def pop(self):

        if self.top is None:
            return  None

        else:
            self.len -= 1
            result = self.bottom.value
            self.bottom = self.bottom.prev
            return result



