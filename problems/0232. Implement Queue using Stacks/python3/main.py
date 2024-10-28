class MyQueue:
    def __init__(self):
        self.oldest = []
        self.rest = []

    def push(self, x: int) -> None:
        if not self.oldest:
            self.oldest.append(x)
        else:
            self.rest.append(x)

    def pop(self) -> int:
        ret = self.oldest.pop()

        # get the second oldest, now the oldest element
        # buried on the bottom of the stack
        while len(self.rest) > 1:
            self.oldest.append(self.rest.pop())

        new_oldest = None
        if self.rest:
            new_oldest = self.rest.pop()

        while self.oldest:
            self.rest.append(self.oldest.pop())

        if new_oldest:
            self.oldest.append(new_oldest)

        return ret

    def peek(self) -> int:
        return self.oldest[0]

    def empty(self) -> bool:
        return not self.oldest


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


if __name__ == "__main__":
    mq = MyQueue()
    assert mq.empty()
    mq.push(1)
    assert not mq.empty()
    mq.push(2)
    assert mq.peek() == 1
    mq.push(3)
    mq.push(4)
    mq.push(5)
    assert mq.pop() == 1
    p = mq.peek()
    assert p == 2
    assert mq.pop() == 2
    assert mq.pop() == 3
    mq.push(6)
    assert mq.pop() == 4
    assert mq.pop() == 5
    assert not mq.empty()
    assert mq.pop() == 6
    assert mq.empty()
