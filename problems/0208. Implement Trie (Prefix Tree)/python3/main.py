from typing import Optional


def idx(char: str) -> int:
    assert len(char) == 1
    return ord(char) - ord("a")


class Node:
    def __init__(self, word, i=0) -> None:
        self.end = False
        self.next: list[Optional[Node]] = [None] * 26

        if i < len(word) - 1:
            next = Node(word, i + 1)
            self.next[idx(word[i + 1])] = next
        else:
            self.end = True

    def insert(self, word, i=0):
        if i == len(word) - 1:
            self.end = True
            return

        elif self.next[idx(word[i + 1])] is None:
            node = Node(word, i + 1)
            self.next[idx(word[i + 1])] = node
            return

        else:
            self.next[idx(word[i + 1])].insert(word, i + 1)
            return

    def exists(self, word, i=0):
        if i == len(word) - 1 and self.end:
            return True

        if i + 1 < len(word) and self.next[idx(word[i + 1])] is not None:
            return self.next[idx(word[i + 1])].exists(word, i + 1)

        return False

    def prefix(self, word, i=0):
        if i == len(word) - 1:
            return True

        if self.next[idx(word[i + 1])] is None:
            return False

        return self.next[idx(word[i + 1])].prefix(word, i + 1)


class Trie:
    def __init__(self):
        self.tree: list[Optional[Node]] = [None] * 26

    def insert(self, word: str) -> None:
        if not word:
            return

        if self.tree[idx(word[0])] is not None:
            self.tree[idx(word[0])].insert(word)
        else:
            # will initialize the word in the tree
            self.tree[idx(word[0])] = Node(word)

    def search(self, word: str) -> bool:
        # word is empty
        if not word:
            return True

        if self.tree[idx(word[0])] is None:
            return False

        return self.tree[idx(word[0])].exists(word)

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True

        if self.tree[idx(prefix[0])] is None:
            return False

        return self.tree[idx(prefix[0])].prefix(prefix)


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
    t.insert("apple")
    assert t.search("apple")
    assert not t.search("app")
    assert t.startsWith("app")
    t.insert("app")
    assert t.search("app")
