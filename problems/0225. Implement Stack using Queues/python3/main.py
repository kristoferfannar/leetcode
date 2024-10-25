from queue import Queue


class MyStack:
    def __init__(self):
        self.last: Queue[int] = Queue()
        self.rest: Queue[int] = Queue()

    def push(self, x: int) -> None:
        # move last item to rest
        if not self.last.empty():
            last = self.last.get()
            self.rest.put(last)

        self.last.put(x)

    def pop(self) -> int:
        last = self.last.get()

        if not self.rest.empty():
            item = self.rest.get()
            while not self.rest.empty():
                self.last.put(item)
                item = self.rest.get()

            # put item back to rest
            # this will now be in front of last
            self.rest.put(item)

        self.last, self.rest = self.rest, self.last

        return last

    def top(self) -> int:
        # pretty stupid, but this Queue
        # doesn't allow for peeking
        last = self.last.get()
        self.last.put(last)

        return last

    def empty(self) -> bool:
        # last should never be empty if there are any items
        return self.last.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

if __name__ == "__main__":
    ms = MyStack()
    ms.push(1)
    ms.push(2)

    assert ms.pop() == 2
    assert ms.empty() == False
    assert ms.top() == 1
    assert ms.pop() == 1
    assert ms.empty() == True
