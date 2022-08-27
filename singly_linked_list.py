class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_list:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data, None)
        itr =  self.head
        if not self.head:
            self.head = node
        else:
            flag = True
            while flag:
                if itr.next:
                    itr = itr.next
                else:
                    flag = False
            itr.next = node

    def insert_values(self, lst):
        for i in lst:
            self.insert_at_beginning(i)

    def print(self):
        itr = self.head
        if not itr:
            print("Linked list is empty")
        while itr:
            print(itr.name, end="")
            if itr.next:
                print("-->", end="")
            itr = itr.next
        print()

    def get_length(self):
        length = 0
        itr = self.head
        while itr:
            length += 1
            itr = itr.next
        return length


    def remove_at(self, index):
        if index <0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next

        else:
            itr = self.head
            count = 0
            while count <= index:
                if count == index - 1:
                    itr.next = itr.next.next
                else:
                    itr = itr.next
                count += 1

    def insert_at(self, index, data):
        if index <0 or index > self.get_length() :
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)

        else:
            i = 0
            itr = self.head
            while itr:
                if i == index - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                i += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head.name == data:
            self.head = self.head.next
        else:
            itr = self.head
            while itr.next:
                if itr.next.name == data:
                    itr.next = itr.next.next
                    break
                itr = itr.next


ll = Linked_list()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple") # insert apple after mango
ll.print()
ll.remove_by_value("orange") # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()