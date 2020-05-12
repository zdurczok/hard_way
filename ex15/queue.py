class QueueNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class Queue(object):

    def __init__(self):
        self.tail = None
        self.head = None

    def shift(self, obj):
        """Shifts a new value on the end of the queue"""

        node = QueueNode(obj, None, None)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node

    def unshift(self):
        """Removes the first item (from begin) and returns it."""

        if self.head is None:
            return None
        elif self.head == self.tail:
            node = self.head
            self.head = None
            self.tail = None
            return node.value
        else:
            node = self.head
            self.head = node.next
            node.prev = None
            self.head.prev = None
            return node.value

    def first(self):
        """Returns a *reference* to the *head* item, does not remove."""

        if self.head is None:
            return None
        return self.head.value

    def last(self):
        """Returns a reference to the *tail* item, does not remove."""

        if self.tail is None:
            return None
        return self.tail.value

    def count(self):
        """Counts the number of elements in the queue."""

        cur_node = self.head
        count = 0
        if cur_node is None:
            print("This queue List has 0 nodes")
        while cur_node is not None:
            cur_node = cur_node.next
            count += 1
        return count

    def print_queue(self): # substitute of dump()
        if self.head is None:
            print('Empty')
            return

        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next

    def _invariant(self):
        if self.head == None:
            assert self.tail == None, "End tail while head is not."

        if self.head:
            assert self.head.prev == None, "head.prev not None"
            assert self.tail.next == None, "tail.next not None"
