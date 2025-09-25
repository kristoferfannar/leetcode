from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def ln(lis):
    l = ListNode(lis[0])
    prev = l

    for i in range(1, len(lis)):
        curr = ListNode(lis[i])
        prev.next = curr
        prev = curr

    return l


def lis(l: Optional[ListNode]):
    li = []
    while l:
        li.append(l.val)
        l = l.next
    return li


class Solution:
    def rm(self, node: ListNode) -> Optional[ListNode]:
        if node.next is None:
            return node

        new_next = self.rm(node.next)
        node.next = new_next

        if node.next and node.next.val > node.val:
            return node.next

        return node

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        return self.rm(head)


if __name__ == "__main__":
    org = [1, 2, 3, 4]
    assert lis(ln(org)) == org

    s = Solution()
    got = lis(s.removeNodes(ln([5, 2, 13, 3, 8])))
    exp = [13, 8]

    # print(f"got: {got}")
    # print(f"exp: {exp}")
    assert got == exp
