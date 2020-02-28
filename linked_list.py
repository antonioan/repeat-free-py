# Source: https://github.com/Darthfett/Hashtable/blob/master/LinkedList.py


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head

        # TODO: Support for self.tail is still in progress. Only push() supports it for now.
        raise NotImplementedError()

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

        if prev_node is None:
            popped = self.head
            self.head = self.head.next
            return popped
        else:
            prev_node = cur_node.next
            return cur_node

    def insert(self, node, index=0):
        if node is None:
            raise Exception("node is None Type")
        cur = index
        prev_node = None
        cur_node = self.head
        while cur > 0:
            prev_node = cur_node
            cur_node = cur_node.next
            cur -= 1

        if prev_node is None:
            self.head = node
        else:
            prev_node.next = node

        node.next = cur_node

    def __str__(self):
        return str(self.head) if self.head is not None else ""
