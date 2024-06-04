"""
Leetcode 876: Middle of the Linked List
"""

from singly_linked_list import Node, SinglyLinkedList


if __name__ == "__main__":
    sllist = SinglyLinkedList()

    sllist.insert_at_begin(1)
    sllist.print_sll()
    sllist.insert_at_end(2)
    sllist.print_sll()
    sllist.insert_at_end(3)
    sllist.print_sll()
    sllist.insert_at_begin(0)
    sllist.print_sll()
    sllist.insert_at_index(6, 2)
    sllist.print_sll()
    sllist.update_at_index(2, 2)
    sllist.print_sll()
    sllist.remove_last_node()
    sllist.print_sll()
    sllist.remove_node(2)
    sllist.print_sll()
