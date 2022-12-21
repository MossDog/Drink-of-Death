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

    curr = leader

    print("{}! You are the leader!\nHow many steps would you like to take?".format(parts[curr]))
    n = int(input())
    for i in range(n):
        print("{} | {} -> {}".format(i, parts[curr], parts[points[curr]]))
        curr = points[curr]
    print("{}, my brother in christ, you must consume the liquid! 0_0".format(parts[curr]))


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