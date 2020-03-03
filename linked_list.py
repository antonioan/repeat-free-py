# Source: https://github.com/Darthfett/Hashtable/blob/master/LinkedList.py


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def push(self, new, prev=None):
        if prev is None:
            new.next = self.head
            self.head = new
        else:
            new.next = prev.next
            prev.next = new
            if new.next is None:
                self.tail = new

    def pop(self, index=0):
        cur = index
        prev_node = None
        cur_node = self.head
        while cur > 0:
            prev_node = cur_node
            cur_node = cur_node.next
            cur -= 1

        if cur_node.next is None:
            self.tail = prev_node
        if prev_node is None:
            popped = self.head
            self.head = cur_node.next
            return popped
        else:
            prev_node.next = cur_node.next
            return cur_node

    def insert(self, node, index=0):
        if node is None:
            raise Exception("node is None Type")
        cur = index
        prev_node = None
        next_node = self.head
        while cur > 0:
            if next_node is None:
                raise Exception("Index out of bounds")
            prev_node = next_node
            next_node = next_node.next
            cur -= 1

        if prev_node is None:
            self.head = node
        else:
            prev_node.next = node

        node.next = next_node
        if next_node is None:
            self.tail = node

    def __str__(self):
        return str(self.head) if self.head is not None else ""
