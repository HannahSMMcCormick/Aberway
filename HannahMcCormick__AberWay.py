#! /bin/python

from aberway_background_code import create, update, main_loop
import time
import math
import pygame 

ColourFlip = False

    
screen, bg, lineList, nodeList = create(ColourFlip)
update(None, screen, bg, lineList, nodeList, None, None, None, None, 0)


# --- SET THESE VALUES TO AN EXAMPLE ---
startPos = 0
listOfNodesToPass = [10,11,14]
length = 676.75
error = 0.06

def path_update():
    ListOfNodeId = [0,2,10,13,11,14,15] #set the value of this to the nodes that your path takes
    start = time.time_ns() # for timing your algorithm
    # ---------- ---------- YOUR CODE GOES HERE ---------- ----------

    Journey = []

    currentNode = startPos

    endNode = listOfNodesToPass[-1]

    distance = math.dist(nodeList[startPos][0],nodeList[endNode][0])

    #print(distance)#

    shortNode = None

    testDistance = distance


    while currentNode != endNode:


        for i in range(len(nodeList[currentNode][3])):

            testNode = nodeList[currentNode][3][i]

            tempDistance = math.dist(nodeList[testNode][0], nodeList[endNode][0])

            if tempDistance < testDistance:

                testDistance = tempDistance

                shortNode = testNode
            

        if shortNode is not None:

            currentNode = shortNode

            Journey.append(currentNode)

        else:

            print("ERROR")

    print(Journey)



    # ---------- ---------- ---------- ---------- ---------- ---------- ----------
    end = time.time_ns()
    update(ListOfNodeId, screen, bg, lineList, nodeList, startPos, listOfNodesToPass, length, error, end - start)

path_update()
main_loop()
