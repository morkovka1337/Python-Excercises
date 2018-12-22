class Node():
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
    
    def __repr__(self):
        if self == None:
            return ''
        return str(self.value) + str(self.left_child) + str(self.right_child)

    # def __repr__(self):
    #     return "\t" + self.value.__repr__() + "\n" + self.left_child.__repr__() + "\t\t" + self.right_child.__repr__()

class Biniry_Search_Tree():
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left_child==None:
                node.left_child = Node(value)
            else:
                self._insert(value, node.left_child)
                
        else:
            if node.right_child == None:
                node.right_child = Node(value)
            else:
                self._insert(value, node.right_child)
                
    def height(self):
        if self.root == None:
            return 0
        else:
            return self._height(self.root, 0)

    def _height(self, node, cur_height):
        if node == None:
            return cur_height
        left_height = self._height(node.left_child, cur_height + 1)
        right_height = self._height(node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root == None:
            return None
        else:
            return self._search(value, self.root)

    def _search(self, value, node):
        if node:
            if node.value == value:
                return node
            elif value < node.value:
                return self._search(value, node.left_child)
            else:
                return self._search(value, node.right_child)
        else:
            return None

    def print_tree(self):
        if self.root:
            self._print(self.root)

    def __repr__(self):
        tree_height = self.height()
        res = '  ' * tree_height + str(self.root.value)
        res += str(self.root.left_child) + str(self.root.right_child)

    def _print(self, node):
        if node:
            self._print(node.left_child)
            print (node.value)
            self._print(node.right_child)

if __name__ == '__main__':
    tree = Biniry_Search_Tree()
    tree.insert(5)
    tree.insert(6); tree.insert(4)
    print(tree)
    print (tree.search(5))
    print (tree.search(10))
    