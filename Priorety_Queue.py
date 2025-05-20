from __future__ import annotations


class Node:

    def __init__(self, data: any, priority: int):
        self.data = data
        self.next_node = None
        self.priority = priority


class PriorityQueue:



    def __init__(self):

        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, item: any, priority: int) -> None:
        node = PriorityQueue.Node(item, priority)

        if self.is_empty():
            self.__tail = node
            self.__head = node

        elif self.__tail.priority <= node.priority:
            self.__tail.next_node = node
            self.__tail = node
        else:
            current_node = self.__head
            while current_node.next_node.priority <= node.priority:
                current_node = current_node.next_node

            node.next_node = current_node.next_node
            current_node.next_node = node

        self.__count += 1

    def dequeue(self) -> Node or None:
        if self.is_empty():
            return None

        result = self.__head.data

        self.__head = self.__head.next_node
        self.__count -= 1
        return result

    def peek(self) -> Node:
        if self.__head is not None: return self.__head.data
        else: return None

    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

