import sys
import random
import numpy as np

def main():
    # parts = []
    # for i in range(1, len(sys.argv)):
        #parts.append(sys.argv[i])
    parts = ["Luke", "David", "Conor", "Ryan", "James", "Keith", "Daniel", "Jordan", "Taylor"]
    points = genPoints(parts)

    # Display who's pointing to who
    for i in range(len(parts)):
        print("{} | {} points to {}".format(i, parts[i], parts[points[i]]))

    print("Please choose a leader! (0 - {})".format(len(parts)-1))
    leader = int(input()) # Store leader in curr
    
    runGame(parts, points, leader)


def runGame(parts, points, leader):
    superDict = {1:'\u02e2\u1d57', 2:'\u207F;\u1D48', 3:'\u02B3\u1d48'} # 1:st, 2:nd, 3:rd
    loop = None
    curr = leader

    print("{}! You are the leader!\nHow many steps would you like to take?".format(parts[curr]))
    n = int(input())

    for i in range(n):
        print("{} | {} -> {}".format(i, parts[curr], parts[points[curr]]))
        curr = points[curr]

        if(curr == leader and loop == None):
            loop = i

    print("MFW {}, my brother in christ, must consume the Death Juice! 0_0".format(parts[curr]))

    if loop != None:
        # \u1D57\u02B0 is the default value (st) which is used for all numbers from 10-20
        print("A loop was entered on the {}{} step".format(loop, superDict.get(loop if (loop<20) else (loop%10), '\u1D57\u02B0')))


def genPoints(parts):
    points = []
    nums = np.arange(len(parts))

    for i in range(len(parts)):
        test = [n for n in nums if n != i and n not in points]

        if len(test)==0:
            points = genPoints(parts)

        points.append(random.choice(test))
        
    return points


if __name__ == '__main__':
    main()