import heapq


class MedianFinder:
    def __init__(self):
        # holds the larger half
        # numbers' negative value must be added to this heap to create a min_heap
        # as heapq only supports max heaps
        self.min_heap = []
        # holds the smaller half
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= self.max_heap[0]:
            heapq.heappush(self.min_heap, -num)
        else:
            heapq.heappush(self.max_heap, num)

        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        elif len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # the difference in sizes between max and min should always be none,
        # or the max_heap should have one more element than the min heap
        assert 0 <= len(self.max_heap) - len(self.min_heap) <= 1

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.min_heap[0] + self.max_heap[0]) / 2

        return self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(2)
    mf.addNum(3)
    mf.addNum(4)
    assert mf.findMedian() == 3
    mf.addNum(9)
    r = mf.findMedian()
    print(r)
    assert r == 3.5
