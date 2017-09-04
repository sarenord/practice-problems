package main

import (
	"strings"
	"os"
	"fmt"
)

func main() {
	counter := 0
	inp := os.Args[1]
	var plc []string
	plc = strings.Split(inp, "")
	var plc_inverse []string
	fmt.Println(plc_inverse)
	for i := 1; i <= (len(plc)); i++ {
	plc_inverse = append(plc_inverse, plc[len(plc)-i])
	fmt.Println(plc_inverse)
	}
	for in, v := range plc {
		if v == plc_inverse[in]{
			counter++
		}
	}
	if counter == len(plc){ 
		fmt.Println(inp + " is a palindrome!")
	} else { 
		fmt.Println(inp + " is not a palindrome")
	}
}
