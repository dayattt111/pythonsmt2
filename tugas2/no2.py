class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class UntaianGanda:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def hitung_jumlah_dan_rata_rata(self):
        count = 0
        total = 0
        current = self.head
        while current:
            total += current.data
            count += 1
            current = current.next
        if count == 0:
            return 0, 0  # Menghindari pembagian dengan nol
        rata_rata = total / count
        return count, rata_rata

# Program Pengujian
dll = UntaianGanda()
dll.tambah(10)
dll.tambah(20)
dll.tambah(30)
dll.tambah(40)

count, rata_rata = dll.hitung_jumlah_dan_rata_rata()
print(f"Jumlah elemen: {count}, Rata-rata: {rata_rata:.2f}")  # Output: Jumlah elemen: 4, Rata-rata: 25.00
