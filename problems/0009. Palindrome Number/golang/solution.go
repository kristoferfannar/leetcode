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

func isPalindrome(x int) bool {
	xStr := strconv.Itoa(x)
	var xRev string

	for i := len(xStr) - 1; i >= 0; i-- {
		xRev += string(xStr[i])
	}

	for i := 0; i < len(xStr); i++ {
		if xStr[i] != xRev[i] {
			return false
		}
	}
	return true
}
