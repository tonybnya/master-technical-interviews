"""
234. Palindrome Linked List
"""


class Node:
    """Definition of a Node"""
    def __init__(self, val=0, next=None):
        """Initialization"""
        self.val = val
        self.next = next


class LL:
    """Definition of a Singly Linked List"""
    def __init__(self, head):
        """Initialize the Singly Linked List"""
        self.head = head

    def push(self, val):
        """Method to push a value to the Linked List"""
        node = Node(val)

        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def pop(self):
        """Method to pop the last node of the Linked List"""
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
        """Method to print the Linked List"""
        if self.head is None:
            return

        temp = self.head
        while temp:
            print(f'{temp.val} -> ', end='')
            temp = temp.next
        print('None')

    # O(n) time
    # O(1) space
    def is_palindrome(self):
        """Method to check if the Linked List is a palindrome"""
        if self.head is None or self.head.next is None:
            return True

        stack = []
        temp = self.head

        while temp:
            stack.append(temp.val)
            temp = temp.next

        # print(stack)
        temp = self.head
        while temp:
            if temp.val == stack.pop():
                temp = temp.next
            else:
                return False

        return True


if __name__ == '__main__':
    lst = LL(None)
    lst.push(1)
    lst.push(2)
    # lst.push(2)
    # lst.push(1)
    lst.push(3)
    lst.print_ll()
    popped_val = lst.pop()
    print(popped_val)
    lst.print_ll()
    print(lst.is_palindrome())
