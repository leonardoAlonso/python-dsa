from typing import TypeVar, Generic

T = TypeVar('T')


class DinamycArray(Generic[T]):

    def __init__(self):
        self._capacity = 1
        self._size = 0
        self.array = [None] * self._capacity

    def append(self, element: T):
        if self._size == self._capacity: # If the array is full, resize it
            self.resize(self._capacity * 2)
        self.array[self._size] = element # Add the element to the array
        self._size += 1 # increment the size of the array

    def pop(self) -> T:
        if self._size == 0:
            raise IndexError('pop from empty array')
        self._size -= 1 # decrement the size of the array
        element = self.array[self._size] # get the last element
        self.array[self._size] = None # remove the last element
        return element

    def insert(self, index:int, element: T):
        if self._size == self._capacity:
            self.resize(self._capacity * 2)
        if index < 0 or index > self._size: # index can not be negative or greater than the size of the array
            raise IndexError('index out of range')
        for i in range(self._size, index, -1): # Shift elements to the right, the -1 means that the loop will go from the end to the start
            self.array[i] = self.array[i - 1] # Move the element to the right
        self.array[index] = element
        self._size += 1

    def resize(self, new_capacity: int):
        new_array = [None] * new_capacity # Create a new array with the new capacity
        for i in range(self._size):
            new_array[i] = self.array[i] # Copy the elements to the new array
        self.array = new_array
        self._capacity = new_capacity
        

    def __str__(self):
        return str(self.array)


if __name__ == '__main__':
    array: DinamycArray[int] = DinamycArray()
    array.append(10)
    array.insert(1, 5)
    array.append(20)
    print("Last element", array.pop())
    print(array)
