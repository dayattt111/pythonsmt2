class ArrayStack:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            print("Error: pop from empty stack")
            return None
        return self._data.pop()

    def top(self):
        if self.is_empty():
            print("Error: top from empty stack")
            return None
        return self._data[-1]

    def find_minimum(self):
        if self.is_empty():
            print("Error: stack is empty")
            return None
        return min(self._data)

    def find_maximum(self):
        if self.is_empty():
            print("Error: stack is empty")
            return None
        return max(self._data)

class Queue:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Error: dequeue from empty queue")
            return None
        return self._data.pop(0)

    def total_sum(self):
        return sum(self._data)

    def __repr__(self):
        return repr(self._data)

def hitung_jumlah_kuadrat(x, y):
    if x >= y:
        print("Error: Nilai x harus lebih kecil dari y.")
        return None
    
    z = sum(i ** 2 for i in range(x, y + 1))
    return z

def main():
    x = int(input("Masukkan nilai x: "))
    y = int(input("Masukkan nilai y: "))

    hasil = hitung_jumlah_kuadrat(x, y)
    if hasil is not None:
        print(f"Jumlah kuadrat dari semua angka bulat antara {x} dan {y} adalah {hasil}")

    stack = ArrayStack()
    stack.push(3)
    stack.push(5)
    stack.push(2)
    stack.push(8)

    minimum_value = stack.find_minimum()
    if minimum_value is not None:
        print("Minimum value in stack:", minimum_value)

    maximum_value = stack.find_maximum()
    if maximum_value is not None:
        print("Maximum value in stack:", maximum_value)

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Jumlah data dalam antrian:", queue.total_sum())
    value = Queue()
    for i in range(30):
        if (i % 3) == 0:
            value.enqueue(i)
        elif (i % 4) == 0:
            value.dequeue()

    print("Isi antrian setelah loop:", value)

if __name__ == "__main__":
    main()