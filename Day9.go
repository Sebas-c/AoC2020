package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	input := fileRead("../Inputs/Day9-input.txt")

	ruleBreaker := findRuleBreakingNumber(input)
	if ruleBreaker != 0 {
		fmt.Printf("First number to break the rule: %v\n", ruleBreaker)
	} else {
		fmt.Printf("Whoopsie daisy, an error occured\n")
	}

	encryptionWeakness := breakEncryption(input, ruleBreaker)
	if encryptionWeakness != 0 {
		fmt.Printf("Encryption weakness: %v\n", encryptionWeakness)
	} else {
		fmt.Printf("Whoopsie daisy, an error occured\n")
	}
}

func breakEncryption(input []int, key int) int {
	tempValue := 0

	for i := 0; i < len(input); i++ {
		for j := i; j < len(input); j++ {
			tempValue += input[j]
			if tempValue > key {
				break
			} else if tempValue == key {
				tempSlice := input[i:j]
				smallest := 1<<32 - 1
				max := 0
				for _, number := range tempSlice {
					if number < smallest {
						smallest = number
					}
					if number > max {
						max = number
					}
				}
				return smallest + max
			}
		}
		tempValue = 0
	}
	return 0
}

func findRuleBreakingNumber(input []int) int {
	pairFound := false

	for i := 25; i < len(input); i++ {
		var tempInput []int

		// Storing only the numbers that are smaller than the 26th one (for positive numbers, if a + b = c then a and b are both smaller than c)
		for j := -25; j < 0; j++ {
			if input[i+j] < input[i] {
				tempInput = append(tempInput, input[i+j])
			}
		}

		// Looping through the entire input and looking for a pair
		for j := 0; j < len(tempInput); j++ {
			for k := j + 1; k < len(tempInput); k++ {
				if j != k && tempInput[j]+tempInput[k] == input[i] {
					// fmt.Printf("Left: %v, Right: %v, Total = %v. Looking for: %v", tempInput[j], tempInput[k], tempInput[j]+tempInput[k], input[i])
					pairFound = true
					break
				}
			}
			if pairFound {
				break
			}
		}

		if !pairFound {
			return input[i]
		}
		pairFound = false
	}
	return 0
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
