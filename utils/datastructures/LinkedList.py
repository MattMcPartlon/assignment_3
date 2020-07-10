class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, head):
        self.head=head

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail



class LinkedListNode(object):

    def __init__(self, data):
        self.data = data
        self.left, self.right, self.above, self.below = None, None, None, None

    def set_4_neighbors(self, left : 'LinkedListNode', right : 'LinkedListNode',
                        above: 'LinkedListNode', below:'LinkedListNode' ):
        self.set_left_and_right(left, right)
        self.set_above_below(above, below)

    def set_left_right(self, left, right):
        self.set_left(left)
        self.set_right(right)

    def set_above_below(self, above : 'LinkedListNode', below : 'LinkedListNode'):
        self.set_above(above)
        self.set_above_below(below)

    def set_left(self, node : 'LinkedListNode' ) -> 'LinkedListNode':
        self.left = node

    def set_right(self, node : 'LinkedListNode' ) -> 'LinkedListNode':
        self.right = node

    def set_above(self, node: 'LinkedListNode') -> 'LinkedListNode':
        self.above = node

    def set_below(self, node : 'LinkedListNode') -> 'LinkedListNode':
        self.below = node

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_above(self):
        return self.above

    def get_below(self):
        return self.below

    def get_data(self):
        return self.data

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def has_above(self):
        return self.above is not None

    def has_below(self):
        return self.below is not None

    def __str__(self):
        return 'LinkedListNode : {}'.format(str(self.data))

