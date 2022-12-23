'''
Author: Luke Moss 'Mossdog' Hughes
Note: I hope nobody expects comments on this abstract mess B)
'''

import sys
import random
import numpy as np

def main():
    parts = []
    for i in range(1, len(sys.argv)):
        parts.append(sys.argv[i])
    #parts = ["Luke", "David", "Conor", "Ryan", "James", "Keith", "Daniel", "Jordan", "Taylor"]
    points = genPoints(parts)

    # Display who's pointing to who
    print("PLAYERS")
    for i in range(len(parts)):
        print(f"{i} | {parts[i]} points to {parts[points[i]]}")

    print(f"\nPlease choose a leader! (0 - {len(parts)-1})")
    leader = int(input()) # Store leader in curr
    
    runGame(parts, points, leader)
    findLoops(parts, points)


def findLoops(parts, points):
    loops = []
    for i in range(len(parts)):
        curr = i
        loop = []

        for j in range(len(parts)):
            loop.append(parts[curr])
            curr = points[curr]

            if curr == i:
                stored = None
                
                for iLoop in loops:
                    if loop[0] in iLoop:
                        stored = True

                if not stored:
                    loops.append(loop)

                break

    print(f"\nThere are {len(loops)} loops, the longest is {len(max(loops, key=len))} long and is shown below\n{max(loops, key=len)}")

    if len(loops)>1:
        print("\nOther loops")

        for loop in loops:
            if loop != max(loops, key=len):
                print(loop)


def runGame(parts, points, leader):
    superDict = {1:'\u02e2\u1d57', 2:'\u207F;\u1D48', 3:'\u02B3\u1d48'} # 1:st, 2:nd, 3:rd
    thStr = '\u1D57\u02B0'
    loop = None
    curr = leader

    print(f"\n{parts[curr]}! You are the leader!\nHow many steps would you like to take?")
    n = int(input())

    print("\nRUNNING...")
    for i in range(n):
        print(f"{i+1} | {parts[curr]} -> {parts[points[curr]]}")
        curr = points[curr]

        if curr == leader and loop == None:
            loop = i+1

    print(f"\nMy brother in christ, {parts[curr]}, must consume the Death Juice!")

    if loop != None:
        # thStr is the default value (st) which is used for all numbers from 10-20
        print(f"\nA loop was entered on the {loop}{superDict.get(loop if loop<20 else loop%10, thStr)} step")


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