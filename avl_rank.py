# Source: https://gist.github.com/Jekton/d161ccf57bdcc9da5ee134c191f81af7


class AvlRankTree(object):
    class Node:
        def __init__(self, key):
            self.key = key
            self.height = 0
            self.size = 1
            self.left = None
            self.right = None

    def __init__(self):
        # Initially empty range index.
        self.root = None

    def add(self, key):
        # Inserts a key in the range index.
        if key is None:
            raise ValueError('Index must not be None')
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return AvlRankTree.Node(key)
        if root.key < key:
            root.right = self._insert(root.right, key)
        else:
            root.left = self._insert(root.left, key)
        return self._balance(root)

    def _update_height(self, root):
        root.height = max(self._height(root.left), self._height(root.right)) + 1

    def _update_size(self, root):
        root.size = self._size(root.left) + self._size(root.right) + 1

    @staticmethod
    def _height(node):
        if node is None:
            return -1
        return node.height

    @staticmethod
    def _size(node):
        if node is None:
            return 0
        return node.size

    def _balance(self, root):
        left_height = self._height(root.left)
        right_height = self._height(root.right)
        if left_height >= right_height + 2:
            if self._height(root.left.left) > self._height(root.left.right):
                root = self._right_rotate(root)
            else:
                root.left = self._left_rotate(root.left)
                root = self._right_rotate(root)
        elif right_height >= left_height + 2:
            if self._height(root.right.right) > self._height(root.right.left):
                root = self._left_rotate(root)
            else:
                root.right = self._right_rotate(root.right)
                root = self._left_rotate(root)
        else:
            self._update_height(root)
            self._update_size(root)
        return root

    def _left_rotate(self, root):
        right = root.right
        root.right = right.left
        right.left = root
        self._update_height(root)
        self._update_height(right)
        self._update_size(root)
        self._update_size(right)
        return right

    def _right_rotate(self, root):
        left = root.left
        root.left = left.right
        left.right = root
        self._update_height(root)
        self._update_height(left)
        self._update_size(root)
        self._update_size(left)
        return left

    def remove(self, key):
        # Removes a key from the range index.
        self.root = self._remove(self.root, key)

    def _remove(self, root, key):
        if root is None:
            return None

        if root.key < key:
            root.right = self._remove(root.right, key)
        elif root.key > key:
            root.left = self._remove(root.left, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                right_most_of_left = self._right_most(root.left)
                root.left = self._remove(root.left, right_most_of_left)
                root.key = right_most_of_left
        return self._balance(root)

    @staticmethod
    def _right_most(root):
        while root.right is not None:
            root = root.right
        return root.key

    def list(self, first_key, last_key):
        # List of values for the keys that fall within [first_key, last_key].
        lca = self._lca(first_key, last_key)
        result = []
        self._node_list(lca, first_key, last_key, result)
        return result

    def _node_list(self, node, lo, hi, result):
        if node is None:
            return
        if lo <= node.key <= hi:
            result.append(node.key)
        if node.key >= lo:
            self._node_list(node.left, lo, hi, result)
        if node.key <= hi:
            self._node_list(node.right, lo, hi, result)

    def _lca(self, lo, hi):
        node = self.root
        while node is not None and not (lo <= node.key <= hi):
            node = node.left if lo < node.key else node.right
        return node

    def count(self, first_key, last_key):
        # Number of keys that fall within [first_key, last_key].
        first_exists, first_rank, _ = self._rank(first_key)
        _, last_rank, _ = self._rank(last_key)
        return last_rank - first_rank + int(first_exists)

    def _rank(self, key):
        rank = 0
        root = self.root
        while root is not None and not (root.key == key):
            if key < root.key:
                root = root.left
            else:
                rank += self._size(root.left) + 1
                root = root.right
        if root is not None:
            rank += self._size(root.left) + 1
            return True, rank, root.key
        return False, rank, None

    def find(self, key):
        exists, _, existent_key = self._rank(key)
        return exists, existent_key
