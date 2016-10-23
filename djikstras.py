#Vitalii Stadnyk
import sys

# setting weight of the node
def setValue(node, my_weight):
   my_index = vertexes.index(node)
   weight[my_index] = my_weight

# getting weight of the node
def getValue(node):
   my_index = vertexes.index(node)
   return weight[my_index]

# setting previous node in the shortest path
def setPred(node, pred):
   my_index = vertexes.index(node)
   prev[my_index] = pred

# getting previous node in the shortest path
def getPred(node):
   my_index = vertexes.index(node)
   return prev[my_index]

# finding node with smallest weight that hasn't been visited yet
def findSmallest(array):
    minimum = float('inf')
    p = 0
    for i in array:
        if i < minimum:
            for x in range(len(array)):
                if array[x] == i:
                    if vertexes[x] not in visited:
                        minimum = i
                        p = x
                        break
    return p

query = [] # stores the input
vertexes = [] #stores all the vertixes
visited = [] #keeps track of all non-visited vertixes
prev = [] # stores predecessors for each vertex
weight = [] # stores weight for each vertex

for line in open(sys.argv[1],'r'):
    query.append(line.split())

for x in query:
    for i in range (2):
        if x[i] not in vertexes:
            vertexes.append(x[i])
            weight.append(float('inf'))
            prev.append(-1)

for i in vertexes:
    source = i
    setValue(source, 0)
    while len(visited) != len(vertexes):
        smallest_value = vertexes[findSmallest(weight)]
        # finding neighbor nodes and updating path if possible
        for array in query:
            if array[0] == smallest_value and array[1] not in visited:
                if getValue(smallest_value) + int(array[2]) < getValue(array[1]):
                    setValue(array[1],getValue(smallest_value) + int(array[2]))
                    setPred(array[1],smallest_value)
            elif array[1] == smallest_value and array[0] not in visited:
                if getValue(smallest_value) + int(array[2]) < getValue(array[0]):
                    setValue(array[0],getValue(smallest_value) + int(array[2]))
                    setPred(array[0],smallest_value)
        visited.append(smallest_value)
    for k in vertexes:
        p = k
        if k != source:
            while getPred(p)!= source:
                p = getPred(p)
            print("source =", source, ", destination =", k , ", route =", p, ", cost =", getValue(k))
        else:
            print("source =", source, ", destination =", k , ", route =", getPred(k), ", cost =", getValue(k))
    print()
    prev = []
    weight = []
    visited = []
    vertexes = []
    for x in query:
        for m in range (2):
            if x[m] not in vertexes:
                weight.append(float('inf'))
                prev.append(-1)
                vertexes.append(x[m])
