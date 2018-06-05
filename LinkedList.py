
class LinkedNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __eq__(self, that):
        if self.val == that.val:
            return True


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def _append_item(self, item):
        return LinkedNode(item)

    def append(self, new_item):
        if not self.tail:
            self.head = self._append_item(new_item)
            self.tail = self.head
        else:
            self.tail.next = self._append_item(new_item)
            self.tail = self.tail.next

    def _find(self, tg_node, idx):
        node = self.head
        pre_node = None
        if tg_node:
            while not tg_node == node.val:
                pre_node = node
                node = node.next
            else:
                return (pre_node, node)
        else:
            cnt = 0
            while node.next:
                if cnt == idx:
                    return (pre_node, node)
                pre_node = node
                node = node.next
                cnt += 1
            else:
                return (pre_node, node)

    def insert(self, new_item=None, tg_item=None, idx=-1, loc='after'):
        if not self.head:
            return None

        pre_node, node = self._find(tg_item, idx)
        new_node = self._append_item(new_item)
        if loc == 'after':
            new_node.next = node.next
            node.next = new_node
        elif loc == 'before':
            if pre_node:
                pre_node.next = new_node
                new_node.next = node
            else:  # 如果insert在第一筆前面要變成head
                new_node.next = self.head
                self.head = new_node
        else:
            return None

    def delete(self, tg_item=None, idx=-1):
        if not self.head:
            return None

        if self.size() < idx + 1 and not idx == -1:
            return None

        pre_node, node = self._find(tg_item, idx)
        if pre_node:
            pre_node.next = node.next
        else:
            self.head = node.next

    def size(self):
        size = 1
        if not self.head:
            return 0
        else:
            node = self.head
            while node.next:
                node = node.next
                size += 1

            return size

    def __str__(self):
        items = []
        node = self.head
        while node is not None:
            items.append(node.val)
            node = node.next

        return str(items)


if __name__ == '__main__':
    item = 3
    singlylist = SinglyLinkedList()
    singlylist.append(item)
    singlylist.append(4)
    singlylist.append(5)
    singlylist.insert(new_item=7, tg_item=4, loc='before')
    singlylist.delete(4)
    singlylist.insert(new_item=8, idx=0, loc="before")
    singlylist.delete(idx=0)
    singlylist.delete(3)
    print(singlylist.size())
    # singlylist.delete(idx=10)
    print(singlylist)
