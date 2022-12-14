# 2022 advent of code
# day 05 supply stacks
import string


def main():
    with open('supply_stacks.txt') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = lines[i].replace('move ', '')
        lines[i] = lines[i].replace(' from ', '')
        lines[i] = lines[i].replace(' to ', '')

    actions = lines[10:]
    stacks = createStacks(lines)
    columns = createColumns(stacks)
#    moveStacksPart1(actions, columns)
    moveStacksPart2(actions, columns)

def moveStacksPart1(actions, columns):
    for action in actions:
        startColumn = int(action[-2])-1
        endColumn = int(action[-1])-1
        action = action[:-2]
        numToMove=int(action)
        for i in range(numToMove):
            columns[endColumn].insert(0,columns[startColumn][0])
            columns[startColumn].pop(0)
    printStacks(columns)

def moveStacksPart2(actions, columns):
    for action in actions:
        startColumn = int(action[-2])-1
        endColumn = int(action[-1])-1
        action = action[:-2]
        numToMove=int(action)
        for i in range(numToMove):
            loc = numToMove-(i+1)
            columns[endColumn].insert(0,columns[startColumn][loc])
            columns[startColumn].pop(loc)
    printStacks(columns)
    
def createStacks(lines):
    stacks = []
    for row in lines[:8]:
        newRow = []
        for letter in row:
            newRow.append(letter)
        stacks.append(newRow)
    return stacks

def createColumns(stacks):
    alphabet = list(string.ascii_letters)
    columns = [[],[],[],[],[],[],[],[],[]]
    for i in range(len(stacks)):
        for j in range(1,34,4):
            colNum = (j//4)
            if stacks[i][j] in alphabet:
                columns[colNum].append(stacks[i][j])
    return columns


def printStacks(columns):
    i=1
    for row in columns:
        print(i,row)
        i+=1

main()

