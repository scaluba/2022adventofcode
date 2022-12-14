# 2022 advent of code
# day 06 tuning trouble

def main():
    with open('tuning_trouble.txt') as f:
        lines = f.readlines()

    packets = cleanString(lines)
    
    pt1 = findStartingPacket(packets, 4)
    print('location of first packet:',pt1)

    pt2 = findStartingPacket(packets, 14)
    print('location of second packet:',pt2)


def findStartingPacket(packets, length):
    currentPacket = []
    for i in range(len(packets)):
        if packets[i] in currentPacket:
            loc = currentPacket.index(packets[i])
            currentPacket = currentPacket[loc+1:]
            currentPacket.append(packets[i])
        else:
            currentPacket.append(packets[i])
        
        if len(currentPacket) == length:
            return i+1
            
def cleanString(lines):
    lines = str(lines)
    lines = lines.replace('\'', '')
    lines = lines.replace('\\n', '')
    lines = lines.replace('[', '')
    lines = lines.replace(']', '')
    return lines

main()

