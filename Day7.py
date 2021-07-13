# Advent of Code - Day 7
import re


# Nodes to hold the data
class Bag:
    def __init__(self, adjective, colour, contains, amounts_of_contains):
        self.adjective = adjective
        self.colour = colour
        self.contains = contains
        self.amounts_of_contains = amounts_of_contains
        self.contained_by = []
        self.counted = False

    def add_container(self, container):
        self.contained_by.append(container)


# Creating a dictionary to store all the nodes (the adjective/colour combo being unique, it can be used as a key for
# quick access later on)
graph = dict()

# Looping through all the lines to create nodes
for line in open("input-Day7.txt"):
    # Separating the line between the node and what it contains
    bag_name, bag_contains = re.match(r"(.*) contain (.*)\.", line).groups()
    # Removing " bags" from the node name
    bag_name = bag_name[:-5]
    # Breaking the name apart
    bag_adjective, bag_colour = re.match(r"(.*) (.*)", bag_name).groups()

    # Handling bag contains
    bag_contains = bag_contains.split(", ")
    # Creating lists to hold contains and the amounts
    contains_bags = []
    amount_of_contains = []
    # if there are bags contained
    if bag_contains[0] != "no other bags":
        # Loop through the different bags contained
        for i in range(len(bag_contains)):
            # Separate numbers and bag's name
            contains_number, contains_name = re.match(r"([\d]) (.*)", bag_contains[i]).groups()

            # Remove " bag" or " bags" and append name to the list
            if int(contains_number) > 1:
                contains_bags.append(contains_name[:-5])
            else:
                contains_bags.append(contains_name[:-4])
            # Append number to the list
            amount_of_contains.append(contains_number)

    # Creating a new object
    newBag = Bag(bag_adjective, bag_colour, contains_bags, amount_of_contains)

    # Adding the object to the dictionary
    graph[bag_name] = newBag

# Looping through all the lines to create "contained" relationships
for bag in graph:
    for contained in graph[bag].contains:
        graph[contained].add_container(graph[bag])


# Returns all the count of all the parents of a bag
def count_parents(name_of_bag):
    counter = 0
    # If no parents, return 0
    if len(graph[name_of_bag].contained_by) == 0:
        return 0
    else:
        # Loop through all the containers
        for container in graph[name_of_bag].contained_by:
            container_name = container.adjective + ' ' + container.colour
            # If the bag has not been counted yet
            if not container.counted:
                # Set to counted
                container.counted = True
                # Recursively call to count the parents of the container
                counter += count_parents(container_name)
                # Count this bag
                counter += 1
        return counter


# Counts how many children a bags must contain
def count_children(name_of_bag):
    counter = 0
    # If the bag doesn't contain children, return 0
    if not len(graph[name_of_bag].contains) > 0:
        return 0
    else:
        # Loop through all the bags contained
        for j in range(len(graph[name_of_bag].contains)):
            # Add to the counter:
            # number of bags contained in the contained bag * amount of bags contained + amounts of bag contained
            counter += count_children(graph[name_of_bag].contains[j]) * int(graph[name_of_bag].amounts_of_contains[j])\
                       + int(graph[name_of_bag].amounts_of_contains[j])
        return counter


print('shiny gold can be contained by ' + str(count_parents('shiny gold')) + ' bags.')
print('shiny gold contains ' + str(count_children('shiny gold')) + ' bags.')
