
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node [{self.value:^5}]'


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add_node(self, node):
        if self.root is None:
            self.root = node
        else:
            current = self.root
            while True:
                if node.value < current.value:
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right

    def get_height(self, node=None):
        if node is None:
            return 0

        height_left = self.get_height(node.left)
        height_right = self.get_height(node.right)

        if height_right < height_left:
            return 1 + height_left
        else:
            return 1 + height_right

    def print_tree_depth(self, node=None, parent=None, show_parent=True):
        if node is not None:
            print(f"{node} {parent if show_parent else ''}")
            self.print_tree_depth(node.left, node, show_parent=show_parent)
            self.print_tree_depth(node.right, node, show_parent=show_parent)

    def get_width(self, node, level=1):
        if node is None:
            return 0
        if level == 1:
            return 1
        if level > 1:
            return self.get_width(node.left, level - 1) + self.get_width(node.right, level - 1)

    def print_tree_width(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root, end=' ')
        elif level > 1:
            self.print_tree_width(root.left, level - 1)
            self.print_tree_width(root.right, level - 1)


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.value))
        print_tree(node.left, level + 1)


if __name__ == '__main__':
    t = Tree()

    value = (25, 15, 5, 17, 55, 35, 45, 65, 11, 13)
    for i in value:
        t.add_node(Node(i))
    b = Tree()

    print(b.get_height(b.root))
    print(t.get_height(t.root))
    t.print_tree_depth(t.root, show_parent=False)
    print()
    print(t.get_width(t.root, 3))
    t.print_tree_width(t.root, level=3)

    # for i in range(1, t.get_height(t.root) + 1):
    #     print(t.get_width(t.root, i))
