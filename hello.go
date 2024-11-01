package main

import (
	"fmt"
	"time"
)

func collatzCount(n int) int {
	i := 1
	for n > 1 {
		if n%2 == 0 {
			n /= 2
		} else {
			n = 3*n + 1
		}
		i++
	}
	return i
}

func main() {
	start := time.Now() // Start time tracking

	maxCollatz := 0
	for i := 1; i < 1000000; i++ {
		count := collatzCount(i)
		if count > maxCollatz {
			maxCollatz = count
		}
	}

	elapsed := time.Since(start) // Calculate elapsed time
	fmt.Printf("Maximum Collatz count: %d\n", maxCollatz)
	fmt.Printf("Execution time: %s\n", elapsed)
}
