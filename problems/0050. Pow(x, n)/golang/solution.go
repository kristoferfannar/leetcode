package main

import "fmt"

func main() {
	fmt.Printf("myPow(2.1, 3): %v\n", myPow(2.1, 3))
	fmt.Printf("myPow(2.0, -2): %v\n", myPow(2.0, -2))
	fmt.Printf("myPow(1.0, 200000): %v\n", myPow(1.0, 200000))
	fmt.Printf("myPow(2.0, 12): %v\n", myPow(2.0, 12))
	fmt.Printf("myPow(2.0, 4): %v\n", myPow(2.0, 4))
}

// Solutions
// 1. multiply pow with x n times...
// 2. square pow log(n) times, repeat with remainder. Sum results...
func myPow(x float64, n int) float64 {
	negative := n < 0
	answer := 1.0
	left := n

	if negative {
		left = -n
	}

	// run while there's an exponent left
	for left > 0 {
		pwr := x
		rem, jmps := findHighestPowerOfTwo(left)
		for i := 0; i < jmps; i++ {
			// square result as many times as possible
			pwr *= pwr
		}
		left = rem
		answer *= pwr
	}

	if negative {
		return 1 / answer
	}

	return answer
}

func findHighestPowerOfTwo(n int) (int, int) {
	pwr := 1
	jumps := 0

	for pwr <= n {
		pwr *= 2
		jumps++
	}
	return n - pwr/2, jumps - 1
}
