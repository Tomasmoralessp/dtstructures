class MaxHeap:
    def __init__(self):
        self.heap = [None]


    def insert(self, value):
        if len(self.heap) <= 1:
            self.heap.append(value)

        else:
            self.heap.append(value)
            self._heapify_up(len(self.heap) -1 )
    
    def extract_max(self):
        if len(self.heap) <= 1:
            return None
        
        root = self.heap[1]

        last_item = self.heap.pop()
        self.heap[1] = last_item

        self._heapify_down(1)

        return root


    def _heapify_up(self, index):
        
        while (index // 2) < len(self.heap):
            parent_index = index // 2
            parent_value = self.heap[parent_index]
            
            # If there is a parent and its smaller than the appended switch them
            if parent_value and self.heap[index] > parent_value:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            # If there is no parent left or is not smaller break the loop
            else:
                break

    def _heapify_down(self, index):
        while (2 * index) < len(self.heap):
            left_index = 2 * index
            right_index = 2 * index + 1
            
            greater_ind = left_index
            
            # If there is a right index and its value is greater than the current greater_ind switch them
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[left_index]:
                greater_ind = right_index
            # If the greater_ind value is greater than the current switch them
            if self.heap[greater_ind] > self.heap[index]:
                self.heap[greater_ind], self.heap[index] = self.heap[index], self.heap[greater_ind]
                index = greater_ind
            # If neither of the aforementioned break the loop
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


maxheap = MaxHeap()


valores = [10, 4, 15, 1, 8, 20, 3]
for v in valores:
    maxheap.insert(v)

print(maxheap)

print("max:", maxheap.extract_max())
print(maxheap)


