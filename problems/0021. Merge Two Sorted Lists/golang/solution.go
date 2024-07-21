package main

import "fmt"

func main() {
	var list1, list2, merged *ListNode

	list1 = &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: nil}}
	list2 = &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: nil}}}
	merged = mergeTwoLists(list1, list2)
	fmt.Printf("list1: %v, list2: %v = merged: %v\n", list1.toString(), list2.toString(), merged.toString())

	list1 = &ListNode{}
	list2 = &ListNode{}
	merged = mergeTwoLists(list1, list2)
	fmt.Printf("list1: %v, list2: %v = merged: %v\n", list1.toString(), list2.toString(), merged.toString())

	list1 = nil
	list2 = nil
	merged = mergeTwoLists(list1, list2)
	fmt.Printf("list1: %v, list2: %v = merged: %v\n", list1.toString(), list2.toString(), merged.toString())

	list1 = nil
	list2 = &ListNode{Val: 12}
	merged = mergeTwoLists(list1, list2)
	fmt.Printf("list1: %v, list2: %v = merged: %v\n", list1.toString(), list2.toString(), merged.toString())

	list1 = nil
	list2 = &ListNode{Val: 0}
	merged = mergeTwoLists(list1, list2)
	fmt.Printf("list1: %v, list2: %v = merged: %v\n", list1.toString(), list2.toString(), merged.toString())

}

type ListNode struct {
	Val  int
	Next *ListNode
}

func (l *ListNode) toString() (listStr string) {
	curr := l

	listStr += "["

	if curr == nil {
		listStr += "]"
		return
	}

	for curr.Next != nil {
		listStr += fmt.Sprintf("%v, ", curr.Val)
		curr = curr.Next
	}

	listStr += fmt.Sprintf("%d]", curr.Val)

	return
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	merged := &ListNode{}
	curr := merged

	if list1 == nil && list2 == nil {
		return nil
	}

	for list1 != nil || list2 != nil {
		curr.Next = &ListNode{}

		// list1 is empty, append the rest of list2
		if list1 == nil && list2 != nil {
			curr.Val = list2.Val
			curr.Next = list2.Next
			list2 = nil

			// list2 is empty, append the rest of list1
		} else if list2 == nil && list1 != nil {
			curr.Val = list1.Val
			curr.Next = list1.Next
			list1 = nil

			// neither is empty, but list1 is lower
		} else if list1.Val < list2.Val {
			curr.Val = list1.Val
			list1 = list1.Next

			// neither is empty, but list2 is lower
		} else {
			curr.Val = list2.Val
			list2 = list2.Next

		}
		curr = curr.Next
	}

	return merged
}
