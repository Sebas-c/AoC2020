package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	input := fileRead("../Inputs/Day10-input.txt")
	joltageDifference := joltageDifference(input)
	if joltageDifference == 0 {
		fmt.Println("Whoopsie daisy, an error occured")
	} else {
		fmt.Printf("The joltage difference is: %v\n", joltageDifference)
	}

	// Arrays given as part of the problem for testing (will work with the recursive solution since the data set is significantly smaller)
	// input = []int{28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3}
	// sort.Ints(input)
	// input = []int{ 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19}
	// Appending plane's outlet and personal device's adaptor
	input = append([]int{0}, input...)
	input = append(input, input[len(input)-1]+3)

	// Recursive solution, only good if you're fine waiting about a month
	// totalBranches := totalBranchesRecursive(input, 0)
	// if totalBranches == 0 {
	// 	fmt.Println("Whoopsie daisy, an error occured")
	// } else {
	// 	fmt.Printf("Total possible paths: %v\n", totalBranches)
	// }

	totalBranches := totalBranches(input)
	if totalBranches == 0 {
		fmt.Println("Whoopsie daisy, an error occured")
	} else {
		fmt.Printf("Total possible paths: %v\n", totalBranches)
	}
}

// Solution based on a comment by reddit user u/Nunki3 (https://www.reddit.com/r/adventofcode/comments/kacdbl/2020_day_10c_part_2_no_clue_how_to_begin/gf9lzhd/)
func totalBranches(input []int) int {
	// creating a slice to hold all paths leading to each number and setting first one as 1
	totalBranches := make([]int, len(input))
	totalBranches[0] = 1

	//Looping through all adaptors
	for i := 0; i < len(input)-1; i++ {
		// If current adaptor can reach one of the next three, add its number of path to it
		for j := i + 1; j < i+4; j++ {
			if j <= len(input)-1 && input[j]-input[i] <= 3 {
				totalBranches[j] += totalBranches[i]
			}
		}
	}
	// Return number of path for the last adaptor (device's charging outlet)
	return totalBranches[len(input)-1]
}

// Recursive solution
func totalBranchesRecursive(input []int, index int) int {
	if index == len(input)-2 {
		return 1
	} else {
		children := 0
		for i := index + 1; i < index+4 && i < len(input)-1; i++ {
			if input[i]-input[index] <= 3 {
				children += totalBranchesRecursive(input, i)
			}
		}
		return children
	}
}

func joltageDifference(input []int) int {
	// Counters
	ones := 0
	threes := 0
	// Ordering the adapters
	sort.Ints(input)
	// Appending plane's outlet and personal device's adaptor
	input = append([]int{0}, input...)
	input = append(input, input[len(input)-1]+3)

	for i := 0; i < len(input)-1; i++ {
		diff := input[i+1] - input[i]
		if diff < 2 {
			ones++
		} else if diff > 2 {
			threes++
		}
	}
	return ones * threes
}

// Returns the file's content
func fileRead(filePath string) []int {
	// Variables
	var input []int

	// Opening the file
	file, errFile := os.Open(filePath)

	checkError(errFile)

	// Creating a scanner and setting it to read line by line
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	// Appending every line
	for scanner.Scan() {
		line, errConversion := strconv.Atoi(scanner.Text())
		checkError(errConversion)
		input = append(input, line)
	}

	// Closing the file
	file.Close()

	return input
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
