"""
Part 2C: Singly Linked List (CLRS Section 10.2)
Implements:
  - Node: stores a key and a next pointer
  - SinglyLinkedList: supports insert_front, insert_end, search, delete, traverse
"""


class Node:
    """A single node in a singly linked list."""

    def __init__(self, key):
        self.key = key
        self.next = None


class SinglyLinkedList:
    """Singly linked list with a head pointer."""

    def __init__(self):
        self.head = None

    def insert_front(self, key):
        """Add a new node at the head of the list in O(1) time."""
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, key):
        """Add a new node at the end of the list in O(n) time."""
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def search(self, key):
        """Return the first node matching key, or None if not found. O(n) time."""
        current = self.head
        while current is not None and current.key != key:
            current = current.next
        return current

    def delete(self, key):
        """
        Remove the first node matching key in O(n) worst-case time.
        Returns True if removed, or False if key was not found.
        """
        prev = None
        current = self.head

        while current is not None and current.key != key:
            prev = current
            current = current.next

        if current is None:
            return False

        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        return True

    def traverse(self):
        """Visit every node from head to tail and return keys in a list. O(n) time."""
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.key)
            current = current.next
        return elements


if __name__ == "__main__":
    print("--- SinglyLinkedList Test ---")
    linked_list = SinglyLinkedList()
    linked_list.insert_front(1)
    linked_list.insert_front(4)
    linked_list.insert_front(16)
    linked_list.insert_front(9)
    print("Initial traversal:", linked_list.traverse())

    linked_list.insert_front(25)
    print("After insert_front(25):", linked_list.traverse())

    linked_list.insert_end(99)
    print("After insert_end(99):", linked_list.traverse())

    print("Search for 16 found?", linked_list.search(16) is not None)
    print("Delete 4 succeeded?", linked_list.delete(4))
    print("After delete(4):", linked_list.traverse())
