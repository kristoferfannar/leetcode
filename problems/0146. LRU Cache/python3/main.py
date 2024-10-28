class Node:
    def __init__(self, key, value, prev=None, next=None) -> None:
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

        # point to yourself if you're alone
        if not prev:
            self.prev = self
        if not next:
            self.next = self

    def __repr__(self) -> str:
        return f"|{self.key}, {self.value}|"


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.nodes = None
        self.lookup = dict()

    def __repr__(self) -> str:
        final = ""
        first = self.nodes
        curr = first.next
        final += str(first)

        while curr.key != first.key:
            final += f" <-> {curr}"
            curr = curr.next

        return final

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1

        node = self.lookup[key]
        self.add_to_top(node)

        return node.value

    def add_to_top(self, node):
        # node is alredy on top
        if node == self.nodes.prev:
            return
        if node == self.nodes:
            self.nodes = node.next
            return

        # remove node from old pos
        node.prev.next = node.next
        node.next.prev = node.prev

        # link prev <-> node
        prev = self.nodes.prev
        prev.next = node
        node.prev = prev
        # link node <-> oldest
        node.next = self.nodes
        self.nodes.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            node.value = value
            self.add_to_top(node)
            return

        node = Node(key, value)
        self.lookup[key] = node

        self.size += 1
        if self.size == 1:
            self.nodes = node
            return

        assert self.nodes is not None

        self.add_to_top(node)

        if self.size > self.capacity:
            # delete oldest
            oldest = self.nodes
            oldest.prev.next = oldest.next
            oldest.next.prev = oldest.prev
            self.nodes = oldest.next
            del self.lookup[oldest.key]
            self.size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == "__main__":
    lru = LRUCache(capacity=4)
    assert lru.get(0) == -1
    lru.put(0, 1001)
    assert lru.size == 1
    assert lru.get(0) == 1001
    lru.put(1, 1001)
    lru.put(2, 1001)
    lru.put(3, 1001)
    lru.put(4, 1001)
    assert lru.size == 4
    assert lru.get(0) == -1
    assert lru.get(1) == 1001
    lru.put(5, 1002)
    assert lru.get(1) == 1001
    assert lru.get(2) == -1

    lru = LRUCache(capacity=2)
    lru.put(2, 1)
    lru.put(2, 2)
    assert lru.get(2) == 2
    lru.put(1, 1)
    lru.put(4, 1)
    assert lru.get(2) == -1
