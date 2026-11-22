"""
Part 2A: Arrays and Matrices (CLRS Section 10.1.1 - 10.1.2)
Implements:
  - SimpleArray: fixed-capacity array with access, insert, and delete
  - RowMajorMatrix: 2D matrix stored in a single 1D row-major array
"""


class SimpleArray:
    """Fixed-capacity 0-based array supporting access, insertion, and deletion."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.length = 0

    def access(self, index):
        """Return element at index in O(1) time."""
        if index < 0 or index >= self.length:
            raise IndexError("Array index out of bounds.")
        return self.data[index]

    def insert(self, index, value):
        """Insert value at index, shifting elements right in O(n) worst-case time."""
        if self.length == self.capacity:
            raise OverflowError("Array is full.")
        if index < 0 or index > self.length:
            raise IndexError("Insert index out of bounds.")

        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.length = self.length + 1

    def delete(self, index):
        """Remove and return element at index, shifting elements left in O(n) time."""
        if index < 0 or index >= self.length:
            raise IndexError("Delete index out of bounds.")

        removed = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

        self.data[self.length - 1] = None
        self.length = self.length - 1
        return removed

    def to_list(self):
        """Return the active elements as a Python list for display."""
        result = []
        for i in range(self.length):
            result.append(self.data[i])
        return result


class RowMajorMatrix:
    """
    m x n matrix stored in a single 1D array in row-major order.
    For 0-based indexing, M[row, col] maps to index: cols * row + col.
    """

    def __init__(self, rows, cols, default_value=0):
        self.rows = rows
        self.cols = cols
        self.data = [default_value] * (rows * cols)

    def _get_index(self, row, col):
        """Convert 2D (row, col) coordinates into a 1D row-major index."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Matrix position out of bounds.")
        return self.cols * row + col

    def access(self, row, col):
        """Read element at (row, col) in O(1) time."""
        return self.data[self._get_index(row, col)]

    def insert(self, row, col, value):
        """Store value at (row, col) in O(1) time."""
        self.data[self._get_index(row, col)] = value

    def delete(self, row, col, default_value=0):
        """Clear (row, col) back to default_value in O(1) time."""
        idx = self._get_index(row, col)
        old_value = self.data[idx]
        self.data[idx] = default_value
        return old_value

    def display(self):
        """Print the matrix row by row."""
        for r in range(self.rows):
            row_values = []
            for c in range(self.cols):
                row_values.append(self.access(r, c))
            print(row_values)


if __name__ == "__main__":
    print("--- SimpleArray Test ---")
    arr = SimpleArray(5)
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(1, 15)  # Shifts 20 to the right
    print("Array after inserts:", arr.to_list())
    print("Access index 1:", arr.access(1))
    print("Deleted index 0:", arr.delete(0))
    print("Array after delete:", arr.to_list())

    print("\n--- RowMajorMatrix (2x3) Test ---")
    mat = RowMajorMatrix(2, 3)
    values = [1, 2, 3, 4, 5, 6]
    idx = 0
    for r in range(2):
        for c in range(3):
            mat.insert(r, c, values[idx])
            idx = idx + 1
    mat.display()
    print("1D row-major array:", mat.data)
    print("Access (1, 0):", mat.access(1, 0))
    mat.delete(1, 0)
    print("After deleting (1, 0):", mat.access(1, 0))
