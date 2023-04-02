package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b, c float64
	fmt.Scan(&a) //teihen
	fmt.Scan(&b)
	fmt.Scan(&c)
	c = c * math.Pi / 180

	s := a * b * math.Sin(c) / 2
	l := a + b + math.Sqrt(math.Pow(a, 2)+math.Pow(b, 2)-2*a*b*math.Cos(c))
	h := b * math.Sin(c)

	fmt.Printf("%f\n%f\n%f\n", s, l, h)
}
