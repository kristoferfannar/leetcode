package main

import "fmt"

func main() {
	fmt.Printf("myPow(2.1, 3): %v\n", myPow(2.1, 3))
	fmt.Printf("myPow(2.0, -2): %v\n", myPow(2.0, -2))
}

// Solutions
// 1. multiply pow with x n times...
// 2. square pow log(n) times...
func myPow(x float64, n int) float64 {
	var pow float64 = 1
	exp := n

	if n < 0 {
		exp = -n
	}

	for i := 0; i < exp; i++ {
		pow *= x
	}

	if exp != n {
		return 1 / pow
	}
	return pow
}
