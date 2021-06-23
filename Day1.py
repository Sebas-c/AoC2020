# Advent of Code - Day 1
import time

numbers = open("input-Day1.txt").readlines()

found_duo = False
found_trio = False
start_time = time.time_ns()

for number in numbers:
    for number2 in numbers:
        if not found_duo and int(number) + int(number2) == 2020:
            found_duo = True
            print("Duo: " + str(int(number) * int(number2)))

        for number3 in numbers:
            if not found_trio and int(number) + int(number2) + int(number3) == 2020:
                found_trio = True
                print("Trio: " + str(int(number) * int(number2) * int(number3)))

print("Total time:" + str(time.time_ns() - start_time))
