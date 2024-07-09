package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("n k: ")
	text, _ := reader.ReadString('\n')
	split := strings.Split(text, " ")
	n, _ := strconv.Atoi(strings.Trim(split[0], "\n"))
	k, _ := strconv.Atoi(strings.Trim(split[1], "\n"))
	winner := findTheWinner(n, k)

	fmt.Printf("hello %v\n", winner)
}

type Node struct {
	Value int
	Next  *Node
	Prev  *Node
}

func initializeNodes(n int) *Node {
	var first Node = Node{
		Value: 1,
	}

	prev := &first
	var curr *Node = &first

	for idx := range n - 1 {
		curr = &Node{
			Prev:  prev,
			Value: idx + 2,
		}

		prev.Next = curr
		prev = curr
	}

	first.Prev = curr
	first.Prev.Next = &first

	return &first
}

func findTheWinner(n int, k int) int {
	fmt.Printf("findTheWinner(n: %v, k: %v)\n", n, k)

	nodes := n
	curr := initializeNodes(n)
	jumps := k - 1

	for nodes > 1 {

		for jumps > 0 {
			curr = curr.Next
			jumps--
		}

		curr.Prev.Next = curr.Next
		curr.Next.Prev = curr.Prev
		fmt.Printf("deleting: %v\n", curr.Value)
		curr = curr.Prev
		nodes--
		jumps = k
	}

	return curr.Value
}
