# 2022 advent of code
# day 08 treetop tree house

def main():
    treeGrid = openFile('treetop_treehouse.txt')
    #treeGrid = openFile('test_treehouse.txt')

    rows, cols = findRowsCols(treeGrid)
    visibleTrees=findVisibleTrees(rows, cols)
    maxScore = findScenicScores(rows, cols)
    

    print('visible trees', visibleTrees)
    print('highest scenic score', maxScore)

def findVisibleTrees(rows, cols):                       
    visibleTrees = (len(rows[0])*2)+(len(cols[0])*2)-4
    for rowNum, trees in rows.items():
        if rowNum > 0 and rowNum < len(rows.keys())-1:
            for loc in range(1,len(trees)-1):
                visibility = set()
                treeHeight = trees[loc]
                leftNeighbors = trees[:loc]
                rightNeighbors = trees[loc+1:]
                upNeighbors = cols[loc][:rowNum]
                downNeighbors = cols[loc][rowNum+1:]

                leftVisible= checkNeighbors(leftNeighbors, treeHeight, 'left')
                rightVisible = checkNeighbors(rightNeighbors, treeHeight, 'right')
                upVisible = checkNeighbors(upNeighbors, treeHeight, 'up')
                downVisible = checkNeighbors(downNeighbors, treeHeight, 'down')

                visibility = {leftVisible, rightVisible, upVisible, downVisible}
                if True in visibility:
                    visibleTrees+=1
    return visibleTrees


def findScenicScores(rows, cols):
    scenicScores = set()
    for rowNum, trees in rows.items():
        if rowNum > 0 and rowNum < len(rows.keys())-1:
            for loc in range(1,len(trees)-1):
                treeHeight = trees[loc]
                leftNeighbors = trees[:loc]
                rightNeighbors = trees[loc+1:]
                upNeighbors = cols[loc][:rowNum]
                downNeighbors = cols[loc][rowNum+1:]

                leftVis = findNumVisibleTrees(leftNeighbors, treeHeight, 'left')
                rightVis = findNumVisibleTrees(rightNeighbors, treeHeight, 'right')
                upVis = findNumVisibleTrees(upNeighbors, treeHeight, 'up')
                downVis = findNumVisibleTrees(downNeighbors, treeHeight, 'down')

                treeScore = leftVis*rightVis*upVis*downVis
                scenicScores.add(treeScore)
    return max(scenicScores)

def checkNeighbors(neighborList, treeHeight, side):
    visible = False
    neighbors = []
    if side == 'left' or side == 'up':
        for i in range(len(neighborList)-1, -1, -1):
            neighbors.append(neighborList[i])
    elif side == 'right' or side == 'down':
        neighbors = neighborList
        
    for neighbor in neighbors:
        if treeHeight > neighbor:
            visible = True
        elif treeHeight == neighbor:
            visible = False
            return visible
        else:
            visible = False
            return visible
    return visible

def findNumVisibleTrees(neighborList, treeHeight, side):
    numTrees = 0
    neighbors = []
    if side == 'left' or side == 'up':
        for i in range(len(neighborList)-1, -1, -1):
            neighbors.append(neighborList[i])
    elif side == 'right' or side == 'down':
        neighbors = neighborList

    for neighbor in neighbors:
        if treeHeight > neighbor:
            numTrees += 1
        elif treeHeight == neighbor:
            numTrees += 1
            return numTrees
        else:
            numTrees += 1
            return numTrees
            
    return numTrees
    

def findRowsCols(treeGrid):
    cols = dict()
    rows = dict() 
    
    for i in range(len(treeGrid)):
        for j in range(len(treeGrid[i])):
            if i not in cols.keys():
                cols[i] = []
            if i not in rows.keys():
                rows[i] = []
            cols[i].append(treeGrid[j][i])
            rows[i].append(treeGrid[i][j])
    return rows, cols


def printDict(dictName):
    for k, v in dictName.items():
        print(k, ':', v)
        print('\n')

def openFile(fileName):
    with open(fileName) as f:
        file = f.readlines()
    for row in range(len(file)):
        file[row] = file[row].replace('\n', '')
        file[row] = list(file[row])
        for height in range(len(file[row])):
            file[row][height] = int(file[row][height])

    return file
main()

