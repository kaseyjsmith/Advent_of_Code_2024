package main

import (
	// "bufio"
	// "std"
	// "io"
	"fmt"
	"os"
	"strings"
)

// read in file
// helper function for error checking
func check(e error) {
	if e != nil {
		panic(e)
	}
}

func read(file string) *string {
	data, err := os.ReadFile(file)
	check(err)
	var dataString = string(data)
	fmt.Println(strings.Split(dataString, "\t"))
	return &dataString
}

// create right and left lists
func assembleLists(dataString *string) [][]string {
	mainList := strings.Split(*dataString, "\t")
	var listOne = []int
	var listTwo = []int
	for idx, elem := range mainList {
		switch {
			case idx % 2 == 0:

		}

	}
	return splitLists
}

// sort right and left lists

// find the running sum of the  distance between lists 

func main() {
	read("puzzle.txt")
}
