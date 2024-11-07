package main

import (
	"fmt"
	"time"
)

func start(gridX, gridY int) int {
	var forward func(posX, posY int) int
	forward = func(posX, posY int) int {
		x, y := 0, 0
		if posX < gridX {
			x = forward(posX+1, posY)
		}
		if posY < gridY {
			y = forward(posX, posY+1)
		}

		if x == 0 && y == 0 {
			return 1
		}
		return x + y
	}
	return forward(0, 0)
}

func square(size int) int {
	return start(size, size)
}

func main() {
	for i := 1; i <= 20; i++ {
		startTime := time.Now()
		result := square(i)
		fmt.Printf("Size: %d, Result: %d, Time: %v seconds\n", i, result, time.Since(startTime).Seconds())
	}
	fmt.Println("Done")
}