package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func arrToListNode(arr []int) *ListNode {
	if len(arr) == 0 {
		return nil
	}

	return &ListNode{arr[0], arrToListNode(arr[1:])}
}

func main() {
	l1 := arrToListNode([]int{2, 4, 3})
	l2 := arrToListNode([]int{5, 6, 4})
	fmt.Printf("addTwoNumbers(l1, l2): %v\n", addTwoNumbers(l1, l2))

	l1 = arrToListNode([]int{0})
	l2 = arrToListNode([]int{0})

	fmt.Printf("addTwoNumbers(l1, l2): %v\n", addTwoNumbers(l1, l2))
}

func addTwoNumbers(l1, l2 *ListNode) *ListNode {
	ans := &ListNode{}
	curr := ans
	carried := 0

	for l1 != nil && l2 != nil {
		newVal := l1.Val + l2.Val + carried
		carried = newVal / 10
		newVal %= 10
		new := &ListNode{newVal, nil}
		curr.Next = new
		curr = new
		l1, l2 = l1.Next, l2.Next
	}

	left := l1
	if l1 == nil {
		left = l2
	}

	for left != nil {
		newVal := left.Val + carried
		carried = newVal / 10
		newVal %= 10
		new := &ListNode{newVal, nil}
		curr.Next = new
		curr = new
		left = left.Next
	}

	if carried > 0 {
		new := &ListNode{carried, nil}
		curr.Next = new
	}

	return ans.Next
}
