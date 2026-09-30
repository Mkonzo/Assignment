"""
Task 1: DynamicArray
Implement capacity, append, get, set, length, and resize —
i.e. build a simplified version of what Python's built-in list
does internally (and what Java's ArrayList / C++'s vector do).
"""


class DynamicArray:
    def __init__(self, initial_capacity=4):
        self._capacity = initial_capacity
        self._length = 0
        self._data = [None] * self._capacity

    def __len__(self):
        return self._length

    def length(self):
        return self._length

    def capacity(self):
        return self._capacity

    def get(self, index):
        if not (0 <= index < self._length):
            raise IndexError("index out of range")
        return self._data[index]

    def set(self, index, value):
        if not (0 <= index < self._length):
            raise IndexError("index out of range")
        self._data[index] = value

    def append(self, value):
        if self._length == self._capacity:
            self._resize(self._capacity * 2)   # double when full
        self._data[self._length] = value
        self._length += 1

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._length):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def __repr__(self):
        return f"[{', '.join(str(self._data[i]) for i in range(self._length))}]"


if __name__ == "__main__":
    arr = DynamicArray(initial_capacity=2)
    for i in range(6):
        arr.append(i * 10)
        print(f"append({i*10}) -> length={arr.length()}, capacity={arr.capacity()}, arr={arr}")

    arr.set(0, 999)
    print("after set(0, 999):", arr)
    print("get(3):", arr.get(3))