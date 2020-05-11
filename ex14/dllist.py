class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None


    def push(self, obj):
        """Appends a new value on the end of the list."""

        new_node = DoubleLinkedListNode(obj, None, None)

        if self.begin is None:
            self.begin = self.end = new_node
        else:
            self.end.next = new_node
            new_node.prev = self.end
            new_node.next = None
            self.end = new_node

    def pop(self):
        """Removes the last item and returns it."""

        if self.begin is None:
            return None
        elif self.begin == self.end and self.end.next is None:
            node = self.begin
            self.begin = None
            self.end = None
            return node.value
        else:
            node = self.end
            self.end = self.end.prev
            self.end.next.prev = None
            self.end.next = None
            return node.value

    def shift(self, obj):
        """Actually just another name for push."""

        self.push(obj)

    def unshift(self):
        """Removes the first item (from begin) and returns it."""

        if self.begin is None:
            return None
        elif self.begin == self.end:
            node = self.begin
            self.begin = None
            self.end = None
            return node.value
        else:
            node = self.begin
            self.begin = node.next
            node.prev = None
            self.begin.prev = None
            return node.value

    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly
        inside remove().  It should take a node, and detach it from
        the list, whether the node is at the front, end, or in the middle."""

        if self.begin == node:
            self.unshift()
        elif self.end == node:
            self.pop()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""

        node = self.begin
        count = 0

        while node:
            if node.value == obj:
                self.detach_node(node)
                return count
            else:
                count += 1
                node = node.next

    def first(self):
        """Returns a *reference* to the first item, does not remove."""

        if self.begin is None:
            return None
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""

        if self.end is None:
            return None
        return self.end.value

    def count(self):
        """Counts the number of elements in the list."""

        cur_node = self.begin
        count = 0
        if cur_node is None:
            print("This Single Linked List has 0 nodes")
        while cur_node is not None:
            cur_node = cur_node.next
            count += 1
        return count

    def get(self, index):
        """Get the value at index."""

        if self.begin is None:
            return None

        cur_node = self.begin
        count = 0
        while count < index:
            cur_node = cur_node.next
            count += 1
            if cur_node is None:
                return None
        return cur_node.value

    def print_list(self): # substitute of dump()
        if self.begin is None:
            print('Empty')
            return

        cur_node = self.begin
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next

    def _invariant(self):
        if self.begin == None:
            assert self.end == None, "End set while begin is not."

        if self.begin:
            assert self.begin.prev == None, "begin.prev not None"
            assert self.end.next == None, "end.next not None"
