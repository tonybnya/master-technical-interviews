"""
876. Middle of the Linked List
"""


class Node:
    """Definition of a Node"""
    def __init__(self, val=0, next=None):
        """Initialization"""
        self.val = val
        self.next = next


class SLL:
    """Definition of a Singly Linked List"""
    def __init__(self, head):
        """Initialize the Singly Linked List"""
        self.head = head

    def push(self, val):
        """Method to push a value to the Singly Linked List"""
        node = Node(val)

        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def pop(self):
        """Method to pop the last node of the Singly Linked List"""
        if self.head is None:
            return None

        if self.head.next is None:
            popped_val = self.head.val
            self.head = None
            return popped_val

        temp = self.head
        while temp.next.next:
            temp = temp.next
        popped_val = temp.next.val
        temp.next = None
        return popped_val

    def print_ll(self):
        """Method to print the Singly Linked List"""
        if self.head is None:
            return

        temp = self.head
        while temp:
            print(f'[{temp.val}] -> ', end='')
            temp = temp.next
        print('None')

    def length(self):
        """Method to get the length of the Singly Linked List"""
        length = 0
        if self.head is None:
            return

        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length

    def middle_node(self):
        """Get the middle nodeof the linked list"""
        length = self.length()
        middle = length // 2
        res = None

        idx = 0
        temp = self.head
        while temp:
            if idx == middle:
                res = temp
            idx += 1
            temp = temp.next

        return res


if __name__ == '__main__':
    sll1 = SLL(None)
    sll2 = SLL(None)

    sll1.push(1)
    sll2.push(1)

    sll1.push(2)
    sll2.push(2)

    sll1.push(3)
    sll2.push(3)

    sll1.push(4)
    sll2.push(4)

    sll1.push(5)
    sll2.push(5)

    sll2.push(6)

    print('Singly Linked List #1')
    sll1.print_ll()
    print(f'Length: {sll1.length()}')
    print(f'Middle node: {sll1.middle_node()}')

    print()

    print('Singly Linked List #2')
    sll2.print_ll()
    print(f'Length: {sll2.length()}')
    print(f'Middle node: {sll2.middle_node()}')
