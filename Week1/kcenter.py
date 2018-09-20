from queue import PriorityQueue
from random import randint
import numpy as np
import time

def main():

    fileNumber = pickFile()

    matrix = open("data/kcenter-" + str(fileNumber) + ".txt").read()
    matrix = [item.split() for item in matrix.split('\n')[:-1]]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = int(matrix[i][j])

    numberOfV = matrix[0][0]
    numberOfE = matrix[0][1]
    k = matrix[0][2]

    graphMatrix = [[101 for x in range(numberOfV)] for y in range(numberOfV)]

    for edge in range(numberOfE):
            i = matrix[edge + 1][0]
            j = matrix[edge + 1][1]
            graphMatrix[i - 1][j - 1] = matrix[edge + 1][2]
            graphMatrix[j - 1][i - 1] = matrix[edge + 1][2]

    shortestPathMatrix = [[None for x in range(numberOfV)] for y in range(numberOfV)]

    for i in range(numberOfV):
        for j in range(numberOfV):
            shortestPathMatrix[i][j] = dijkstra(i, j, graphMatrix, numberOfV)

    center = [0]

    for c in range(k - 1):
        distanceToCenters = [[101 for x in range(numberOfV)] for y in range(len(center))]

        for i in range(numberOfV):
            if i not in center:
                for j in range(len(center)):
                    distanceToCenters[j][i] = shortestPathMatrix[i][center[j]]

        minDistanceToCenters = distanceToCenters[0]

        for i in range(len(center)):
            for j in range(numberOfV):
                if minDistanceToCenters[j] > distanceToCenters[i][j]:
                    minDistanceToCenters[j] = distanceToCenters[i][j]

        for i in range(numberOfV):
            if minDistanceToCenters[i] == 101:
                minDistanceToCenters[i] = 0

        center.append(minDistanceToCenters.index(max(minDistanceToCenters)))

    possibleLongestPathsToCenters = [[101 for x in range(numberOfV)] for y in range(len(center))]

    for i in range(len(center)):
        possibleLongestPathsToCenters[i] = shortestPathMatrix[center[i]]

    for i in range(len(center)):
        for j in range(numberOfV):
            if possibleLongestPathsToCenters[i][j] > 1000:
                possibleLongestPathsToCenters[i][j] = 0

    longestPathToCenters = possibleLongestPathsToCenters[0]

    for i in range(len(center)):
        for j in range(numberOfV):
            if longestPathToCenters[j] > possibleLongestPathsToCenters[i][j]:
                longestPathToCenters[j] = possibleLongestPathsToCenters[i][j]

    print("The maximum distance is: {}".format(max(longestPathToCenters)))
    print("The following centers: {}".format(center))

def pickFile():
    x = input("Which file do you want to use? ")
    return x

def dijkstra(currentNode, goal, graph, numberOfVertices):
    if currentNode == goal:
        return 101

    visited = {}
    queue = PriorityQueue()

    distances = [graph[currentNode][x] for x in range(numberOfVertices)]

    visited[str(currentNode)] = "visited"

    for i in range(numberOfVertices):
        if str(i) not in visited.keys():
            queue.put((distances[i], i))

    while str(currentNode) in visited.keys():
        currentDistance, currentNode = queue.get()

    while currentNode != goal:
        for i in range(numberOfVertices):
            if graph[currentNode][i] + currentDistance < distances[i]:
                distances[i] = graph[currentNode][i] + currentDistance

        for i in range(numberOfVertices):
            if str(i) not in visited.keys():
                    queue.put((distances[i], i))

        visited[str(currentNode)] = "visited"

        while str(currentNode) in visited.keys():
            currentDistance, currentNode = queue.get()

    return currentDistance

if __name__ == "__main__":
    main()
