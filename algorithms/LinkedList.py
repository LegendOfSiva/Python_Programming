class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def push_list_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def push_list_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def show_list(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current, end=" -> ")
            current = current.next

    def pop_list_tail(self):
        if not self.head:
            print("List is empty")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        self.length -= 1

    def pop_list_head(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next
        self.length -= 1