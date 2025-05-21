class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    return

    def lookup(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def find_node(self, value):
        current = self.root
        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def find_parent(self, value):
        current = self.root
        parent = None
        while current:
            if value == current.value:
                return parent
            elif value < current.value:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
        return None

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def _remove_node_by_reference(self, node, parent):
        # Caso 1: nodo sin hijos
        if node.left is None and node.right is None:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            return

        # Caso 2: nodo con un solo hijo
        child = node.left if node.left else node.right
        if parent.left == node:
            parent.left = child
        else:
            parent.right = child

    def remove(self, value):
        parent = self.find_parent(value)
        node_to_remove = self.find_node(value)

        if node_to_remove is None:
            return False  # No existe

        # Caso 3: El nodo tiene 2 hijos
        if node_to_remove.left and node_to_remove.right:
            successor = self.find_min(node_to_remove.right)
            successor_parent = self.find_parent(successor.value)

            node_to_remove.value = successor.value
            self._remove_node_by_reference(successor, successor_parent)
            return True

        # Caso 2: el nodo tiene un solo hijo
        if node_to_remove.left or node_to_remove.right:
            hijo = node_to_remove.left or node_to_remove.right

            if node_to_remove == self.root:
                self.root = hijo
            else:
                if parent.left == node_to_remove:
                    parent.left = hijo
                elif parent.right == node_to_remove:
                    parent.right = hijo
            return True

        # Caso 1: el nodo es hoja
        if node_to_remove.left is None and node_to_remove.right is None:
            if parent is None:
                self.root = None
            elif parent.left == node_to_remove:
                parent.left = None
            else:
                parent.right = None
            return True

        return NotImplemented

    def __repr__(self):
        return self._draw_tree(self.root)

    def _draw_tree(self, node, prefix="", is_left=False):
        if node is None:
            return ""
        result = ""
        if node.right:
            result += self._draw_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        result += prefix + ("└── " if is_left else "┌── ") + str(node.value) + "\n"
        if node.left:
            result += self._draw_tree(node.left, prefix + ("    " if is_left else "│   "), True)
        return result


bst = BinarySearchTree()

for v in [20, 10, 30, 5, 15, 25, 35, 14, 16, 13]:
    bst.insert(v)

print("Árbol antes de eliminar 15:")
print(bst)

bst.remove(15)

print("Árbol después de eliminar 15:")
print(bst)
