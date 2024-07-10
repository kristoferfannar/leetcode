package main

import "fmt"

func main() {
	minOperations([]string{"d1/", "d2/", "./", "d3/", "../", "d31/"})
	minOperations([]string{"d1/", "../", "../", "../"})
	minOperations([]string{"./", "../", "./"})
}

func minOperations(logs []string) int {
	fmt.Printf("minOperations(logs: %v)", logs)

	operations := 0

	for _, log := range logs {
		if log == "./" {
			continue
		}

		if log == "../" {
			operations = max(operations-1, 0)
		} else {
			operations++
		}

	}

	fmt.Printf(" = %d\n", operations)
	return operations
}
