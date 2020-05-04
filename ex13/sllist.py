class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt


class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None


    def print_list(self): # substitute of dump()
        if self.begin is None:
            print('Empty')
            return

        cur_node = self.begin
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next


    def push(self, obj):
        """Adds a new value to the end of the list"""
        new_node = SingleLinkedListNode(obj, None)
        if self.begin is None:
            self.begin = self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node


    def pop(self):
        """Removes the last item and returns it."""

        cur_node = self.begin

        if cur_node == None:
            return None
        elif cur_node.next is None:
            rmv = self.begin.value
            self.begin = None
            return rmv
        else:
            while cur_node != self.end:
                if cur_node.next.next is None:
                    rmv = cur_node.next.value
                    cur_node.next = None
                    self.end = cur_node
                    return rmv
                else:
                    cur_node = cur_node.next


    def shift(self, obj):
        """Adds a new value to the beginning of the list"""
        new_node = SingleLinkedListNode(obj, None)
        if self.begin is None:
            self.begin = new_node
        else:
            new_node.next = self.begin
            self.begin = new_node


    def unshift(self):
        """Removes the first item and returns it."""
        if self.begin is None:
            return None

        cur_node = self.begin
        self.begin = cur_node.next
        return cur_node.value


    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        cur_node = self.begin

        if cur_node and cur_node.value == obj:
            self.begin = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.value != obj:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None


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
