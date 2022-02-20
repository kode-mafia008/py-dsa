
class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):

        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        itr = self.head
        if self.head is None:
            self.head = Node(data, None)
            return
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.insert_at_begin(data)
            return

        itr = self.head
        count = 0
        while itr.next:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def print(self):
        itr = self.head

        llstr = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = '-->'
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count


if __name__ == '__main__':
    root = LinkedList()
    root.insert_at_begin(5)
    root.insert_at_begin(10)
    root.insert_at_end(99)
    root.insert_at_end(344)
    root.insert_at(2, 1000)
    root.insert_at(1, 40)
    root.get_length()
    # root.print()
