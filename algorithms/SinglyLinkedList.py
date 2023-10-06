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

    def push_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def push_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert_node(self, index, value):
        if index < 0 or index > self.length:
            print(f"Invalid index. List length is {self.length}")
            return
        elif index == 0:
            self.push_head(value)
        elif index == self.length:
            self.push_tail(value)
        else:
            previous_node = self.get_node(index - 1)
            new_node = Node(value)
            new_node.next = previous_node.next
            previous_node.next = new_node
            self.length += 1

    def show_list(self):
        if not self.head:
            print("List is empty")
            return
        print("\n")
        current = self.head
        while current:
            print(current, end=" -> ")
            current = current.next
        print("\n")

    def pop_tail(self):
        if not self.head:
            print("List is empty")
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        self.length -= 1

    def pop_head(self):
        if not self.head:
            print("List is empty")
            return
        else:
            self.head = self.head.next
            self.length -= 1

    def get_node(self, index):
        if index < 0 or index >= self.length:
            print("No node at that index in the list")
            return None

        current = self.head
        for _ in range(index):
            current = current.next

        print(current)
        return current

    def set_node(self, index, value):
        found_node = self.get_node(index)
        if found_node is not None:
            found_node.value = value
        else:
            print("No node available at the provided index")

    def remove_node(self, index):
        if index < 0 or index >= self.length:
            print(f"Invalid index. List length is {self.length}")
            return
        if index == 0:
            self.pop_head()
            return
        elif index == self.length - 1:
            self.pop_tail()
            return
        previous_node = self.get_node(index - 1)
        found_node = self.get_node(index)
        if previous_node is not None and found_node is not None:
            previous_node.next = found_node.next
            found_node = None
            self.length -= 1

    def reverse_in_place(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head, self.tail = self.tail, self.head


linked_list = LinkedList()
linked_list.push_tail(7)
linked_list.push_head(9)
linked_list.insert_node(1, 11)
linked_list.set_node(2, 25)

print("Original linked list:")
linked_list.show_list()

linked_list.reverse_in_place()

print("Reversed linked list:")
linked_list.show_list()
