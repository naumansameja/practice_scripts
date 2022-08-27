class Node:
    def __init__(self, data, next, prev=None):
        self.data = data
        self.next = next
        self.previous = prev


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        if self.head.next:
            self.head.next.previous = node

    def insert_at_end(self, data):
        if not self.head:
            node = Node(data, self.head)
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next

            itr.next = Node(data, None, itr)

    def get_length(self):
        length = 0
        itr = self.head
        while itr:
            length += 1
            itr = itr.next

        return length

    def insert_by_index(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception ("Invalid index")

        if index == 0:
            node = Node(data, self.head, None)
            self.head = node
            self.head.next.previous = node

        else:
            i = 0
            itr = self.head
            while itr:
                if i == index - 1:
                    itr.next = Node(data, itr.next, itr)
                    itr.next.next.previous = itr.next

                itr = itr.next
                i += 1

    def remove(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.previous = None

        else:
            itr = self.head
            i = 0
            while itr:
                if i == index - 1:
                    if index == self.get_length() - 1:
                        itr.next = itr.next.next
                    else:
                        itr.next = itr.next.next
                        itr.next.previous = itr
                itr = itr.next
                i += 1

    def print_forward(self):
        itr = self.head
        while itr:
            if itr.next:
                print(itr.name, end="-->")
            else:
                print(itr.name)
            itr = itr.next
        print()

    def print_backward(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        while itr:
            if itr.previous:
                print(itr.name, end="<--")
            else:
                print(itr.name)
            itr = itr.previous
        print()


ll = Linked_list()
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(6)
ll.insert_at_end(7)
ll.insert_by_index(0, 2)
ll.insert_by_index(3, 5)
ll.remove(5)
ll.print_forward()
ll.print_backward()