class Node:

    def __init__(self, value):
        self.data = value
        self.next_node = None





class Queue:




    def __init__(self):
        self.__count = 0

        self.head = None
        self.tail = None

    def enqueue(self, item: any) -> None:
        node = Node(item)

        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        self.__count += 1

    def dequeue(self):
        if self.head is None:
            return None

        result = self.head.value

        if self.__count == 1:
            self.tail = None

        self.head = self.head.next

        self.__count -= 1
        return result

    def peek(self):

        if self.head is not None:return self.head.value
        else: return None

    def is_empty(self):
        if self.__count == 0: return True
        else:
            return False

    def get_count(self):
        return self.__count

    def __str__(self):
        result = ""
        if self.head is None:
            return ""
        current_node = self.head
        while current_node.next is not None:
            result += str(current_node.value) + " "

        return result

