package main

import (
	"fmt"
	"sort"
)

func twoSum(nums []int, target int) []int {
	// return slices.twoSum(nums, target) // oops

	// create a sorted copy of the original array
	// containing value-index pairs
	sorted := [][2]int{}

	for i, num := range nums {
		sorted = append(sorted, [2]int{num, i})
	}

	sort.Slice(sorted, func(a, b int) bool { return sorted[a][0] < sorted[b][0] })

	for x := 0; x < len(sorted); x++ {
		for y := x + 1; y < len(sorted); y++ {
			// if the values match...
			if sorted[x][0]+sorted[y][0] == target {
				// ... return the indices
				return []int{sorted[x][1], sorted[y][1]}
			}
		}
	}

	panic("no solution found")
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	ans := twoSum(nums, target)
	fmt.Printf("ans: %v\n", ans)

	nums = []int{2, 5, 5, 11}
	target = 10
	ans = twoSum(nums, target)
	fmt.Printf("twoSum(%v, %d) = %v\n", nums, target, ans)
}
