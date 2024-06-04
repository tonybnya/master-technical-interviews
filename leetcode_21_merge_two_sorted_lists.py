# pylint: disable=all


class Node:
    def __init__(self, val=0, nextnode=None):
        self.val = val
        self.nextnode = nextnode


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, val):
        node = Node(val)

        if self.head:
            tmp = self.head
            while tmp.nextnode:
                tmp = tmp.nextnode

            tmp.nextnode = node
        else:
            self.head = node

        self.length += 1

    def show(self):
        tmp = self.head

        while tmp:
            if not tmp.nextnode:
                print(f'[{tmp.val}] -> None')
            else:
                print(f'[{tmp.val}] -> ', end='')

            tmp = tmp.nextnode


def merge(list1, list2):
    newlst = LinkedList()
    tmp = newlst

    tmp1 = list1.head
    tmp2 = list2.head

    while tmp1 and tmp2:
        if tmp1.val <= tmp2.val:
            tmp.nextnode = tmp1
            tmp1 = tmp1.nextnode
        else:
            tmp.nextnode = tmp2
            tmp2 = tmp2.nextnode

        tmp = tmp.nextnode

    if tmp1:
        tmp.nextnode = tmp1

    if tmp2:
        tmp.nextnode = tmp2

    return newlst
    # return newlst.nextnode


if __name__ == '__main__':
    list1 = LinkedList()
    list2 = LinkedList()

    list1.insert(1)
    list1.insert(2)
    list1.insert(4)

    list2.insert(1)
    list2.insert(3)
    list2.insert(4)

    list1.show()
    list2.show()

    newlst = merge(list1, list2)
    newlst.show()
