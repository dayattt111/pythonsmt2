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
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def hapus_berdasarkan_posisi(self, posisi):
        if self.head is None:
            return
        
        current = self.head

        # Menghapus kepala (head) untaian
        if posisi == 0:
            self.head = current.next
            if self.head:
                self.head.prev = None
            current = None
            return

        # Menghapus elemen di posisi tertentu
        for _ in range(posisi):
            current = current.next
            if current is None:
                return  # Posisi melebihi panjang untaian

        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

        current = None

    def tampilkan(self):
        elemen = []
        current = self.head
        while current:
            elemen.append(current.data)
            current = current.next
        print(elemen)

# Program Pengujian
dll = UntaianGanda()
dll.tambah(10)
dll.tambah(20)
dll.tambah(30)
dll.tambah(40)
dll.tambah(50)

print("Sebelum penghapusan:")
dll.tampilkan()  # Output: [10, 20, 30, 40, 50]

dll.hapus_berdasarkan_posisi(2)  # Menghapus elemen di posisi ke-2 (nilai 30)
print("Setelah penghapusan elemen di posisi ke-2:")
dll.tampilkan()  # Output: [10, 20, 40, 50]

dll.hapus_berdasarkan_posisi(0)  # Menghapus elemen di posisi ke-0 (nilai 10)
print("Setelah penghapusan elemen di posisi ke-0:")
dll.tampilkan()  # Output: [20, 40, 50]

dll.hapus_berdasarkan_posisi(5)  # Posisi tidak valid, tidak ada perubahan
print("Setelah mencoba menghapus elemen di posisi ke-5 (tidak ada perubahan):")
dll.tampilkan()  # Output: [20, 40, 50]
