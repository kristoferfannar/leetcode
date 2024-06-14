package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Printf("isPalindrome(10): %v\n", isPalindrome(10))
	fmt.Printf("isPalindrome(121): %v\n", isPalindrome(121))
	fmt.Printf("isPalindrome(12): %v\n", isPalindrome(12))
}

// Solutions:
// 1. parse x into a string, reverse that string and compare the two
// 2. parse x into a string, compare idxs i and len(string) - i - 1 until halfway there
func isPalindrome(x int) bool {
	xStr := strconv.Itoa(x)

	for i := 0; i < len(xStr); i++ {
		if i*2 > len(xStr) {
			return true
		}

		if xStr[i] != xStr[len(xStr)-1-i] {
			return false
		}
	}

	return true
}
