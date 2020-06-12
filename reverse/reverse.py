class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev= None):
        if node is None:
            return
        current = node
        next = node.get_next()


        while (current):
            current.set_next(prev)
            prev = current
            current = next
            if next: 
                next = next.get_next()

        self.head = prev





        # current_head = node
        # current_head_value = node.value
        # next_value = current_head.next.value
        # node.value = next_value
        # node.next = current_head_value
        # self.reverse_list(node.next)



        # prev = None
        # current = self.head
        # while current is not None:
        #     next = current.next
        #     current.next = prev
        #     prev = current
        #     current = next
        # self.head = prev
