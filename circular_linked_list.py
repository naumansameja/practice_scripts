class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.previous = prev

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)
        if not self.head:
            self.tail = node
        self.head = node
        if self.tail:
            self.tail.next = self.head
        if self.head.next:
            self.head.next.previous = node
            self.head.previous = self.tail

    def insert_at_end(self, data):
        if not self.head:
            node = Node(data, self.head, None)
            self.head = node
            self.tail = node
        else:
            node = Node(data, self.head, self.tail)
            self.tail.next = node
            self.tail = node
            self.head.previous = self.tail

    def get_length(self):
        itr = self.head
        length = 0
        while itr:
            if itr == self.tail:
                length += 1
                break
            length += 1
            itr = itr.next
        return length

    def insert_at_index(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
        else:
            i = 0
            itr = self.head
            while itr:
                if i == index - 1:
                    node = Node(data, itr.next, itr)
                    itr.next = node
                    itr.next.next.previous = node
                if itr == self.tail:
                    break
                itr = itr.next
                i += 1



    def print(self):
        itr = self.head
        while itr:
            if itr == self.tail:
                print(itr.name)
                break
            else:
                if itr.next:
                    print(itr.name, end="-->")
                else:
                    print(itr.name)
            itr = itr.next



ll = Linked_List()
ll.insert_at_end(3)
ll.print()
# print(ll.get_length())