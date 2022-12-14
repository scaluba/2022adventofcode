# 2022 advent of code
# day 04 camp cleanup

def main():
    with open('camp_cleanup.txt') as f:
        lines = f.readlines()

    elfGroups = []
    for group in range(len(lines)):
        lines[group] = lines[group].replace('\n', '')
        lines[group] = lines[group].split(',')
        elfGroups.append(lines[group][0].split('-') + lines[group][1].split('-'))

    for group in elfGroups:
        for idNum in range(len(group)):
            group[idNum] = int(group[idNum])

    findFullOverlap(elfGroups)
    findAnyOverlap(elfGroups)

def findFullOverlap(elfGroups):
    totalOverlap = 0
    for groupNum in range(len(elfGroups)):
        if elfGroups[groupNum][0]<=elfGroups[groupNum][2] and elfGroups[groupNum][1]>=elfGroups[groupNum][3]:
            totalOverlap+=1
            
        elif elfGroups[groupNum][3]>=elfGroups[groupNum][1] and elfGroups[groupNum][2]<=elfGroups[groupNum][0]:
            totalOverlap+=1

    print('complete overlap:', totalOverlap)

def findAnyOverlap(elfGroups):
    noDup = 0
    for groupNum in range(len(elfGroups)):
        if elfGroups[groupNum][1]<elfGroups[groupNum][2] or elfGroups[groupNum][0]>elfGroups[groupNum][3]:
            noDup += 1
        
    totalOverlap = len(elfGroups)-noDup
    print('any overlap:', totalOverlap) 
        

main()

