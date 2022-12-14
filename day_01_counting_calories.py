# 2022 advent of code
# day 01: counting calories

with open('calories.txt') as f:
    lines = f.readlines()

strippedList = []
for item in lines:
    if len(item)>=1 and item != '\n':
        item.replace('\n', '')
        strippedList.append(int(item))
    else:
        strippedList.append(item)

strippedList.append('\n')
caloriesByElf = []
count = 1
totalCalories = 0
for num in strippedList:
    if isinstance(num, int):
        totalCalories += num
    else:
        caloriesByElf.append(totalCalories)
        totalCalories = 0
        count+=1

caloriesByElf.sort()
greatestCals = caloriesByElf[-1]
topThree = caloriesByElf[-1] + caloriesByElf[-2] + caloriesByElf[-3]

print('greatest calories: ' + str(greatestCals))
print('top three calories total: ' + str(topThree))

