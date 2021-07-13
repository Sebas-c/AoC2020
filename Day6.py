# Advent of Code - Day 4
import re

unique_answers, group_answers, total_group_answers = [""], [], []
total_unique_answers, total_group_answers_value = 0, 0

for line in open("input-Day6.txt"):
    if line != "\n":
        line = line.rstrip("\n")
        group_answers.append(line)
        for letter in line:
            if re.search(letter, unique_answers[-1]) is None:
                unique_answers[-1] += letter
    else:
        unique_answers.append("")
        total_group_answers.append(group_answers)
        group_answers = []

for answer in unique_answers:
    total_unique_answers += len(answer)

for group in total_group_answers:
    answered_by_all = True
    i = 0
    group = sorted(group, key=len)
    print(group)
    for letter in group[0]:
        for answer in group[1:]:
            if re.search(letter, answer) is None:
                answered_by_all = False
                break
        if answered_by_all:
            total_group_answers_value += 1
        answered_by_all = True


print("Total unique answers: " + str(total_unique_answers))
print("Total non unique answers: " + str(total_group_answers_value))
