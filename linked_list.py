class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_index(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insert_at_begin(data)
        else:
            while current_node is not None and position + 1 != index:
                position = position + 1
                current_node = current_node.next

            if current_node is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def update_node(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while current_node is not None and position != index:
                position = position + 1
                current_node = current_node.next

            if current_node is not None:
                current_node.data = val
            else:
                print("Index not present")

    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    def remove_at_index(self, index):
        if self.head is None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while current_node is not None and position + 1 != index:
                position = position + 1
                current_node = current_node.next

            if current_node is not None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return

        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next

        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

    def reverse(self):
        prv = None
        current = self.head

        while current:
            nxt = current.next
            current.next = prv
            prv = current
            current = nxt

        self.head = prv

    def sort(self, reverse=False):
        if self.head is None or self.head.next is None:
            return

        sorted_list = None

        current = self.head
        while current:
            next_node = current.next
            current.next = None

            if sorted_list is None or (current.data < sorted_list.data) ^ reverse:
                current.next = sorted_list
                sorted_list = current
            else:
                sorted_current = sorted_list
                while (sorted_current.next and
                       ((sorted_current.next.data < current.data) ^ reverse)):
                    sorted_current = sorted_current.next

                current.next = sorted_current.next
                sorted_current.next = current

            current = next_node

        self.head = sorted_list

    def is_sorted(self, reverse=False):
        if self.head is None or self.head.next is None:
            return True

        sorted_list = None

        current = self.head
        while current:
            next_node = current.next
            current.next = None

            if sorted_list is None or (current.data < sorted_list.data) ^ reverse:
                sorted_list = current
            else:
                return False

            current = next_node

        return True

    def merge(self, other):
        if not self.is_sorted():
            self.sort()
        if not other.is_sorted():
            other.sort()

        merged_list = LinkedList()
        node1 = self.head
        node2 = other.head

        while node1 is not None and node2 is not None:
            if node1.data < node2.data:
                merged_list.insert_at_end(node1.data)
                node1 = node1.next
            else:
                merged_list.insert_at_end(node2.data)
                node2 = node2.next

        while node1 is not None:
            merged_list.insert_at_end(node1.data)
            node1 = node1.next

        while node2 is not None:
            merged_list.insert_at_end(node2.data)
            node2 = node2.next

        self.head = merged_list.head

    def __len__(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0

    def __str__(self) -> str:
        current_node = self.head
        string = ""
        while current_node:
            string = string + str(current_node.data) + " "
            current_node = current_node.next
        return string

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def __getitem__(self, index):
        current_node = self.head
        position = 0
        while current_node:
            if position == index:
                return current_node.data
            position = position + 1
            current_node = current_node.next
        raise IndexError("list index out of range")

    def __setitem__(self, index, value):
        current_node = self.head
        position = 0
        while current_node:
            if position == index:
                current_node.data = value
                return
            position = position + 1
            current_node = current_node.next
        raise IndexError("list index out of range")

    def __contains__(self, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return True
            current_node = current_node.next
        return False

    def __copy__(self):
        copy = LinkedList()
        current_node = self.head
        while current_node:
            copy.insert_at_end(current_node.data)
            current_node = current_node.next
        return copy

    def __reversed__(self):
        self_copy = self.__copy__()

        prv = None
        current = self_copy.head

        while current:
            nxt = current.next
            current.next = prv
            prv = current
            current = nxt

        self_copy.head = prv
