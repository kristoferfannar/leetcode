from typing import Optional

from math import gcd


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"LN({self.val}, {self.next})"


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:

        curr = head

        while curr and curr.next:
            g = gcd(curr.val, curr.next.val)
            new = ListNode(g, curr.next)
            curr.next = new
            curr = new.next

        return head


def to_ln(lis):
    if not lis:
        return None

    first = ListNode(lis[0])
    last = first
    for l in lis[1:]:
        ln = ListNode(l)
        last.next = ln
        last = ln

    return first


def from_ln(ln):
    lis = []

    curr = ln
    while curr:
        lis.append(curr.val)
        curr = curr.next

    return lis


if __name__ == "__main__":
    assert from_ln(Solution().insertGreatestCommonDivisors(to_ln([18, 6, 10, 3]))) == [
        18,
        6,
        6,
        2,
        10,
        1,
        3,
    ]

    assert from_ln(Solution().insertGreatestCommonDivisors(to_ln([7]))) == [7]
