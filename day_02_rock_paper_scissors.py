# 2022 advent of code
# day 02: rock paper scissors

def main():
    with open('rock_paper_scissors.txt') as f:
        lines = f.readlines()

    opponent = []
    player = []

    for item in lines:
        opponent.append(item[0])
        player.append(item[-2])

    opponentPoints, playerPoints = part01(opponent, player)
    playerPoints = part02(opponent, player)
    playerPoints = part03(opponent, player)
    # print('opponent points: ' + str(opponentPoints))
    print('player points: ' + str(playerPoints))

def part01(opponent, player):
    opponentPoints = 0
    playerPoints = 0
    for roundNum in range(len(opponent)):
        if opponent[roundNum] == 'A':
            if player[roundNum] == 'X':
                opponentPoints += 4
                playerPoints += 4
            elif player[roundNum] == 'Y':
                opponentPoints += 1
                playerPoints += 8
            else:
                opponentPoints += 7
                playerPoints += 3
        elif opponent[roundNum] == 'B':
            if player[roundNum] == 'X':
                opponentPoints += 8
                playerPoints += 1
            elif player[roundNum] == 'Y':
                opponentPoints += 5
                playerPoints += 5
            else:
                opponentPoints += 2
                playerPoints += 9
        else:
            if player[roundNum] == 'X':
                opponentPoints += 3
                playerPoints += 7
            elif player[roundNum] == 'Y':
                opponentPoints += 9
                playerPoints += 2
            else:
                opponentPoints += 6
                playerPoints += 6
    return opponentPoints, playerPoints


def part02(opponent, player):
    outcomePoints = {'X': 0, 'Y': 3, 'Z': 6}
    playerPoints = 0
    for roundNum in range(len(player)):
        playerPoints += outcomePoints[player[roundNum]]
        if opponent[roundNum] == 'A':
            if player[roundNum] == 'X':
                playerPoints += 3 
            elif player[roundNum] == 'Y':
                playerPoints += 1
            else:
                playerPoints += 2
        elif opponent[roundNum] == 'B':
            if player[roundNum] == 'X':
                playerPoints += 1
            elif player[roundNum] == 'Y':
                playerPoints += 2
            else:
                playerPoints += 3
        else:
            if player[roundNum] == 'X':
                playerPoints += 2
            elif player[roundNum] == 'Y':
                playerPoints += 3
            else:
                playerPoints += 1
    return playerPoints

def part03(opponent, player):
    # follows pointing for part 02
    points = {'X': [0, {'A': 3, 'B': 1, 'C': 2}],
              'Y': [3, {'A': 1, 'B': 2, 'C': 3}],
              'Z': [6, {'A': 2, 'B': 3, 'C': 1}]}

    playerPoints = 0
    for roundNum in range(len(player)):
        outcome = player[roundNum]
        oppChoice = opponent[roundNum]
        playerPoints += points[outcome][0] + points[outcome][1][oppChoice]

    return playerPoints

main()
