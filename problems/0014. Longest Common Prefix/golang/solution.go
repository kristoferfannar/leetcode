package main

import (
	"fmt"
	"slices"
)

func main() {
	strs := []string{"hello", "world", "roger", "that", "alien"}
	common := longestCommonPrefix(strs)
	fmt.Printf("longestCommonPrefix(%v) = \"%s\"\n", strs, common)

	strs = []string{"hello", "hey", "helium"}
	common = longestCommonPrefix(strs)
	fmt.Printf("longestCommonPrefix(%v) = \"%s\"\n", strs, common)
}

// Sort the strings, by definition the first and the last strings must have the worst (shortest) common prefix
// therefore, we only have to compare their prefixes
func longestCommonPrefix(strs []string) string {
	slices.Sort(strs)

	common := ""

	first, last := strs[0], strs[len(strs)-1]
	for i := 0; i < min(len(first), len(last)); i++ {
		if first[i] != last[i] {
			break
		}
		common += string(first[i])
	}

	return common
}
