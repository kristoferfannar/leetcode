package main

import (
	"fmt"
	"slices"
)

func main() {
	fmt.Printf("minIncrementForUnique([]int{1, 3, 2}): %v\n", minIncrementForUnique([]int{1, 3, 2}))
	fmt.Printf("minIncrementForUnique([]int{1, 3, 1}): %v\n", minIncrementForUnique([]int{1, 3, 1}))
	fmt.Printf("minIncrementForUnique([]int{1, 3, 1, 3}): %v\n", minIncrementForUnique([]int{1, 3, 1, 3}))

	fmt.Printf("minIncrementForUnique([]int{3,2,1,2,1,7}): %v\n", minIncrementForUnique([]int{3, 2, 1, 2, 1, 7})) //  [1 1 2 2 3 7]
}

func minIncrementForUnique(nums []int) int {
	slices.Sort(nums)

	lastValue := nums[0]
	moves := 0

	for i := 1; i < len(nums); i++ {
		if nums[i] <= lastValue {
			newVal := lastValue + 1
			moves += newVal - nums[i]
			lastValue = newVal
		} else {
			lastValue = nums[i]
		}
	}

	return moves
}
