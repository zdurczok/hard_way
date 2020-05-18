class StackNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class Stack(object):

    def __init__(self):
        self.top = None

    def push(self, obj):
        """Pushes a new value to the top of the stack."""

        node = StackNode(obj, None)

        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        """Pops the value that is currently on the top of the stack."""

        if self.top:
            node = self.top
            self.top = self.top.next
            return node.value
        else:
            return None

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        if self.top:
            return self.top.value
        else:
            return None

    def count(self):
        """Counts the number of elements in the stack."""

        node = self.top
        count = 0

        if node is None:
            return 0
        while node is not None:
            node = node.next
            count += 1
        return count

    def print_stack(self): # substitute of dump()
        if self.top is None:
            print('Empty')
            return

        node = self.top
        while node:
            print(node.value)
            node = node.next
