"""
Part 2B: Stacks and Queues Using Arrays (CLRS Section 10.1.3)
Implements:
  - ArrayStack: LIFO stack using a fixed-size array
  - ArrayQueue: FIFO circular queue using a fixed-size array
"""


class ArrayStack:
    """
    LIFO stack implemented with a fixed-size array.
    Uses 0-based indexing where top = -1 means the stack is empty.
    """

    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.top = -1

    def is_empty(self):
        """Return True if the stack has no elements. O(1) time."""
        return self.top == -1

    def push(self, x):
        """Add x to the top of the stack in O(1) time."""
        if self.top == self.size - 1:
            raise OverflowError("Stack overflow.")
        self.top = self.top + 1
        self.data[self.top] = x

    def pop(self):
        """Remove and return the top element in O(1) time."""
        if self.is_empty():
            raise IndexError("Stack underflow.")
        self.top = self.top - 1
        return self.data[self.top + 1]

    def peek(self):
        """Return the top element without removing it in O(1) time."""
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.data[self.top]


class ArrayQueue:
    """
    FIFO circular queue implemented with a fixed-size array.
    Allocates (capacity + 1) slots so head == tail always means empty
    and (tail + 1) % size == head always means full.
    """

    def __init__(self, capacity):
        self.size = capacity + 1
        self.data = [None] * self.size
        self.head = 0
        self.tail = 0

    def is_empty(self):
        """Return True if the queue is empty. O(1) time."""
        return self.head == self.tail

    def is_full(self):
        """Return True if the queue cannot accept another element. O(1) time."""
        return (self.tail + 1) % self.size == self.head

    def enqueue(self, x):
        """Add x at the tail of the queue in O(1) time."""
        if self.is_full():
            raise OverflowError("Queue overflow.")
        self.data[self.tail] = x
        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail = self.tail + 1

    def dequeue(self):
        """Remove and return the element at the head in O(1) time."""
        if self.is_empty():
            raise IndexError("Queue underflow.")
        x = self.data[self.head]
        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head = self.head + 1
        return x


if __name__ == "__main__":
    print("--- ArrayStack Test ---")
    stack = ArrayStack(4)
    stack.push(15)
    stack.push(6)
    stack.push(2)
    print("Top element (peek):", stack.peek())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Is empty?", stack.is_empty())

    print("\n--- ArrayQueue (Circular Wrap-Around) Test ---")
    queue = ArrayQueue(3)
    queue.enqueue(15)
    queue.enqueue(6)
    queue.enqueue(9)
    print("Dequeued:", queue.dequeue())  # Removes 15 and frees a slot
    queue.enqueue(17)                    # Wraps around to reuse freed slot
    print("Dequeued:", queue.dequeue())  # Removes 6
    print("Dequeued:", queue.dequeue())  # Removes 9
    print("Dequeued:", queue.dequeue())  # Removes 17
    print("Is empty?", queue.is_empty())
