from random import randint
import heapq


class RandomizedCollection:
    def __init__(self):
        self.vals = []
        self.idx: dict[int, list[int]] = dict()

    def insert(self, val: int) -> bool:
        if val not in self.idx:
            self.idx[val] = [-len(self.vals)]
        else:
            heapq.heappush(self.idx[val], -len(self.vals))

        self.vals.append(val)

        return len(self.idx[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False

        val_idx = -heapq.heappop(self.idx[val])
        if len(self.idx[val]) == 0:
            del self.idx[val]

        # the value we popped is the actual last value
        if val_idx == len(self.vals) - 1:
            self.vals.pop()
            return True

        # replace with actual last value
        last = self.vals[-1]
        heapq.heappop(self.idx[last])
        self.vals[val_idx] = last
        heapq.heappush(self.idx[last], -val_idx)

        self.vals.pop()

        return True

    def getRandom(self) -> int:
        rand_idx = randint(0, len(self.vals) - 1)

        return self.vals[rand_idx]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == "__main__":
    rc = RandomizedCollection()
    assert rc.insert(10)
    assert not rc.insert(10)
    assert rc.insert(20)
    assert not rc.insert(20)
    assert rc.insert(30)
    assert not rc.insert(30)
    assert rc.remove(10)
    assert rc.remove(10)
    assert rc.remove(30)
    assert rc.remove(30)
