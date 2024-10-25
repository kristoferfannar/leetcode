class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:

        curr_min = val
        if len(self.stack) != 0:
            last_min = self.stack[-1][1]
            curr_min = min(last_min, val)

        self.stack.append((val, curr_min))

    def pop(self) -> None:
        # last = (val, min)
        last = self.stack.pop()
        return last[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    ms = MinStack()

    ms.push(1)
    ms.push(2)
    ms.push(3)
    ms.pop()
    assert ms.top() == 2
    assert ms.getMin() == 1
