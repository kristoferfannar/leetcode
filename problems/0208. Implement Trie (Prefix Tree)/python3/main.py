class Node:
    def __init__(self, word, i=0) -> None:
        self.next = dict()
        self.end = i == len(word) - 1


class Trie:
    def __init__(self):
        self.tree = dict()

    def insert(self, word: str) -> None:
        cur = self.tree

        for i, char in enumerate(word):
            if char not in cur:
                cur[char] = Node(word, i)

            if i == len(word) - 1:
                cur[char].end = True

            cur = cur[char].next

    def search(self, word: str) -> bool:
        cur_node = self
        cur = self.tree

        for char in word:
            if char not in cur:
                return False
            cur_node = cur[char]
            cur = cur_node.next

        return cur_node == self or cur_node.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.tree

        for char in prefix:
            if char not in cur:
                return False
            cur = cur[char].next

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    t = Trie()
    assert not t.search("hello")
    t.insert("hello")
    assert t.search("hello")
    assert not t.search("hellothere")
    assert t.startsWith("he")
    assert t.startsWith("hello")
    assert t.startsWith("")
    # what happens here
    assert t.search("")
    t.insert("")
    assert t.search("")

    t = Trie()
    assert not t.startsWith("a")
    t.insert("apple")
    assert t.search("apple")
    assert not t.search("app")
    assert t.startsWith("app")
    t.insert("app")
    assert t.search("app")
