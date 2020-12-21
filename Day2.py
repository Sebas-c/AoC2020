# Advent of Code - Day 2

# Retrieving every line from the file
passwords = open("input-Day2.txt").readlines()

# Creating a counter for valid password
first_rule_counter = 0
second_rule_counter = 0


# Turns a line from the input into a list with positions at index 0, letter at index 1 and password at index 2
def breakdown_input_line(file_line):
    # Splitting line by space
    new_line = file_line.split()
    # Splitting first input by dash
    numbers = new_line[0].split("-")
    # Transforming List of string in List of int (there might be a better way to do that on the previous line)
    numbers = [int(i) for i in numbers]
    # Storing letter to check for
    letter = new_line[1]
    letter = letter.replace(":", "")
    # Storing password to check for
    password = new_line[2]

    return [numbers, letter, password]


# Checks if a password matches the pattern
def is_password_valid(file_line):
    # Storing positions
    numbers = file_line[0]
    # Storing letter to check for
    letter = file_line[1]
    # Storing password to check for
    password = file_line[2]

    # Counter for characters matching the ones we're looking for
    matching_characters = 0

    # Checking each character in the password for matches
    for character in password:
        if character == letter:
            matching_characters += 1

    # If the number of matching characters is within limits, return true
    if numbers[0] <= matching_characters <= numbers[1]:
        return True
    else:
        return False


def is_password_valid2(file_line):
    # Storing positions
    numbers = file_line[0]
    # Storing letter to check for
    letter = file_line[1]
    # Storing password to check for
    password = list(file_line[2])

    # Counter for characters matching the ones we're looking for
    match_on_first_position = False
    match_on_second_position = False

    # print("numbers: " + str(numbers[0]) + ", " + str(numbers[1]))
    # print("Looking for:" + letter)

    # Checking each character in the password for matches
    if password[(numbers[0] - 1)] == letter:
        # print("first position match on: " + file_line[2])
        match_on_first_position = True

    if password[(numbers[1] - 1)] == letter:
        # print("second position match on: " + file_line[2])
        match_on_second_position = True

    # If the number of matching characters is within limits, return true
    if match_on_first_position != match_on_second_position:
        return True
    else:
        return False


# Checking validity of all passwords
for line in passwords:
    if is_password_valid(breakdown_input_line(line)):
        first_rule_counter += 1

    if is_password_valid2(breakdown_input_line(line)):
        second_rule_counter += 1

print("Number of valid passwords with the first rule: " + str(first_rule_counter))
print("Number of valid passwords with the second rule: " + str(second_rule_counter))
