class MultiplicationTable:
    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self._table = {(i, j): i*j for i in range(1, length + 1) for j in range(1, length + 1)}
        self._length = length

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self._table)

    def __str__(self):
        """Returns a string representation of the table"""
        st = ''
        for i in range(1, self._length + 1):
            for j in range(1, self._length + 1):
                st += str(self._table[(i,j)])
                st += "\n" if j == self._length else " | "
        return st

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        if x > self._length or y > self._length:
            raise IndexError
        else:
            return x * y
