from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"LN({self.val}, {str(self.next)})"


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        codds = head
        evens = head.next
        cevens = evens

        while True:
            if not cevens.next:
                break
            codds.next = cevens.next
            codds = codds.next

            if not codds.next:
                break
            cevens.next = codds.next
            cevens = cevens.next

        # append evens after last odd
        cevens.next = None
        codds.next = evens

        return head


def toLn(lis):
    if not lis:
        return None

    head = ListNode(lis[0])
    prev = head

    for num in lis[1:]:
        curr = ListNode(num)
        prev.next = curr
        prev = curr

    return head


def fromLn(ln):
    lis = []
    if not ln:
        return lis

    curr = ln
    while curr:
        lis.append(curr.val)
        curr = curr.next

    return lis


if __name__ == "__main__":
    assert fromLn(toLn([1, 2, 3])) == [1, 2, 3]
    s = Solution().oddEvenList(toLn([1, 2, 3, 4, 5]))
    lis = fromLn(s)
    assert lis == [1, 3, 5, 2, 4]

    assert fromLn(Solution().oddEvenList(toLn([2, 1, 3, 5, 6, 4, 7]))) == [
        2,
        3,
        6,
        7,
        1,
        5,
        4,
    ]
