# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def get_next(self, ni: NestedInteger) -> list[int]:
        curr = []

        if ni.isInteger():
            curr.append(ni.getInteger())
        else:
            for n in ni.getList():
                curr.extend(self.get_next(n))

        return curr

    def __init__(self, nestedList: [NestedInteger]):
        self.lis = []
        self.curr = 0

        for ns in nestedList:
            self.lis.extend(self.get_next(ns))

    def next(self) -> int:
        tmp = self.lis[self.curr]
        self.curr += 1
        return tmp

    def hasNext(self) -> bool:
        return self.curr < len(self.lis)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
