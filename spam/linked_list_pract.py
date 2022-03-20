class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'{self.value}'


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __str__(self):
        item_values = []
        for item in self:
            item_values.append(str(item))
        item_values.append('None')
        return '->'.join(item_values)

    def add_node(self, node):
        if self.head is None:
            self.head = node
        else:
            item = None
            for item in self:
                continue
            item.next = node

    def get_item(self, order):
        temp = 1
        for item in self:
            if temp == order:
                return item
            temp += 1
        return f'No {order} item'

    def add_after(self, required_value, new_node):
        for item in self:
            if item.value == required_value:
                new_node.next = item.next
                item.next = new_node
                break

    def add_before(self, require_value, new_node):
        pass

    def check_if_values_correct(self):
        copy_head = self.head
        for i in self:
            print(i is copy_head)
            copy_head = copy_head.next


list_link = LinkedList()

values = [22, 15, 97, 7, 91, 61, 3, 79, 91, 5, 62]
for i in values:
    list_link.add_node(Node(i))

print(list_link)
list_link.add_after(91, Node(15))
list_link.add_after(7, Node(28))
print(list_link)
