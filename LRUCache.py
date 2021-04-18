class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.data = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if self.data.get(key):
            node = self.data.get(key)
            self.remove_node(node)
            self.append_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.data.get(key):
            node = self.data[key]
            self.remove_node(node)
            node.val = value
        else:
            node = ListNode(key, value)
            self.data[key] = node
            if self.size < self.capacity:
                self.size += 1
            else:
                key = self.remove_tail()
                del self.data[key]
        self.append_head(node)

    def remove_node(self, node):
        pre_node = node.pre
        next_node = node.next
        pre_node.next, next_node.pre = next_node, pre_node

    def append_head(self, node):
        head_next = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = head_next
        head_next.pre = node

    def remove_tail(self) -> int:
        key = self.tail.pre.key
        self.remove_node(self.tail.pre)
        return key
