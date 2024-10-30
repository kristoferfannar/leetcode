from random import randint


class RandomizedSet:
    def __init__(self):
        self.vals = []
        self.idxs = dict()
        pass

    def insert(self, val: int) -> bool:
        if val in self.idxs:
            return False

        self.idxs[val] = len(self.vals)
        self.vals.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.idxs:
            return False

        last = self.vals[-1]
        curr_idx = self.idxs[val]

        self.vals[curr_idx] = last
        self.idxs[last] = curr_idx
        del self.idxs[val]

        self.vals.pop()

        return True

    def getRandom(self) -> int:
        rand_idx = randint(0, len(self.vals) - 1)
        return self.vals[rand_idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == "__main__":
    rs = RandomizedSet()
    assert rs.insert(1)
    assert not rs.remove(2)
    assert rs.insert(2)
    assert rs.getRandom() == 2
    assert rs.remove(1)
    assert not rs.insert(2)
    assert rs.getRandom() == 2
