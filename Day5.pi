# Advent of Code - Day 4
import re

# Variables to be used while looping through the file
all_seat_IDs = []


def letter_to_binary(letter):
    if letter.group(0) == "F" or letter.group(0) == "L":
        return "0"
    else:
        return "1"


for line in open('input-Day5.txt').read().split("\n"):
    # Retrieving the row and column separately
    row, column = line[:7], line[7:]

    # Converting strings into binary
    row, column = re.sub(".", letter_to_binary, row), re.sub(".", letter_to_binary, column)

    # Converting binary to decimal
    row, column = int(row, 2), int(column, 2)

    # Calculating the id of this line and storing it
    all_seat_IDs.append(row * 8 + column)

# Ordering all the seat IDs
all_seat_IDs = sorted(all_seat_IDs)

# Looping through all the IDs to find non-sequential ones
my_ID, i = 0, 0

while i < len(all_seat_IDs):
    if all_seat_IDs[i] + 1 != all_seat_IDs[i + 1]:
        my_ID = all_seat_IDs[i] + 1
        break
    i += 1

# Printing results
print("Highest seat ID: " + str(all_seat_IDs[-1]))
print("My seat ID is: " + str(my_ID))
