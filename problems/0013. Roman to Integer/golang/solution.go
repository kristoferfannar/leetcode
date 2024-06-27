package main

import "fmt"

func main() {

	fmt.Printf("romanToInt(\"MCMXCIV\") == %d", romanToInt("MCMXCIV"))
}

var mapper = map[rune]int{rune('I'): 1, rune('V'): 5, rune('X'): 10, rune('L'): 50, rune('C'): 100, rune('D'): 500, rune('M'): 1000}

// Start at the last rune and iterate until at first rune
// Decrease the total value if the current rune (position i), is lower than the last (position i+1)
// Else, increase the total value by the amount specified by the rune
func romanToInt(s string) int {
	value := 0

	r := []rune(s)
	last := r[len(r)-1]
	for i := len(r) - 1; i >= 0; i-- {
		curr := r[i]

		if mapper[curr] >= mapper[last] {
			value += mapper[curr]
		} else {
			value -= mapper[curr]
		}

		last = curr
	}

	return value
}
