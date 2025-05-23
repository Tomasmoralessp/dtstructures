class MinHeap:
    def __init__(self):
        self.heap = [None]

    def insert(self,value):
        # Añade el valor y lo ajusta hacia arriba
        # 1. Añadir el valor al final del heap
        self.heap.append(value)

        # 2. ¿Cuál es el index de este valor insertado?
        index = len(self.heap) - 1

        self._heapify_up(index)

    def extract_min(self):
        # Caso 1: Árbol vacío o un solo valor
        if len(self.heap) == 1:
            return None
        elif len(self.heap) == 2:
            return self.heap.pop()

        else:
            # 2. Guardar el valor de la raíz actual
            root = self.heap[1]

            # 3. Cambiar y eliminar la root por el útlimo elemento
            last_item = self.heap.pop()
            self.heap[1] = last_item
        

            # 4. Reorganizar la wea 
            self._heapify_down(1)

            return root


    def _heapify_up(self, index):
        while index > 1 and self.heap[index] < self.heap[index // 2]:
            self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
            index = index // 2

    def _heapify_down(self, index):

        while 2 * index  < len(self.heap):
            left_index = 2 * index
            right_index = 2 * index + 1

            # Asumimos que el pequeño es el izquierdo
            smaller_ind = left_index

            if right_index < len(self.heap) and self.heap[right_index] < self.heap[left_index]:
                smaller_ind = right_index

            if self.heap[index] > self.heap[smaller_ind]:
                self.heap[index], self.heap[smaller_ind] = self.heap[smaller_ind], self.heap[index]
                index = smaller_ind
            else:
                break

    def peek(self):
        if len(self.heap) <= 1:
            return None
        else:
            return self.heap[1]


    def __repr__(self):
        if len(self.heap) <= 1:
            return "<Heap vacío>"

        def build_lines(index, prefix="", is_left=True):
            if index >= len(self.heap):
                return []

            val = str(self.heap[index])
            left_index = 2 * index
            right_index = 2 * index + 1

            lines = []
            if right_index < len(self.heap):
                right = build_lines(right_index, prefix + ("│   " if is_left else "    "), False)
                lines += right

            lines.append(prefix + ("└── " if is_left else "┌── ") + val)

            if left_index < len(self.heap):
                left = build_lines(left_index, prefix + ("    " if is_left else "│   "), True)
                lines += left

            return lines

        return "\n".join(build_lines(1))

minheap = MinHeap()
heap = [1, 3, 5, 10, 8, 12, 7]

for v in heap:
    minheap.insert(v)

print(minheap)

print()

print("Min:  ", minheap.extract_min())

print()

print(minheap)

print(minheap.peek())
