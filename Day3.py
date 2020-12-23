# Advent of Code - Day 3

# Retrieving input file and remove first line
geological_map = open('input-Day3.txt').read().splitlines()

geological_map.pop(0)


def path_checking(position_horizontal_increment, position_vertical_increment):
    # Counter for trees on the path position being examined and line being examined
    trees_encountered = 0
    horizontal_position = 0
    vertical_position = 0
    # Looping through all the lines of the map
    for line in geological_map:
        # Incrementing line counter
        vertical_position += 1
        # Check if that line should be examined
        if vertical_position % position_vertical_increment == 0:
            # Adding 3 to the current position
            horizontal_position += position_horizontal_increment
            # Checking if our position is still on the line
            if horizontal_position < len(line):
                # Checking if we hit a tree
                if line[horizontal_position] == "#":
                    trees_encountered += 1
            # If not on the line, bring it back to the matching position in the beginning
            else:
                horizontal_position = horizontal_position - len(line)
                # Checking if we hit a tree
                if line[horizontal_position] == "#":
                    trees_encountered += 1

    return trees_encountered


print("First result: " + str(path_checking(3, 1)))
print("Second result: " + str(path_checking(1, 1) * path_checking(3, 1) * path_checking(5, 1) * path_checking(7, 1) * 
                              path_checking(1, 2)))
