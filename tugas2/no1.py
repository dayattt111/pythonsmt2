class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UntaianTunggal:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def tampilkan(self):
        elemen = []
        current = self.head
        while current:
            elemen.append(current.data)
            current = current.next
        print(elemen)

    def gabung(self, L1, L2):
        if L1.head is None:
            self.head = L2.head
            return
        if L2.head is None:
            self.head = L1.head
            return
        last = L1.head
        while last.next:
            last = last.next
        last.next = L2.head
        self.head = L1.head

# Program Pengujian
L1 = UntaianTunggal()
L1.tambah(2)
L1.tambah(3)
L1.tambah(2)

L2 = UntaianTunggal()
L2.tambah(2)
L2.tambah(2)
L2.tambah(0)

L3 = UntaianTunggal()
L3.gabung(L1, L2)
L3.tampilkan()  # Output: [1, 2, 3, 4, 5, 6]
