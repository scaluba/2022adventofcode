# 2022 advent of code
# day 03 rucksack reorganization

import string

def main():
    with open('rucksack_reorganization.txt') as f:
        lines = f.readlines()

    part_01(lines)
    part_02(lines)

def part_01(lines):
    rucksacks = rucksack_organization(lines)
    duplicates = find_duplicate_letters(rucksacks)
    priorityValue = create_priority_values()
    total = add_total_priority(priorityValue, duplicates)
    print('total: ' + str(total))

def part_02(lines):
    groups = elf_groups(lines)
    duplicates = find_duplicate_letters(groups)
    priorityValue = create_priority_values()
    total = add_total_priority(priorityValue, duplicates)
    print('total: ' + str(total))

def elf_groups(lines):
    groups = dict()
    for elfNum in range(0, len(lines), 3):
        lines[elfNum] = lines[elfNum].replace('\n', '')
        lines[elfNum+1] = lines[elfNum+1].replace('\n', '')
        lines[elfNum+2] = lines[elfNum+2].replace('\n', '')
        groups[int(elfNum/3)] = [lines[elfNum], lines[elfNum+1], lines[elfNum+2]]

    return groups

def rucksack_organization(lines):
    rucksacks = dict()
    for rucksackNum in range(len(lines)):
        lines[rucksackNum] = lines[rucksackNum].replace('\n', '')
        numItems = int(len(lines[rucksackNum])/2)
        rucksacks[rucksackNum] = [lines[rucksackNum][:numItems], lines[rucksackNum][numItems:]]

    return rucksacks

def find_duplicate_letters(rucksacks):
    duplicates = []
    for rucksackNum, supplies in rucksacks.items():
        dups = set()
        for item in supplies[0]:
            if len(supplies)==2 and item in supplies[1] and item not in dups:
                dups.add(item)
                duplicates.append(item)
            elif len(supplies)==3 and item in supplies[1] and item in supplies[2] and item not in dups:
                dups.add(item)
                duplicates.append(item)
    return duplicates

def create_priority_values():
    priorityValue = dict()
    alphabet = list(string.ascii_letters)
    for i in range(1, 53):
        priorityValue[alphabet[i-1]] = i

    return priorityValue

def add_total_priority(priorityValue, duplicates):
    total = 0
    for letter in duplicates:
        total += priorityValue[letter]
    return total

main()

