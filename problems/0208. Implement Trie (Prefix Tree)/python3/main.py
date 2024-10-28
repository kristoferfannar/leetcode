class Node:
    def __init__(self, word, i=0) -> None:
        self.end = False
        self.next = dict()

        if i < len(word) - 1:
            self.next[word[i + 1]] = Node(word, i + 1)
        else:
            self.end = True

    def insert(self, word, i=0):
        if i == len(word) - 1:
            self.end = True
            return

        elif word[i + 1] not in self.next:
            self.next[word[i + 1]] = Node(word, i + 1)
            return

        else:
            self.next[word[i + 1]].insert(word, i + 1)
            return

    def exists(self, word, i=0):
        if i == len(word) - 1 and self.end:
            return True

        if i + 1 < len(word) and word[i + 1] in self.next:
            return self.next[word[i + 1]].exists(word, i + 1)

        return False

    def prefix(self, word, i=0):
        if i == len(word) - 1:
            return True

        if word[i + 1] not in self.next:
            return False

        return self.next[word[i + 1]].prefix(word, i + 1)


class Trie:
    def __init__(self):
        self.tree = dict()

    def insert(self, word: str) -> None:
        if not word:
            return

        if word[0] in self.tree:
            self.tree[word[0]].insert(word)
        else:
            # will initialize the word in the tree
            self.tree[word[0]] = Node(word)

    def search(self, word: str) -> bool:
        # word is empty
        if not word:
            return True

        if word[0] not in self.tree:
            return False

        return self.tree[word[0]].exists(word)

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True

        if prefix[0] not in self.tree:
            return False

        return self.tree[prefix[0]].prefix(prefix)


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
