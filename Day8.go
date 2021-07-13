package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	input := fileRead("../Inputs/Day8-input.txt")

	// Printing value of acc before infinite loop
	accValue, finished := accValueCounter(input)
	if finished {
		fmt.Printf("Last acc value before infinite loop: %v\n", accValue)
	}

	expectedAccValue, finishedLoop := expectedAccValue(input)
	if finishedLoop {
		fmt.Printf("Expected acc value: %v\n", expectedAccValue)
	}

}

// Returns the value of the acc and true if it ended in an infinite loop
func accValueCounter(input []string) (int, bool) {
	// Variables
	var executedLines []bool
	accValue := 0
	foundInfiniteLoop := false

	// Initializing array as all false
	for i := 0; i < len(input); i++ {
		executedLines = append(executedLines, false)
	}

	// Following the instructions
	for i := 0; i < len(input); {
		re := regexp.MustCompile(`(?P<instruction>[a-z]{3}) (?P<symbol>\+|\-)(?P<value>\d+)`)

		// Removing submatch (i.e. the entire string)
		line := re.FindStringSubmatch(input[i])
		line = line[1:]

		// Checking if the line has already been executed (i.e. infinite loop)
		if executedLines[i] == true {
			foundInfiniteLoop = true
			break
		}

		// Performing the instruction
		switch line[0] {
		case "jmp":
			setCurrentLineTrue(executedLines, i)
			value, errConv := strconv.Atoi(line[2])
			checkError(errConv)
			if line[1] == "+" {
				i += value
			} else {
				i -= value
			}
		case "acc":
			setCurrentLineTrue(executedLines, i)
			value, errConv := strconv.Atoi(line[2])
			checkError(errConv)
			if line[1] == "+" {
				accValue += value
			} else {
				accValue -= value
			}
			i++
		case "nop":
			setCurrentLineTrue(executedLines, i)
			i++
		}
	}

	return accValue, foundInfiniteLoop
}

// Returns the expected acc value and a false if no value was found to break the infinite loop
func expectedAccValue(input []string) (int, bool) {
	// Finding the combination that solves the infinite loop (through brute force)
	for i := 0; i < len(input); i++ {
		// Regex to break down the line into a slice
		re := regexp.MustCompile(`(?P<instruction>[a-z]{3}) (?P<symbol>\+|\-)(?P<value>\d+)`)

		// Removing submatch (i.e. the entire string)
		line := re.FindStringSubmatch(input[i])
		line = line[1:]

		// Swapping nop and jmp instructions until we find a valid solution
		if line[0] == "jmp" {
			// Swapping the instruction
			input[i] = "nop" + input[i][3:]
			// Getting the acc value and checking if we broke the infinite loop
			accValue, finished := accValueCounter(input)
			if finished == false {
				return accValue, true
			}
			// Resetting the instruction
			input[i] = "jmp" + input[i][3:]
		} else if line[0] == "nop" {
			// Swapping the instruction
			input[i] = "jmp" + input[i][3:]
			// Getting the acc value and checking if we broke the infinite loop
			accValue, finished := accValueCounter(input)
			if finished == false {
				return accValue, true
			}
			// Resetting the instruction
			input[i] = "nop" + input[i][3:]
		}
	}
	return 0, false
}

func fileRead(filePath string) []string {
	// Variables
	var input []string

	// Opening the file
	file, errFile := os.Open(filePath)

	checkError(errFile)

	// Creating a scanner and setting it to read line by line
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	// Appending every line
	for scanner.Scan() {
		input = append(input, scanner.Text())
	}

	// Closing the file
	file.Close()

	return input
}

func setCurrentLineTrue(arrayOfBool []bool, index int) {
	arrayOfBool[index] = true
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
