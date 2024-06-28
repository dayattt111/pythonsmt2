class UnsortedPriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item, priority):
        self.queue.append((item, priority))

    def get_priority(self, element):
        return element[1]

    def sort_item(self):
        sorted_queue = sorted(self.queue, key=self.get_priority)
        for item in sorted_queue:
            print(f'Item: {item[0]}, Priority: {item[1]}')

    def display(self):
        for item in self.queue:
            print(f'Item: {item[0]}, Priority: {item[1]}')

# Program Pengujian
pq = UnsortedPriorityQueue()
pq.insert('A', 3)
pq.insert('B', 1)
pq.insert('C', 2)
pq.insert('D', 5)
pq.insert('E', 4)

print("Isi antrian sebelum diurutkan:")
pq.display()

print("\nIsi antrian setelah diurutkan berdasarkan prioritas:")
pq.sort_item()
